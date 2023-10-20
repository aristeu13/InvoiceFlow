from datetime import datetime, timedelta
from random import randint
from celery import Celery
from celery.schedules import crontab
import pytz
from celery.utils.log import get_task_logger
import ssl

from src.core.settings import get_settings
from src.domains.invoice_management import Invoice
from src.repository.invoice_repository import get_invoice_repository

logger = get_task_logger(__name__)
setting = get_settings()

work = Celery(
    "tasks",
    broker_user_ssl={"ssl_cert_reqs": ssl.CERT_NONE} if setting.broker_ssl else None,
    broker=setting.broker_url,
)


work.conf.task_serializer = "pickle"
work.conf.result_serializer = "json"
work.conf.event_serializer = "json"
work.conf.accept_content = ["application/json", "application/x-python-serialize"]
work.conf.result_accept_content = ["application/json", "application/x-python-serialize"]
work.conf.task_acks_late = True
work.conf.worker_prefetch_multiplier = 1
work.conf.worker_max_memory_per_child = 100_000  # 100MB
work.conf.timezone = "America/Sao_Paulo"  # type: ignore
work.conf.broker_connection_retry_on_startup = True


@work.task(name="send_invoices", ignore_result=True)
def send_invoices():
    invoice_start_datetime = datetime.fromisoformat(setting.invoice_start_datetime)
    end_date = invoice_start_datetime + timedelta(days=1)
    now = datetime.now(tz=pytz.timezone("America/Sao_Paulo"))
    if invoice_start_datetime <= now <= end_date:
        to_be_sent = []
        max_generated = randint(8, 12)
        for _ in range(-1, max_generated):
            to_be_sent.append(Invoice.random())
        get_invoice_repository(settings=setting).send(to_be_sent)
        logger.info("Sending invoices...")


work.conf.beat_schedule = {
    "update_market": {
        "task": "send_invoices",
        "schedule": crontab(minute="0", hour="*/3"),
    },
}

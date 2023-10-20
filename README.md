# Invoice Flow

## Official Link

The project is live at [Official Link](https://starkbank-challenge.aristeu.tech/docs).

## Hosting

The project is hosted on AWS (Amazon Web Services).

## Introduction

This project is designed to create the flow of invoices. Below are the commands you'll need to get started with development, testing, and running the application.

## Testing

To run tests, execute the following command:

coverage run -m pytest

To generate a coverage report in lcov format:

coverage lcov

For additional coverage details:

coverage report

## Development

To run the main development server:

uvicorn src.main:app --reload

To run the Celery workers:

celery -A src.work beat --loglevel=info

celery -A src.work worker --loglevel=info

## Using Docker

Alternatively, you can use Docker to run the entire stack with a single command. Make sure to set the following environment variables either in a .env file or in your shell:

- SB_ENVIRONMENT
- SB_PROJECT_ID
- SB_PRIVATE_KEY
- BROKER_URL
- INVOICE_START_DATETIME

Then run:

docker-compose up -d

## License

[MIT](LICENSE)

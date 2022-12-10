# [サービス名]

## Overview

[サービス名] is a service that provides [機能]. This service was developed for HackU Kosen 2022.

## Prerequisites

### Poetry

Dependency management for Python files is done using POETRY.

1. <https://python-poetry.org/docs/#installation>
1. `python -m venv venv`
1. `source venv/bin/activate`
1. `pip install --upgrade pip` (if needed)
1. `poetry install` (After cloning this repository)

### pre-commit (for developers)

This tool defines commands to be executed before committing. It is already defined in `.pre-commit-config.yaml`, so you need to configure it in your environment. Please follow the steps below.

1. <https://pre-commit.com/#installation>
1. `pre-commit install` (After cloning this repository)

## Usage

1. Clone this repository

1. Create fastapi.env with reference to fastapi.env.tmpl

1. Build

    ```sh
    docker-compose build
    ```

1. Dependency install

    ```sh
    docker-compose run --rm fastapi poetry install
    ```

1. Setup Static Files

    ```sh
    docker-compose run --rm fastapi poetry run python manage.py collectstatic --noinput
    ```

1. Migrate

    ```sh
    docker-compose run --rm fastapi poetry run python manage.py migrate
    ```

1. Create Super User for Admin Page

    ```sh
    docker-compose run --rm fastapi poetry run python manage.py createsuperuser
    ```

1. Start Server

    ```sh
    docker-compose up
    ```

## Alias for frequently used commands

```sh
source alias.sh
```

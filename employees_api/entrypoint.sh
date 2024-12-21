#!/bin/bash

export POSTGRES_HOST=postgres

alembic revision --autogenerate
alembic upgrade head

python3 src/main.py -s
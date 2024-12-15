#!/bin/bash

set -e
set -u

psql -U $POSTGRES_USER <<-EOSQL
    CREATE DATABASE $POSTGRES_NAME;
EOSQL
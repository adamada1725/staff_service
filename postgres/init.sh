#!/bin/bash

set -e
set -u

echo ========hello==========
psql -U $POSTGRES_USER <<-EOSQL
    CREATE DATABASE staff;
    CREATE DATABASE task_service;
EOSQL
#!/bin/bash

echo "Waiting for psotgres ..."

while ! nc -z web-db 5432; do
  sleep 0.1
done

echo "Postgres started"

exec "$@"
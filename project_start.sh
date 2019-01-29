#!/usr/bin/env bash
echo "Starting Database"
docker-compose up -d postgres
echo "Wait 10 seconds"
sleep 10
echo "Starting Django"
docker-compose up -d django
docker-compose logs -f

#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


echo "Running migrations..."
just mng migrate

echo "Running collectstatic..."
just collectstatic

echo "Starting server"
exec gunicorn --bind :80 --workers 3 depub.wsgi:application

#!/bin/sh
source $(dirname ${0})/base.sh

info "Running the development server locally"
python manage.py runserver

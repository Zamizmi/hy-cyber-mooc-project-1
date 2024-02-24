#!/bin/bash
python manage.py loaddata ./polls/fixtures/seed.json
python manage.py createsuperuser
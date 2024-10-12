#!/bin/bash

# Install dependencies using full path to pip
C:/Users/Albert/Documents/DJANGO\ PROJECT/SOCIAL\ JUSTICE\ HACKATHON/venv/Scripts/pip.exe install -r requirements.txt

# Collect static files for Django
python manage.py collectstatic --noinput

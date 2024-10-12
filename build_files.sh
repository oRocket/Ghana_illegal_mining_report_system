#!/bin/bash

# Use the full path to Python executable from the virtual environment
C:/Users/Albert/Documents/DJANGO\ PROJECT/SOCIAL\ JUSTICE\ HACKATHON/venv/Scripts/python.exe -m pip install -r requirements.txt

# Collect static files for Django
C:/Users/Albert/Documents/DJANGO\ PROJECT/SOCIAL\ JUSTICE\ HACKATHON/venv/Scripts/python.exe manage.py collectstatic --noinput

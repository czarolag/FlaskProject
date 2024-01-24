#!/usr/bin/env bash
source /venv/bin/activate

export FLASK_APP=flaskr
export FLASK_ENV=development
flask run -p 8080
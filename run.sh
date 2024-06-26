#!/bin/bash

nohup gunicorn -w 4 -b 0.0.0.0:8000 my_flask_app:app > /dev/null 2> /dev/null < /dev/null &
nohup gunicorn -w 4 -b 0.0.0.0:8001 my_flask_app:app > /dev/null 2> /dev/null < /dev/null &
nohup gunicorn -w 4 -b 0.0.0.0:8002 my_flask_app:app > /dev/null 2> /dev/null < /dev/null &
nohup gunicorn -w 4 -b 0.0.0.0:8003 my_flask_app:app > /dev/null 2> /dev/null < /dev/null &
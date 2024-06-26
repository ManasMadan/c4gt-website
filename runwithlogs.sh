#!/bin/bash

nohup gunicorn -w 4 -b 0.0.0.0:8000 my_flask_app:app > /home/ubuntu/logs/cloudmain/8000.log 2> /home/ubuntu/logs/cloudmain/8000.err < /dev/null &
nohup gunicorn -w 4 -b 0.0.0.0:8001 my_flask_app:app > /home/ubuntu/logs/cloudmain/8001.log 2> /home/ubuntu/logs/cloudmain/8001.err < /dev/null &
nohup gunicorn -w 4 -b 0.0.0.0:8002 my_flask_app:app > /home/ubuntu/logs/cloudmain/8002.log 2> /home/ubuntu/logs/cloudmain/8002.err < /dev/null &
nohup gunicorn -w 4 -b 0.0.0.0:8003 my_flask_app:app > /home/ubuntu/logs/cloudmain/8003.log 2> /home/ubuntu/logs/cloudmain/8003.err < /dev/null &
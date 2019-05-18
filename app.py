# -*- coding: utf-8 -*-
from flask import Flask
from celery import Celery
from configparser import ConfigParser
import time
import logging

app = Flask(__name__)
config = ConfigParser()
config.read("config/config.ini", encoding="utf-8")
#app.config['CELERY_BROKER_URL'] = config.get('Celery', 'broker_url')
#celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
#celery.conf.update(app.config)


# logger = logging.getLogger("Joyship")
# logger.setLevel(logging.DEBUG)
# rf_handler = logging.handlers.TimedRotatingFileHandler(filename="log/Joyship.log", when='D', interval=1, \
#                                                        backupCount=0)
# rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
# logger.addHandler(rf_handler)
from view import *

if __name__ == '__main__':
    app.run()

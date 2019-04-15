# -*- coding: utf-8 -*-

import os
import logging


HOME = os.path.dirname(os.path.realpath(__file__))
USER_PATH = os.path.dirname(os.path.expanduser('~user'))
SUBSCRIPTIONS_FILE = os.path.join(USER_PATH, 'subscriptions.json')
SUBSCRIPTIONS_FILE_FOR_TEST = os.path.join(HOME, 'tests/subscriptions.json')
LOGS_FILE = os.path.join(HOME, 'info.log')


logging.basicConfig(filename=LOGS_FILE, level=logging.DEBUG)

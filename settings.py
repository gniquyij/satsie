# -*- coding: utf-8 -*-

import os
import logging


HOME = os.path.dirname(os.path.realpath(__file__))
SUBSCRIPTIONS_FILE = os.path.join(HOME, 'subscriptions.json')
SUBSCRIPTIONS_FILE_FOR_TEST = os.path.join(HOME, 'tests/subscriptions.json')
LOGS_FILE = os.path.join(HOME, 'info.log')


logging.basicConfig(filename=LOGS_FILE, level=logging.DEBUG)

# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
from subscription import Subscription
import settings
import utils
import json


def setup_funcs(url):
    s = Subscription(url)
    funcs = {
        'initialize': s.initialize(settings.SUBSCRIPTIONS_FILE_FOR_TEST, ut=True),
        'update': s.update(settings.SUBSCRIPTIONS_FILE_FOR_TEST, ut=True)
    }
    return funcs


def setup(url, func_name):
    utils.sketch_meta('subscriptions', settings.SUBSCRIPTIONS_FILE_FOR_TEST)
    setup_funcs(url)[func_name]
    with open('subscriptions.json') as input:
        return json.load(input)


class TestInitialize:
    def test_initialize_url_available_and_nonexistent(self):
        url = 'http://www.jma.go.jp/en/gms/'
        data = setup(url, 'initialize')
        assert url in data['subscriptions']

    def test_initialize_url_unavailable(self):
        url = 'www.jma.go.jp/en/gms/'
        data = setup(url, 'initialize')
        assert url not in data['subscriptions']

    def test_initialize_url_existent(self):
        url = 'http://www.jma.go.jp/en/gms/'
        data = setup(url, 'initialize')
        assert url in data['subscriptions']


class TestUpdate():
    def test_update_url_available_and_nonexistent(self):
        url = 'http://www.jma.go.jp/en/gms/'
        data = setup(url, 'update')
        assert url in data['subscriptions']

    def test_update_url_unavailable(self):
        url = 'www.jma.go.jp/en/gms/'
        data = setup(url, 'update')
        assert url not in data['subscriptions']

    def test_update_url_existent(self):
        url = 'http://www.jma.go.jp/en/gms/'
        data = setup(url, 'update')
        assert url in data['subscriptions']

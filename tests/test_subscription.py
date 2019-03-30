# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
from subscription import Subscription
import settings
import utils


def setup_funcs(url, func_name):
    s = Subscription(url)
    if func_name == 'initialize':
        return s.initialize(settings.SUBSCRIPTIONS_FILE_FOR_TEST, ut=True)
    return s.update(settings.SUBSCRIPTIONS_FILE_FOR_TEST, ut=True)


def setup(url, func_name):
    utils.sketch_meta('subscriptions', settings.SUBSCRIPTIONS_FILE_FOR_TEST)
    if func_name == 'update':
        setup_funcs('https://en.wikipedia.org/', 'initialize')
    setup_funcs(url, func_name)
    return utils.load_db('subscriptions.json')


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


class TestUpdate:
    def test_update_url_available_and_nonexistent(self):
        url = 'http://www.jma.go.jp/en/gms/'
        data = setup(url, 'update')
        assert url not in data['subscriptions']

    def test_update_url_unavailable(self):
        url = 'www.jma.go.jp/en/gms/'
        data = setup(url, 'update')
        assert url not in data['subscriptions']

    def test_update_url_existent(self):
        url = 'https://en.wikipedia.org/'
        data = setup(url, 'update')
        assert url in data['subscriptions']

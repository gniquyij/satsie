# -*- coding: utf-8 -*-

import datetime
import json
import requests
import settings

class Subscription:

    def __init__(self, url):
        self.url = url

    def get(self, url):
        return requests.get(url).text

    def initialize(self):
        self.content = self.get(self.url)
        self.created_at = datetime.datetime.now()
        with open(settings.SUBSCRIPTIONS_FILE) as input:
            data = json.load(input)
        data['subscriptions'][self.url] = {
            'created_at': str(self.created_at),
            'content': self.content,
        }
        with open(settings.SUBSCRIPTIONS_FILE, 'w') as output:
            json.dump(data, output)
        print ('a new face => %s' % (self.url))

    def update(self):
        with open(settings.SUBSCRIPTIONS_FILE) as input:
            data = json.load(input)
        if self.url in data['subscriptions']:
            content_new = self.get(self.url)
            if content_new != data['subscriptions'][self.url]['content']:
                self.content = content_new
                self.updated_at = datetime.datetime.now()
                data['subscriptions'][self.url] = {
                    'content': self.content,
                    'updated_at': str(self.updated_at),
                }
                with open(settings.SUBSCRIPTIONS_FILE, 'w') as output:
                    json.dump(data, output)
                print ('CHANGES! => %s' % (self.url))
            else:
                print ('nothing changed => %s' % (self.url))
        else:
            self.initialize()

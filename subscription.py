# -*- coding: utf-8 -*-

import datetime
import json
import requests
import settings


class Subscription:
    def __init__(self, url):
        self.url = url

    def get(self, url, ut):
        try:
            return requests.get(url).text
        except Exception as e:
            if ut is False:
                print ('INVALID URL!')
                raise SystemExit

    def initialize(self, db=settings.SUBSCRIPTIONS_FILE, ut=False):
        self.content = self.get(self.url, ut)
        if self.content:
            self.created_at = datetime.datetime.now()
            with open(db) as input:
                data = json.load(input)
            data['subscriptions'][self.url] = {
                'created_at': str(self.created_at),
                'content': self.content,
            }
            with open(db, 'w') as output:
                json.dump(data, output)
            print ('a new face => %s' % (self.url))

    def update(self, db=settings.SUBSCRIPTIONS_FILE, ut=False):
        with open(db) as input:
            data = json.load(input)
        if self.url in data['subscriptions']:
            content_new = self.get(self.url, ut)
            if content_new:
                if content_new != data['subscriptions'][self.url]['content']:
                    self.content = content_new
                    self.updated_at = datetime.datetime.now()
                    data['subscriptions'][self.url] = {
                        'content': self.content,
                        'updated_at': str(self.updated_at),
                    }
                    with open(db, 'w') as output:
                        json.dump(data, output)
                    print ('CHANGES! => %s' % (self.url))
                else:
                    print ('nothing changed => %s' % (self.url))
            else:
                self.initialize()

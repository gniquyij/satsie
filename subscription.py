# -*- coding: utf-8 -*-

import datetime
import requests
import settings
import utils


class Subscription:
    def __init__(self, url):
        self.url = url

    def get(self, url, ut):
        try:
            return requests.get(url).text
        except:
            if not ut:
                print ('INVALID URL! => %s' % self.url)
                raise SystemExit

    def initialize(self, db=settings.SUBSCRIPTIONS_FILE, ut=False):
        data = utils.load_db(db)
        if self.url not in data['subscriptions']:
            self.content = self.get(self.url, ut)
            if self.content:
                self.created_at = datetime.datetime.now()
                data['subscriptions'][self.url] = {
                    'created_at': str(self.created_at),
                    'updated_at': None,
                    'content': self.content,
                }
                utils.dump_db(db, data)
                print ('a new face\'s in => %s' % self.url)
        else:
            print ('subscribed. checking for updates...')
            self.update()

    def update(self, db=settings.SUBSCRIPTIONS_FILE, ut=False):
        data = utils.load_db(db)
        if self.url in data['subscriptions']:
            content_new = self.get(self.url, ut)
            if content_new:
                if content_new != data['subscriptions'][self.url]['content']:
                    self.content = content_new
                    self.updated_at = datetime.datetime.now()
                    data['subscriptions'][self.url]['updated_at'] = str(self.updated_at)
                    data['subscriptions'][self.url]['content'] = self.content
                    utils.dump_db(db, data)
                    print ('CHANGES! => %s' % self.url)
                else:
                    print ('nothing changed => %s' % self.url)
        else:
            print ('a new face. new it if required.')

    def remove(self, db=settings.SUBSCRIPTIONS_FILE):
        data = utils.load_db(db)
        if self.url in data['subscriptions']:
            data['subscriptions'].pop(self.url)
            utils.dump_db(db, data)
            print ('removed => %s' % self.url)
        else:
            print ('nothing has been removed')

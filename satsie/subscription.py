# -*- coding: utf-8 -*-

import datetime
import requests
import settings
import utils
import logging


logger = logging.getLogger('satsie.subscription')


class Subscription:
    def __init__(self, url):
        self.url = url

    def get(self, url, ut):
        try:
            return requests.get(url).text
        except Exception as e:
            if not ut:
                logging.exception(e)
                print ('INVALID URL! => %s' % self.url)
                raise SystemExit

    def initialize(self, db=settings.SUBSCRIPTIONS_FILE, ut=False):
        try:
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
                    logger.info('subscribed => %s' % self.url)
                    print ('a new face\'s in => %s' % self.url)
            else:
                print ('subscribed. checking for updates...')
                self.update()
        except Exception as e:
            logging.exception(e)

    def update(self, db=settings.SUBSCRIPTIONS_FILE, ut=False):
        try:
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
                        logger.info('renewed => %s' % self.url)
                        print ('CHANGES! => %s' % self.url)
                    else:
                        print ('nothing changed => %s' % self.url)
            else:
                print ('a new face. new it if required.')
        except Exception as e:
            logging.exception(e)

    def remove(self, db=settings.SUBSCRIPTIONS_FILE):
        data = utils.load_db(db)
        if self.url in data['subscriptions']:
            data['subscriptions'].pop(self.url)
            utils.dump_db(db, data)
            logger.info('unsubscribed => %s' % self.url)
            print ('unsubscribed => %s' % self.url)
        else:
            print ('nothing has been removed.')

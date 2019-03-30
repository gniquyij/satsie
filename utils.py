# -*- coding: utf-8 -*-

import settings
import json
import subscription
import click


@click.group()
def cli():
    pass


def load_db(db):
    with open(db) as input:
        return json.load(input)


def dump_db(db, data):
    with open(db, 'w') as output:
        json.dump(data, output)


def sketch_meta(name, db=settings.SUBSCRIPTIONS_FILE):
    data = {}
    data[name] = {}
    dump_db(db, data)


@cli.command(help='sketch a json file for storing data')
def sketch():
    sketch_meta('subscriptions')


@cli.command(help='new a subscription')
@click.option('--url', help='the subscription to add')
def new(url):
    s = subscription.Subscription(url)
    s.initialize()


@cli.command(help='check if any updates on a specific subscription')
@click.option('--url', help='the subscription to check')
def arenew(url):
    s = subscription.Subscription(url)
    s.update()


@cli.command(help='check if any updates on all the subscriptions')
def renew(db=settings.SUBSCRIPTIONS_FILE):
    data = load_db(db)
    urls = data['subscriptions'].keys()
    for url in urls:
        s = subscription.Subscription(url)
        s.update()


if __name__ == '__main__':
    cli()

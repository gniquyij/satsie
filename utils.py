# -*- coding: utf-8 -*-

import settings
import json
import subscription
import click


@click.group()
def cli():
    pass


@cli.command(help='sketch a json file for storing data')
def sketch():
    data = {}
    data['subscriptions'] = {}
    with open(settings.SUBSCRIPTIONS_FILE, 'w') as output:
        json.dump(data, output)


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


if __name__ == '__main__':
    cli()

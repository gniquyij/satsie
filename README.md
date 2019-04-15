# satsie

## what is satsie

a tool to check for your subscription updates.

satsie is the pronunciation of '飒(sa) 尖(tsie)' in Shanghainese, which means sharp.

## how satsie works

compare the same source between different timestamps.

## why not other RSS tools in the market

- hard to find the RSS feeds (complicated to make one)
- too many useless features like recommendation...i just need someone to tell me if any updates on my subscriptions
- privacy

## how to use

### setup

```
$ git clone https://github.com/vjyq/satsie.git
$ cd satsie
$ pip install -r requirements.txt               # a virtualenv is recommended
$ cd satsie
$ python utils.py sketch
```

### enjoy

```
$ python utils.py new --url <subscription>      # to add a new subscription
$ python utils.py arenew --url <subscription>   # to check if any updates on a specific subscription
$ python utils.py renew                         # to check if any updates on all the subscriptions
$ python utils.py remove --url <subscription>   # to unsubscribe from a url
$ python utils.py dump                          # to dump the subscription brief
```

## TODO

- https://pypi.org/project/satsie/0.1.1/
- flag the subscriptions. e.g. type, author, etc.
- timestamp to utc

## author

<mailto:yuqing.ji@outlook.com>

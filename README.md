# sa tsie

## what is SA TSIE

a tool to manage your subscriptions.

SA TSIE is the pronounciation of "萨尖" in Shanghainese, which means sharp. Wish it sharp enough to figure out the change.

## why not other RSS tools in the market

- hard to find the RSS feeds (complicated to make one)
- too many useless features like recommendation...i just need someone to tell me if any updates on my subscriptions
- privacy

## how to use

### setup

```
$ pip install -r requirements.txt
$ python utils.py sketch
```

### enjoy

```
$ python utils.py new --url <subscription>   # to add a new subscription
$ python utils.py arenew --url <subscription>   # to check if any updates on a specific subsciption
```

## TODO

- unittest

## author

<mailto:yuqing.ji@outlook.com>
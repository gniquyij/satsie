# sa tsie

## what is SA TSIE

a tool to check for your subscription updates.

SA TSIE is the pronounciation of "飒尖" in Shanghainese, which means sharp.

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
$ python utils.py arenew --url <subscription>   # to check if any updates on a specific subscription
$ python utils.py renew   # to check if any updates on all the subscriptions
```

## TODO

- add unittest
- add log

## author

<mailto:yuqing.ji@outlook.com>

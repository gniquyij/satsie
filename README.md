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
$ pip install satsie            # a virtualenv is recommended
$ satsie sketch                 # generate a json file in your current directory for storing data
```

### enjoy

```
$ satsie

Usage: satsie [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  arenew  check if any updates on a specific subscription
  dump    dump the subscriptions and their info
  ls      list the subscriptions
  new     new a subscription
  remove  unsubscribe from a url
  renew   check if any updates on all the subscriptions
  search  keyword search
```

## TODO

- flag the subscriptions. e.g. type, author, etc.
- timestamp to utc

## author

<mailto:yuqing.ji@outlook.com>

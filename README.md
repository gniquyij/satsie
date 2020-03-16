# satsie

## What is satsie

A tool for checking for the subscription updates.

satsie is the pronunciation of '飒(sa) 尖(tsie)' in Shanghainese, which means sharp.

## How satsie works

Compare the same source between different timestamps.

## Why not other RSS tools in the market

- hard to find the RSS feeds (complicated to make one)
- too many useless features like recommendation...i just need someone to tell me if any updates on my subscriptions
- privacy

## How to use

### Setup

```
$ pip install satsie            # A virtualenv is recommended
$ satsie sketch                 # To generate a json file in your current directory for storing data
```

### Enjoy

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

## Author

<yuqing.ji@outlook.com>

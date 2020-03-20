#!/bin/bash
set -e
here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
 . $here/activate.sh

cd $here/../satsie
echo $(satsie renew) | mail -s "satsie weekly $(date +%F)" yuqing.ji@outlook.com

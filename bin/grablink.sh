cat "$1" |tr ' ' '\n'|grep goto\?|sed 's/^href="//;s/"//'

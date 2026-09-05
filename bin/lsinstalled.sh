p='Commandline: *apt install' ; zgrep -e "$p"  /var/log/apt/history.log*|sed 's/^.* install //'|tr ' ' '\n'|sort|uniq|sed '/^-/d'

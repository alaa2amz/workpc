cat uradk |sed -n '/^[^#]/p'|tr ' ' '\n'|sort|uniq -c|less

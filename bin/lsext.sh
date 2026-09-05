grep "^$1" /etc/mime.types |awk '{if(NF==1)next;$1="";print}'|sed  's/^[ \t]*//g'|tr ' ' '\n'|tr '\n' ','|sed 's/,$//'|tr ',' '\n'

#!/bin/bash
fortFile=$HOME/Documents/fort.log

b() { clear ; ls -F  $@ ; }

bb() { b -la $@ ; }

for com in rm cp mv
do
alias $com="$com -iv"
done

cx() { ls -d *.* | sed 's/.*\.//' | sort | uniq -c | sort -n ; }

#echo ok
#if ps -a|grep -qve sxhkd 
#then
#sxhkd&
#fi

{ f="`fortune -s`" ; echo "$f"  ; date ; echo ----------; } >> Documents/fort.log
echo "$f"
HISTFILESIZE=-1
fontconsole() { setfont Lat15-Terminus32x16 ; }
export PATH=$HOME/.local/BRL-CAD_7.42.0_Linux_x86_64/bin/:$PATH
export myrepo=https://github.com/alaa2amz


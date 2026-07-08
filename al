#!/bin/bash

case "$1" in
  Username*)
    echo "alaa2amz"
    exit
    ;;
  Password*)
    cat $HOME/ifrit
    exit
    ;;
esac


export GH_TOKEN=`cat $HOME/ifrit`
export GIT_ASKPASS=$HOME/al
fortFile=$HOME/Documents/fort.log
HISTFILESIZE=-1
fontconsole() { setfont Lat15-Terminus32x16 ; }
export PATH=$HOME/.local/BRL-CAD_7.42.0_Linux_x86_64/bin/:$PATH
export myrepo=https://github.com/alaa2amz

b() { clear ; ls -F  $@ ; }

bb() { b -la $@ ; }

for com in rm cp mv
do
alias $com="$com -iv"
done
alias t="tmux attach -x || tmux"

cx() { ls -d *.* | sed 's/.*\.//' | sort | uniq -c | sort -n ; }
cl() { { xsel ; echo ; echo ======= ; } |tee -a $HOME/clbo.log ; }

#echo ok
#if ps -a|grep -qve sxhkd 
#then
#sxhkd&
#fi
if false # tmux -V
then
	case $TERM in 
		tmux-*)
			;;
		*)
			tmux
			;;
	esac
fi

#if [ -z "$TMUX" ]; then
#	tmux attach || tmux
#fi


{ f="`fortune -s`" ; echo "$f"  ; date ; echo ----------; } >> $HOME/Documents/fort.log
echo "$f"


bind '"\ee":"alaa2amz@gmail.com"' 
bind -x '"\b":b'

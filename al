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

bind '"\ee":"alaa2amz@gmail.com"' 
bind -x '"\b":b'

export HISTFILESIZE=-1
export GH_TOKEN=`cat $HOME/ifrit`
export GIT_ASKPASS=$HOME/al
export fortFil=$HOME/Documents/fort.log
export PATH=$HOME/.local/BRL-CAD_7.42.0_Linux_x86_64/bin/:$PATH
export PATH=$HOME/.local/bin/:$PATH
export PATH=$HOME/.local/J/bin/:$PATH
export myrepo=https://github.com/alaa2amz

wd() { echo $PWD > /tmp/cwd ; }
rd() { cd $(cat /tmp/cwd) ; }
zoom() { setfont Lat15-Terminus32x16 ; }
b() { clear ; ls -F  $@ ; }
bb() { b -la $@ ; }
cx() { ls -d *.* | sed 's/.*\.//' | sort | uniq -c | sort -n ; }
cl() { {  echo ====`date`==== ; xsel ; echo ;echo ; } |tee -a $HOME/clbo.log ; }
fort() {
{ f="`fortune -s`" ; echo "$f"  ; date ; echo ----------;echo; } >> $HOME/Documents/fort.log
echo "$f" ; }
t() {
if   tmux -V
then
	case $TERM in 
		tmux-*)
			;;
		*)
			alias t="tmux attach -x || tmux"
			;;
	esac
fi ; }

for com in rm cp mv
do
alias $com="$com -iv"
done
alias xm="xmessage -geometry 350x150 -xrm 'xmessage*minWidth: 350' -xrm 'xmessage*minHeight: 150' -xrm 'xmessage*maxWidth: 350' -xrm 'xmessage*maxHeight: 150'"

fort

cat ../../yojijukugo\ -\ Google\ Search.html|tr ' ' '\n'|grep goto\?url |sed 's/href=//;s/"//g'|wget  -T5 -i- -nd -e robots=off -HENp

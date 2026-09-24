echo 5 > ~/rotime ;while : ;do sleep `cat ~/rotime` ;sed '/^[!]/d' /usr/share/X11/rgb.txt|shuf -n1|awk '{print $NF}'|tee -a ~/colog|xargs xsetroot -solid ;done

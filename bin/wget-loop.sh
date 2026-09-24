cat k.list |while read l ;do wget -p -k -E -H -e robots=off -nd -A jpg,jpeg,png,gif "$l";echo -e '\033[31m----- $a ---------------------------------------------------------\033[0m--';done


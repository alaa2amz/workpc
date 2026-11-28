find /usr/share -name \*.psf\*|awk -F- '{$1="";print}'|sort|less

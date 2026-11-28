bzcat  jawiktionary-20261101-pages-articles-multistream-index.txt.bz2 |awk -F':' '/twinkle/{off=$1;m=1;print $0}{if(m==1&&$1 + 0 >off){print $1;exit} }' 

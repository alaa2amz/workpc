bzcat jawiktionary-20261101-pages-articles-multistream-index.txt.bz2 |awk -F: '{print $1}' |uniq|awk '{print prev,$1 - prev ;prev=$1}'

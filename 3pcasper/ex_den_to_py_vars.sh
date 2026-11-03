awk '/^[ \t]*[^#]/{c=$1;d=$2;$1=$2="";gsub("[-(]","_");gsub(", ?","_");gsub("\\)","");gsub("\\.$","");gsub("[ ]+","_");sub("^_","");gsub("__+","_");print($0,"=",c," #",d)}' EXAMPLE_DENSITIES 

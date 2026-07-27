 node s.js > site.tcl;
 rm site.g;
 cat site.tcl |mged -c site.g #1>stdout.log 2>stderr.log&
# tail -f stderr.log
# mged site.g 

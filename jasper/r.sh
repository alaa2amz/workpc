rm -f ss.g; python3 s.py > ss.tcl;cat ss.tcl|mged -c ss.g;mged  ss.g

f=$a
rm -f $f.g
python3 skell.py > $f.tcl
cat $f.tcl|mged -c $f.g
mged  -c -aogl $f.g

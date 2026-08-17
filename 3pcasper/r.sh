main() {
f=a
rm -f $f.g
python3 skell.py > $f.tcl
check $?
#cat $f.tcl|mged -c $f.g
#mged -c $f.g source $f.tcl
#mged -c $f.g 'set glob_compat_mode 0;if {[catch {source a.tcl} err]} { puts stderr $err; exit 1 }'
mged -c "$f.g" <<EOF
set glob_compat_mode 0
if {[catch {source a.tcl} err]} {
    puts stderr "Error: \$err"
    # Force MGED to quit with an explicit status
    exit 1
}
EOF



check $?
mged  -c -aogl $f.g
}

check() {
	case $1 in
		0)echo ok;;
		*)echo $1 something wrong
			exit;;
	esac
}

main

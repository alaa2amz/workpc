main() {
	file_prefix=site
echo deleting $file_prefix old g file
rm -f $file_prefix.g
echo generating $file_prefix tcl script
python3 cas.py > $file_prefix.tcl
echo done
check $?
#cat $f.tcl|mged -c $f.g
#mged -c $f.g source $f.tcl
#mged -c $f.g 'set glob_compat_mode 0;if {[catch {source a.tcl} err]} { puts stderr $err; exit 1 }'
echo generating g file from tcl script
mged -c  "$file_prefix.g" <<EOF
set glob_compat_mode 0

#set fp [open "stderr_log.txt" w]


if {[catch {source $file_prefix.tcl} err]} {
    # Force MGED to quit with an explicit status
    exit 1
}
EOF

check $?

mged -x5 -X5  -c -aogl $file_prefix.g 
}

check() {
	case $1 in
		0)echo ok;;
		*)echo $1 something wrong
			exit;;
	esac
}

main

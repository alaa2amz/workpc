cat >/etc/udev/rules.d/70-pcspkr-beep.rules <<'QQ'
ACTION!="remove", SUBSYSTEM=="input", ATTRS{name}=="PC Speaker", ENV{DEVNAME}!="", TAG+="uaccess"
QQ

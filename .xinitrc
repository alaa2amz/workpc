#exec dwm
sxhkd&

export GTK_IM_MODULE=fcitx5
export QT_IM_MODULE=fcitx5
export XMODIFIERS=@im=fcitx5
export SDL_IM_MODULE=fcitx5
export INPUT_METHOD=fcitx5
pgrep -x fcitx5 > /dev/null || fcitx5 -d &


#if false
#then

# 2. Ensure a D-Bus session bus is running if not started by systemd/xinitrc.d
if [ -z "$DBUS_SESSION_BUS_ADDRESS" ]; then
    eval $(dbus-launch --sh-syntax --exit-with-session)
fi

# 3. CRITICAL: Tell D-Bus/Systemd where your display is
# This stops the "cannot open display" timeout crash.
dbus-update-activation-environment --systemd DISPLAY XAUTHORITY XDG_CURRENT_DESKTOP=dwm
systemctl --user import-environment DISPLAY XAUTHORITY XDG_CURRENT_DESKTOP

# 4. Optional: Force GTK applications to use the portal dialog
export GTK_USE_PORTAL=1
#fi




 while true; do  dwm 1>>$HOME/dwm.o 2>>$HOME/dwm.e;done


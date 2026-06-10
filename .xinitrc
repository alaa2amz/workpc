#exec dwm
sxhkd&

export GTK_IM_MODULE=fcitx5
export QT_IM_MODULE=fcitx5
export XMODIFIERS=@im=fcitx5
export SDL_IM_MODULE=fcitx5
export INPUT_METHOD=fcitx5
pgrep -x fcitx5 > /dev/null || fcitx5 -d &

while true; do dwm 1>>$HOME/dwm.o 2>>$HOME/dwm.e;done


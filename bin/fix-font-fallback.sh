mkdir -p ~/.config/fontconfig

cat > ~/.config/fontconfig/fonts.conf <<'QT'
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <alias>
    <family>sans-serif</family>
    <prefer>
      <family>Noto Sans</family>
    </prefer>
  </alias>
  <alias>
    <family>serif</family>
    <prefer>
      <family>Noto Serif</family>
    </prefer>
  </alias>
  <alias>
    <family>monospace</family>
    <prefer>
      <family>Noto Sans Mono</family>
    </prefer>
  </alias>
</fontconfig>
QT
fc-cache -f -v
fc-match -a sans-serif

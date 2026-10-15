sudo apt update
sudo apt install fonts-noto-cjk fonts-ipafont-gothic fonts-ipafont-mincho

mkdir -p ~/.config/fontconfig/conf.d/

cat >~/.config/fontconfig/conf.d/50-japanese-precedence.conf << 'QT'
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "urn:fontconfig:fonts.dtd">
<fontconfig>

    <!-- 1. Suggest 'ja' fallback whenever language is missing -->
    <match target="pattern">
        <edit name="lang" mode="append">
            <string>ja</string>
        </edit>
    </match>

    <!-- 2. Force Noto Sans CJK JP ahead of other CJK fallbacks for Sans-Serif -->
    <alias>
        <family>sans-serif</family>
        <prefer>
            <family>Noto Sans CJK JP</family>
            <family>IPAGothic</family>
        </prefer>
    </alias>

    <!-- 3. Force Noto Serif CJK JP ahead for Serif -->
    <alias>
        <family>serif</family>
        <prefer>
            <family>Noto Serif CJK JP</family>
            <family>IPAMincho</family>
        </prefer>
    </alias>

    <!-- 4. Force Noto Sans Mono CJK JP for Monospace -->
    <alias>
        <family>monospace</family>
        <prefer>
            <family>Noto Sans Mono CJK JP</family>
            <family>IPAGothic</family>
        </prefer>
    </alias>

</fontconfig>
QT

fc-cache -fv
fc-match sans-serif:lang=ja


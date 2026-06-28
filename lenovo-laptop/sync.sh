##repo=$HOME/workpc
dot_files="al  .bashrc  .spectrwm.conf .vimrc .xinitrc .config/sxhkd/ ale-map.vim .tmux.conf"
aptpath="/var/log/apt"

for file in $dot_files
do
	cp -vr $HOME/$file .
done

cp -rv $aptpath .

#cd $repo
git add $dot_files apt
git commit -am"`fortune -s`"
git pull
git push -u origin main


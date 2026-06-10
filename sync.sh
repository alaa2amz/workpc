repo=$HOME/workpc
dot_files="al  .bashrc  .spectrwm.conf .vimrc .xinitrc"
aptpath="/var/log/apt"

for file in $dot_files
do
	cp -v $HOME/$file $repo/
done

cp -rv $aptpath $repo/

cd $repo
git add $dot_files apt
git commit -am"`fortune -s`"
git pull
git push -u origin main


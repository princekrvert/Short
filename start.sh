#!/data/data/com.termux/files/usr/bin/bash
#make a banner first
banner (){
echo -e "\e[92m

 __ _                _   
/ _\ |__   ___  _ __| |_ 
\ \| '_ \ / _ \| '__| __|
_\ \ | | | (_) | |  | |_ 
\__/_| |_|\___/|_|   \__|\e[35m:::\e[37mmade by prince\e[0m
"
                                                      
}
#installing all requirments
apt update && apt upgrade
apt-get install python
apt-get install python2
pkg install python3
pkg install ruby
pip install pyshorteners
gem install lolcat
pkg install figlet
pkg install cowsay
chmod +x short.py
clear
banner
./short.py

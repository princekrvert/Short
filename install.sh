#!/data/data/com.termux/files/usr/bin/bash
#make a banner first
#Made by prince ...
#Date 28 march 2021
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
requirement (){
           
    apt update && apt upgrade
    apt-get install python
    apt-get install python2
    pkg install python3
    pkg install ruby
    pip install pyshorteners
    gem install lolcat
    pkg install figlet
    pkg install cowsay
 }
requirement

chmod +x short.py
clear
#Make a function to move the program
move(){
	cat short.py >> short
	chmod +x short
	mv short /data/data/com.termux/files/usr/bin

}
move
banner
echo " "
echo -e "\e[35;1m Type 'short url' to shorten the url"

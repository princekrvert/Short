#!/data/data/com.termux/files/usr/bin/python3
#import goes here
import pyshorteners
#take a input

link = input("\033[31mEnter a url : ")
p= pyshorteners.Shortener()
short_url=p.tinyurl.short(link)
print("\033[36m Your short url is :")
print("\033[95m " ,short_url)
                                  

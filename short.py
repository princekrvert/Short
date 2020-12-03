#!/data/data/com.termux/files/usr/bin/python3
#Author prince kumar
#date  3 dec 2020
#start


#import goes here
import pyshorteners
#take a input
												
link = input("\033[31mEnter a url : ")
try:
	p= pyshorteners.Shortener()
	short_url=p.tinyurl.short(link)
	print("\033[36m Your short url is :")
	print()
	print("\033[95m " ,short_url)

except:
	print("\033[33mSlow internet connection")
                           

#!/usr/bin/python3
#Author prince kumar
# Modification date14 oct 2021
#import goes here
import pyshorteners
import argparse
import json 
import requests
import time
import os
import sys
#take a input
#make a function to update the repo---
# make a banne function 
def banner():
    print("\033[33;1m")
    print('░s░h░o░r░t░', end=" ")
    print("\033[32;1m MADE BY PRINCE")
def repoUpdate():
    if sys.platform == "linux":
        os.system("git pull https://github.com/princekrvert/Short.git > /dev/null 2>&1 & sleep .05 ")
        print("Updating ...") 
        os.system("clear")
        banner()
    else:
        os.system("cls")
        banner()


#Let's define a main function----
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Enter a url : " )
    args = parser.parse_args()
    link = args.url
    try:
        p= pyshorteners.Shortener()
        short_url=p.tinyurl.short(link)
        print()
        print("\033[36;1m Your short url is :", end=" ")
        print("\033[95;1m " ,short_url)
        print()
        res = requests.get(f"https://is.gd/create.php?format=json&url={link}")
        print("\033[36;1m Your short url is : ", end=" ")
        short_link = res.json().get("shorturl")
        print("\033[95;1m", short_link)
        req = requests.post("https://hideuri.com/api/v1/shorten",data = {'url' : link} )
        short_link = req.json().get("result_url")
        print()
        print("\033[36;1m Your short url is : ", end=" ")
        print("\033[95;1m", short_link)
    except KeyboardInterrupt:
        print("\033[36;1m Exiting--->>>>")
        time.sleep(2)
        sys.exit(1)
    except:
        print("\033[31;1mSlow internet connection ....")

if __name__ == "__main__":
    repoUpdate()
    main()

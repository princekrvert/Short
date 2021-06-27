#!/data/data/com.termux/files/usr/bin/python3
#Author prince kumar
# Modification date 28 mar 2021
#start


#import goes here
import pyshorteners
import argparse
import time
import os
import sys
#take a input
#make a function to update the repo---
def repoUpdate():
    os.system("git pull https://github.com/princekrvert/Short.git > /dev/null 2>&1 & sleep .05 ")
    print("Updating ...") 
    os.system("clear")


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
    except KeyboardInterrupt:
        print("\033[36;1m Exiting--->>>>")
        time.sleep(2)
        sys.exit(1)
    except:
        print("\033[31;1mSlow internet connection ....")

if __name__ == "__main__":
    repoUpdate()
    main()

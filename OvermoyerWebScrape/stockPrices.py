import urllib
import os

def readWebPage(ticker):
        #finds the proper web page with the given ticker
        url="http://finance.yahoo.com/q?s=" + str(ticker) + "&ql=1"
        rawHtml=getContents(url)
        rawHtml=rawHtml[25000:37000]
        indicator="yfs_l84"
        tickerindex=rawHtml.find(indicator)
        tickerString=rawHtml[tickerindex+8:tickerindex+30]
        ticker=""
        for char in tickerString:
                if char.isdigit():
                        ticker+=str(char)
                elif char==("."):
                        ticker+=str(char)
        print ticker
        return ticker

def getContents(url):
        #getContents function returns the html code for given url
        assert(url.startswith("http://"))
        fin = contents = None
        try:
                fin = urllib.urlopen(url)
                contents = fin.read()
        finally:
                if (fin != None): fin.close()
        return contents

def takeTicker(): #main
        ticker=raw_input("Enter the stock ticker: ")
        readWebPage(ticker)

takeTicker()

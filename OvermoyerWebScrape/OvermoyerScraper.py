import urllib
import os

def readWebPageNews(page):
        url="http://www.k2bike.com/index.php?page=" + str(page)
        rawHtml=getContents(url)
        newsTag="Latest News"
        newsIndex=rawHtml.find(newsTag)
        rawHtml=rawHtml[newsIndex:]
        mutableHtml=rawHtml
        startTagOne="<h4>"
        startTagTwo="<div>"
        endTagOne="</h4>"
        endTagTwo="</div>"
        headings=""
        while mutableHtml.find(startTagOne)!=-1:
            startIndexOne=mutableHtml.find(startTagOne)
            startIndexTwo=mutableHtml.find(startTagTwo)
            startIndex=min(startIndexOne,startIndexTwo)
            if(startIndexOne<startIndexTwo):
                    mutableHtml=mutableHtml[startIndex+len(startTagOne):]
                    endIndex=mutableHtml.find(endTagOne)
                    headings+=mutableHtml[:endIndex]
                    headings+="\n"
                    mutableHtml=mutableHtml[endIndex+len(endTagOne):]
            else:
                    mutableHtml=mutableHtml[startIndex+len(startTagTwo):]
                    endIndex=mutableHtml.find(endTagTwo)
                    headings+=mutableHtml[:endIndex]
                    headings+="\n"
                    mutableHtml=mutableHtml[endIndex+len(endTagTwo):]
        tagStart="<"
        tagEnd=">"
        '''while headings.find(tagStart)!=-1:
                tagStartIndex=headings.find(tagStart)
                tagEndIndex=headings.find(tagEnd)
                headings=headings[:tagStartIndex] + headings[tagEndIndex:]'''
        headings="News "+headings
        return headings

def readWebPageProducts(page):
        url="http://www.k2bike.com/index.php?page=" + str(page)
        rawHtml=getContents(url)
        startTag="bike_cat&cat_id"
        products=""
        endTag="<"
        while rawHtml.find(startTag)!=-1:
                startIndex=rawHtml.find(startTag)
                rawHtml=rawHtml[startIndex+len(startTag)+4:]
                endIndex=rawHtml.find(endTag)
                products+=rawHtml[:endIndex]
                products+=" "
                rawHtml=rawHtml[endIndex:]
        products="Products" + products
        return products


def readWebPageNews2(page):
        url="http://www.dorel.com/eng/" + str(page)
        html=getContents(url)
        newsTag="newsList"
        newsIndex=html.find(newsTag)
        html=html[newsIndex:]
        pressReleases=5
        startTag="title="
        endTag=">"
        startTagTwo="newsLeadin"
        endTagTwo="<"
        headings=""
        while pressReleases>=0:
            startIndex=html.find(startTag)
            html=html[startIndex+len(startTag):]
            endIndex=html.find(endTag)
            headings+=html[:endIndex-len(endTag)]
            startIndexTwo=html.find(startTagTwo)
            html=html[startIndexTwo+len(startTagTwo):]
            endIndexTwo=html.find(endTagTwo)
            headings+=html[:endIndexTwo-len(endTagTwo)]
            html=html[endIndexTwo:]
            pressReleases-=1
        headings="News " + headings
        return headings

def readWebPageProducts2():
        url="http://www.dorel.com/eng/cannondale"
        productTag="redpart"
        html=getContents(url)
        productIndex=html.find(productTag)
        html=html[productIndex:]
        startTag="<p>"
        endTag="</p>"
        products=""
        startIndex=html.find(startTag)
        endIndex=html.find(endTag)
        products+=html[startIndex+len(startTag):endIndex]
        url2="http://www.dorel.com/eng/schwinn"
        html2=getContents(url2)
        productIndex=html2.find(productTag)
        html2=html2[productIndex:]
        startIndex=html2.find(startTag)
        endIndex=html2.find(endTag)
        products+=html2[startIndex+len(startTag):endIndex]
        products="Products " + products
        return products
                
def readWebPageMission2(page):
    url="http://www.dorel.com/eng/" + str(page)
    html=getContents(url)
    startTag="<p>"
    endTag="</p>"
    mission=""
    startIndex=html.find(startTag)
    endIndex=html.find(endTag)
    mission+=html[startIndex+len(startTag):endIndex]
    Mission="Mission " + mission
    return mission

def readWebPageNews3():
        url="http://bike.shimano.com/publish/content/global_cycle/en/us/index/news_and_info/news.html"
        html=getContents(url)
        newsTag="newsBar"
        newsIndex=html.find(newsTag)
        html=html[newsIndex:]
        pressReleases=5
        startTag="/>"
        endTag="</div>"
        startTagTwo='"newsIntro">'
        endTagTwo="<"
        headings=""
        while pressReleases>=0:
            startIndex=html.find(startTag)
            html=html[startIndex+len(startTag):]
            endIndex=html.find(endTag)
            headings+=html[:endIndex-len(endTag)]
            startIndexTwo=html.find(startTagTwo)
            html=html[startIndexTwo+len(startTagTwo):]
            endIndexTwo=html.find(endTagTwo)
            headings+=html[:endIndexTwo-len(endTagTwo)]
            html=html[endIndexTwo:]
            pressReleases-=1
        headings="News " + headings
        return headings

def readWebPageProducts3():
        products="""Products Dura Ace, Ultegra, 105, Tiagra, Sora, 2300, XTR, SAINT,
        ZEE, Decore XT, SLX, Deore, Alivio 9-Speed, DXR"""
        return products
                
def readWebPageMission3():
        url="http://bike.shimano.com/publish/content/global_cycle/en/us/index/news_and_info/about_us.html"
        html=getContents(url)
        startTag='<div class="text">'
        endTag="<br><br><br>"
        mission=""
        startIndex=html.find(startTag)
        endIndex=html.find(endTag)
        mission+=html[startIndex+len(startTag):endIndex]
        mission="Mission " + mission
        return mission

                

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

def readStockPage(ticker):
        #finds the proper web page with the given ticker
        url="http://finance.yahoo.com/q?s=" + str(ticker)
        rawHtml=getContents(url)
        indicator="yfs_l84"
        tickerindex=rawHtml.find(indicator)
        tickerString=rawHtml[tickerindex+8:tickerindex+30]
        ticker=""
        for char in tickerString:
                if char.isdigit():
                        ticker+=str(char)
                elif char==(".") and len(ticker)>0:
                        ticker+=str(char)
        return ticker


def getInfo(): #main
        company="Name K2bikes"
        stock="Stock " + readStockPage("JAH")
        stock2="Stock " + readStockPage("DII-A.TO")
        stock3="Stock " + readStockPage("SHMDF")
        missionStatement="Mission No matter who you are, no matter where you ride, there's a k2 built just for you."
        news=readWebPageNews("news")
        products=readWebPageProducts("bike_landing")
        company2="Name Dorel"
        missionStatement2=readWebPageMission2("corporate-profile")
        news2=readWebPageNews2("press-releases")
        products2=readWebPageProducts2()
        company3="Name Shimano"
        missionStatement3=readWebPageMission3()
        news3=readWebPageNews3()
        products3=readWebPageProducts3()
        compiled=(company + stock + missionStatement + news + products + "end"
        + company2 + stock2 + missionStatement2 + news2 + products2 + "end" +
        company3 + stock3 + missionStatement3 + news3 + products3 + "end")
        textFile=open("output.txt", "w")
        textFile.write(compiled)

getInfo()

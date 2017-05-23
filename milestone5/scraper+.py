import sys
import requests
from lxml import etree
from io import StringIO, BytesIO

def main(): 
    ''' Displays the main menu for the program and makes sure the correct amount of arguments are present'''
    args = sys.argv[1:]
    if len(args) == 2:
        print(scrapeKeys(args[0].lower(), args[1].lower()))
    elif len(args) == 3 and args[2] == "pubmed":
        print(runPubMed(args[0].lower(), args[1].lower(), '+synthetic+biology'))
    else:
        print ("Something went wrong with your input. Please type your query in the form \"scraper.py firstName lastName\"")
        print("If you'd like to search PubMed, type \"pubmed\" as a third argument")

def scrapeKeys(personFirst, personLast):
    '''Performs the main functions of the program - scraping the top results on google for keywords'''
    url = 'https://www.google.com/search?q='
    url += personFirst
    url += '+'
    url += personLast
    url += '+synthetic+biology'
    try:
        r = requests.get(url, timeout=5) #Connect to internet to google search input name
    except:
        return "Looks like your internet is not working. Reconnect and try again"
    
    root = etree.HTML(r.text)
    #for node in root.xpath('//div[@class="g"]//span[@class="st"]//text()'):
    #    print(node) #Looking for div class="g" and a span class under that "st". Using // since that means any class below.
    a = []
    #Also using the web developer tool and disabling javascript for rational scraping                                                                          
#------------------------------------------------For printing urls and pieces of urls-----------------------------------------
    for node in root.xpath('//div[@class="g"]//div[@class="kv"]//text()'):
        a.append(node) #Looking for div class="g" and a span class under that "kv". Using // since that means any class below.
       # print(node)
    urls = concatenateURLs(a)
    print(urls)
#---------------------------------------------Create mega string for keywords-------------------------------------------------
    raw_html = ""
    for url in urls:
        raw_html += tryUrl(url)
    return keywordExtract(raw_html)
#
#
#
#Functions are below

def concatenateURLs(urlPieces):
    '''Takes individual parts of the URL returned by requests and puts them together into correct URLs'''
    print(urlPieces)
    nodeIndex = 0
    urls = []
    header = False
    url = ""
    for piece in urlPieces:
        if piece == "Similar":
            pass
        elif (piece[:4] == "http" or piece[:4] == "www."):
            print(url)
            urls.append(url)
            url = piece
            header = False
        elif piece != "Cached" :
            url += piece
        else:
            urls.append(url)
            url = ""
            header = False
    return urls
def tryUrl(url): 
    '''Tries to download the text from a URL using request and does preliminary formatting on the text'''
    try:
        h = requests.get(url, timeout=5)
        b = h.text.lower()
        if url[-4:] == ".pdf":
            return " "
        return b
    except:
        if url[:4] != "http":
            try:
                tempVar = url
                url = "http://"
                url += tempVar
                h = requests.get(url, timeout=5)
                b = h.text.lower()
                return b
            except:
                return " "
        
        return " "
def keywordExtract(html):
    '''Takes a large text file and mines it for keywords that are non-html commands for the most part'''
    c=0
    keywordArray = set([])
    while c !=-1:
        
        c = html.find(" ")
        if c != -1:
            if len(html[:c]) < 15  and not('<'  in html[:c]) and not('>'  in html[:c]) and not('"'  in html[:c]) and not('='  in html[:c]) and not('_'  in html[:c]) and (len(html[:c]) != 0) and not('{'  in html[:c]) and not('}'  in html[:c]) and not( '\\'  in html[:c]) and not(')'  in html[:c]) and not('+' in html[:c]) and not('(' in html[:c]) and not('/' in html[:c]) and not('&' in html[:c]) and not('www.' in html[:c]) and not('\n' in html[:c]) and not('\xa0' in html[:c]) and not('|' in html[:c] and not(str(chr(1)) in html[:c]) and not ('1' in html[:c]) and not('2' in html[:c]) and not('3' in html[:c]) and not('4' in html[:c]) and not('5' in html[:c]) and not('6' in html[:c]) and not('7' in html[:c]) and not('8' in html[:c]) and not('9' in html[:c]) and not('0' in html[:c])): #check for a bunch of common features of formatting and make sure not to include in keyword array 
                keywordArray.add(html[:c])
            tempStr = html[c+1:len(html)]
            html = tempStr
        else:
            if len(html) < 15:
                keywordArray.add(html)
    return(keywordArray)
def runPubMed(firstName, lastName, syntheticBiology):
    '''Searches a person's first and last name on PubMed and generates keywords'''
    url = "https://www.ncbi.nlm.nih.gov/pubmed/?term="
    url += firstName
    url += "+"
    url += lastName
    url += syntheticBiology
    try:
        r = requests.get(url, timeout=5) #Connect to internet to search input name on PubMed                                                                                                      
    except:
        return "Looks like your internet is not working. Reconnect and try again"
    a = []
    keywordArray = set([])
    noResults = True
    root = etree.HTML(r.content)
    for node in root.xpath('//p[@class="title"]'):
        noResults = False
        a.append(node.getchildren()[0].attrib.get('href'))
        extractAbstractText(node.getchildren()[0].attrib.get('href'), keywordArray)
    if noResults:
        for node in root.xpath('//div[@class="abstr"]//div[@class=""]//text()'):
            c = node.find(" ")
            while c != -1:
                c = node.find(" ")
                if '-' in node[:c]:
                    keywordArray.add(node[:node[:c].find('-')])
                    tempStr = node[node[:c].find('-')+1:len(node)]
                else:
                    keywordArray.add(node[:c])
                    tempStr = node[c+1:len(node)]
                node = tempStr
    if not len(keywordArray) and url[-4:] == "logy":
        keywordArray = runPubMed(firstName, lastName, '')
    return(keywordArray)
def extractAbstractText(link, keywordArray):
    '''Parses out the text from scientific abstracts from PubMed'''
    url = "https://www.ncbi.nlm.nih.gov"
    url += link
    r = requests.get(url, timeout=5)
    root = etree.HTML(r.content)
    for node in root.xpath('//div[@class="abstr"]//div[@class=""]//text()'):
        c = node.find(" ")
        while c != -1:
            c = node.find(" ")
            keywordArray.add(node[:c])
            tempStr = node[c+1:len(node)]
            node = tempStr
if __name__ == '__main__': main()

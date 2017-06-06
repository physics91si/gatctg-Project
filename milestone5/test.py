from ttp import ttp
import requests
from lxml import etree
p = ttp.Parser()
url = 'https://twitter.com/realDonaldTrump/status/866749195297976320'
try:
    r = requests.get(url, timeout=5) #Connect to internet
    root = etree.HTML(r.content)
    #for node in root.xpath('//div[@class="js-tweet-text-container"]//text()'):
        #print (node)
        #print("space")
    x = root.xpath('//div[@class="js-tweet-text-container"]//text()')
    print(x)
except:
    print("Looks like your internet is not working. Reconnect and try again")

#result = p.parse(x)
#print(result.reply)
#'burnettedmond'
#print(result.users)
#['burnettedmond']
#print(result.tags)
#['IvoWertzel']
#print(result.urls)
#['https://github.com/burnettedmond/']
#print(result.html)
#u'<a href="http://twitter.com/burnettedmond">@burnettedmond</a>, you now support <a href="https://twitter.com/search?q=%23IvoWertzel">#IvoWertzel</a>\'s tweet parser! <a href="https://github.com/edburnett/">https://github.com/edburnett/</a>'

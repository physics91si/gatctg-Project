import base64
import json
import requests
import pexpect

from base64 import b64encode

client_id = 'my-client-id'

headers = {"Authorization": "Client-ID 4932fef990cd708"}

api_key = '7cf6f638060e1fd300e7f318fcfc4a5e3381206a'

url = "http://api.imgur.com/3/upload.json"

j1 = requests.post(
    url, 
    headers = headers,
    data = {
        'key': api_key, 
        'image': b64encode(open('meme49.jpg', 'rb').read()),
        'type': 'base64',
        'name': 'meme42.jpg',
        'title': 'Picture no. 1'
    }
)
data = json.loads(j1.text)['data']
print (data['link'])
with open('.//template/site.region', 'r') as target_file:
    webhtml = target_file.read()
web1html = webhtml[:webhtml.find("src=")]
web2html = webhtml[webhtml.find("\" ALT"):]
newWebHtml = web1html + "src=\"" +  data['link'] + web2html
print (newWebHtml)
with open('.//template/site.region', 'w') as new:
  new.write(newWebHtml)
pexpect.run('cd template')
pexpect.run('git remote add origin git@github.com:aleclourenco@gmail.com/https://alec-lourenco-srmh.squarespace.com/template.git')
pexpect.run('git add .')
pexpect.run('git commit -m \"This is within pexpect\"')
print(pexpect.run('git push'))

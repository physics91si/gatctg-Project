import pysftp

srv = pysftp.Connection(host="dev.squarespace.com", username="aleclourenco@gmail.com", password="T4Coliphage",log="./temp/pysftp.log")

with srv.cd('public'): #chdir to public
    srv.put('C:\Users\XXX\Dropbox\test.txt') #upload file to nodejs/

# Closes the connection
srv.close()

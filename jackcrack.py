from urlparse import urlparse
from threading import Thread
import httplib, sys
from Queue import Queue
import urllib2
import json

f = open('output.txt','w')
concurrent = 1500

def bruteForce():
    while True:
        url = q.get()
        status, url = getStatus(url)
        printResults(status, url)
        q.task_done()

def getStatus(ourl):

    # Try catch for 404
    try:

        # TRY TO OPEN JSON OBJECTS
        response = urllib2.urlopen(ourl)
        print response 
        data = json.loads(response.read())
        print 'found a room: ', data
        return status, ourl
    except:
        return 'error', ourl
    
def printResults(status, url):
    print>>f, status, url
    

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=bruteForce)
    t.daemon = True
    t.start()
try:
    for url in open('jackbox.txt'):
        q.put(url.strip())
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
print "scan complete"

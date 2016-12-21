import requests
import json
from HTMLParser import HTMLParser
import os
import time

foundSearchString = False
needleNode = "h1"
needleCompare = "Hello World!"
needle = ""

# parse out what's in the source code
class TestDocParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global foundSearchString
        global needleNode
        global needle
    
        if tag.lower().strip() == needleNode:
            foundSearchString = True
        else:
            foundSearchString = False
    def handle_data(self, data):
        global foundSearchString
        global needleNode
        global needle
        
        if foundSearchString:
            foundSearchString = False
            needle = data


########################################
# get sandbox details
########################################
sandboxID = os.environ["SANDBOX_ID"]
testURL = "http://10.0.46.96/index.html"

time.sleep(180)

########################################
# begin test
########################################
tr = requests.get(testURL)
testHTML = tr.text

parser = TestDocParser()
parser.feed(testHTML)

########################################
# do pass fail
########################################
# compare value we got back
if (needle.strip() == needleCompare.strip()):
    # identical
    print "PASS! Expected '" + needleCompare.strip() +"' and got '"+needle.strip()+"'"
    pass
elif (len(needle.strip()) == 0):
    # couldnt find node
    print "FAIL! Expected '" + needleCompare.strip() +"' and could not locate node '"+needleNode+"'"
    exit(1)
else:
    # not identical
    print "FAIL! Expected '" + needleCompare.strip() +"' and got '"+needle.strip()+"'"
    exit(2)
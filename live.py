# -*- coding: utf-8 -*-
import urllib2
import re
import json
import time
import codecs
import sys

class BangumiUser:

    def __init__(self):
        self.id = -1
        self.name = "name"
        self.timeline = []
        self.lastTime = ""

if __name__ == '__main__':
    Id = 0
    userName = ''
    # timeline
    for Id in range(int(sys.argv[1]),int(sys.argv[2])):
        print 'now id is ' + str(Id)
        bgmuser = BangumiUser()
        bgmuser.id = Id
        url = "http://bangumi.tv/user/" + str(Id) + "/timeline"
        
        time.sleep(0.5)

        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        content = response.read()
        # print content.decode("utf-8").encode("UTF-8")

        pattern = re.compile('<div id="timeline">(.*?)<div id="tmlPager">', re.S)
        items = re.findall(pattern, content)

        if len(items) == 0:
            bgmuser.lastTime = 'null'
        else:
            timelinePattern = re.compile('<h4 class="Header">(.*?)</ul>',re.S)
            timelineItmes = re.findall(timelinePattern,items[0])
            bgmuser.timeline = timelineItmes

            count = 0
            for item in timelineItmes:
                # print count
                timelineContent = str(item).decode("utf-8").encode("UTF-8")
                count +=1
                lastTime = ""
                i = 0
                while True:
                    if timelineContent[i] == '<':
                        break
                    else:
                        lastTime += timelineContent[i]
                    i += 1
                # print lastTime
                bgmuser.lastTime = lastTime
        
        userFile = codecs.open('../BangumiCrawler/user/' + str(Id) + '.json', 'w', 'utf-8')
        json.dump(bgmuser.__dict__,userFile)

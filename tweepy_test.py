# -*- coding: utf-8 -*- 
import sys
import io
import tweepy
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
import re
import threading
import codecs
 


"""
auth = tweepy.OAuthHandler('NbKpIaXwEihI0QRCxSF776gED','VqU3dVQfT6B06IFfjk7bfW0NdmqrBm43nCOtbWLBWt9molPUfI')
auth.set_access_token('566173242-FZ71YKx31e8ThMt0QCYR9O58RSg7ym3Xhdj8iHsy','jrjLWJYzIktyHzIE5jXRdOzynwMtSu4eUJIFP8rJmeShx')
api = tweepy.API(auth)
public_tweets = api.home_timeline()
month = {
	'Feb':'02','Jan':'01','Mar':'03','Apr':'04','May':'05','Jun':'06',
	'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'
}
"""

id_dic = []
f = codecs.open('Trump.txt','a','utf-8')
threadLock = threading.Lock()

class myThread (threading.Thread):   
    def __init__(self, name, auth_key,auth_value,access_key,access_value):
        threading.Thread.__init__(self)
        self.name = name
        self.auth_key = auth_key
        self.auth_value = auth_value
        self.access_key = access_key
        self.access_value = access_value
    def run(self):                   
        print("Starting " + self.name)
        auth = tweepy.OAuthHandler(self.auth_key,self.auth_value)
        auth.set_access_token(self.access_key,self.access_value)
        api = tweepy.API(auth)
        twitter_stream = Stream(auth, MyListener())
        twitter_stream.filter(track=['#Trump'])        
        print("Exiting " + self.name)


class MyListener(StreamListener):
    def on_status(self, status):
        try:
            date = status.created_at
            retweeted=status.retweeted
            text = " ".join(status.text.split())
            id_str = status.id_str
            place = status.place
            source = status.source
            friends = status.user.friends_count
            #threadLock.acquire()
            #if id_str not in id_dic:
                #id_dic.append(id_str)
            f.write('\t'.join([str(date),text,id_str,str(place),str(retweeted),source,str(friends)])+'\n')
            #print(len(id_dic))
            #threadLock.release()

            return True
        except BaseException as e:
            print("&quot;Error on_data: %s&quot; "% str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True




if __name__ == "__main__":
    thread1 = myThread('thread1','NbKpIaXwEihI0QRCxSF776gED','VqU3dVQfT6B06IFfjk7bfW0NdmqrBm43nCOtbWLBWt9molPUfI','566173242-FZ71YKx31e8ThMt0QCYR9O58RSg7ym3Xhdj8iHsy','jrjLWJYzIktyHzIE5jXRdOzynwMtSu4eUJIFP8rJmeShx')
    #thread2 = myThread('thread2','CzFWcisQLvGLZWqlurX7fWOsU','zSNilKFFjYr7o71ZJbvdYxf9ghbpkAMPIDVcf1kxT7XHRZTPQm','566173242-kIilDFOaYOlDdbmWk2VSRLtfKy75ZTXcSdZF2DEZ','iMMukZlERjILt3EUiZj5QxgtuwhD5AzA9jWiyVIVdvibQ')
    thread1.start()
    #thread2.start()













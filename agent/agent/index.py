#!/usr/bin/env python

import urllib
import httplib
import httplib2
import time
import json




def submit_data(host,port,source,params,timeout):
    #headers={"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
    headers={"Content-type":"application/x-www-form-urlencoded","Accept":"text/html"}
    try:
#        conn = httplib2.HTTPConnectionWithTimeout(host,port,timeout)
        conn = httplib.HTTPConnection(host,port,timeout)
        conn.request('POST',source,params,headers)
        response = conn.getresponse()
        original = response.read()
        print(original)
    except Exception as e:
        raise(e) 
    return original


server_info={"aa":1, "bb":2}


if __name__=='__main__':
    times = 0
    while True:
#        RequestData = {'data':server_info}
#        RequestData = RequestData.encode(encoding='utf-8')
#        RequestData = json.dumps(RequestData)
#        RequestData = urllib.parse.urlencode({'data':server_info})
        RequestData = urllib.urlencode({'data':server_info})
        print("ttt:" + RequestData)
        result = submit_data('127.0.0.1', '9500', '/api/receive_server_info/', RequestData, 30)
        print('=======The %d request, result is %s' %(times,result))
        times+=1
        time.sleep(3)
    
#!/usr/bin/env python
# coding: UTF-8 

import ansible.runner
import urllib
import httplib
import httplib2
import time
import json


def get_data():
    runner = ansible.runner.Runner(module_name='setup', module_args='', pattern='all', forks=2)
    datastructure = runner.run()
    return datastructure

def get_info(datastructure, ip):
    data = {}
    hostname = datastructure['contacted'][ip]['ansible_facts']['ansible_hostname']
    ip = datastructure['contacted'][ip]['ansible_facts']['ansible_all_ipv4_addresses'][0]
    cpu = datastructure['contacted'][ip]['ansible_facts']['ansible_processor_vcpus']
    memory = datastructure['contacted'][ip]['ansible_facts']['ansible_memtotal_mb']
    disk = datastructure['contacted'][ip]['ansible_facts']['ansible_devices']['sda']['size']
    # print sysinfo
    data['hostname'] = hostname
    data['ip'] = ip
    data['cpu'] = cpu
    data['memory'] = memory
    data['disk'] = disk
    return data

def submit_data(host,port,source,params,timeout):
    #headers={"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
    headers={"Content-type":"application/x-www-form-urlencoded","Accept":"text/html"}
    try:
        conn = httplib.HTTPConnection(host,port,timeout)
        conn.request('POST',source,params,headers)
        response = conn.getresponse()
        original = response.read()
        print(original)
    except Exception as e:
        raise e
    return original



if __name__ == '__main__':
    datastructure = get_data()
    data = get_info(datastructure, '192.168.10.129')

    times = 0
    while True:
#        RequestData = {'data':server_info}
#        RequestData = RequestData.encode(encoding='utf-8')
        datastructure = get_data()
        data = get_info(datastructure, '192.168.10.129')
        RequestData = json.dumps(data)
        RequestData = urllib.urlencode({'data':RequestData})
        result = submit_data('127.0.0.1', '8500', '/CMDB/receive_server_info/', RequestData, 30)
        print('=======The %d request, result is %s' %(times,result))
        times+=1
        time.sleep(5)


#    print(data)
#    get_info('192.168.10.129')
#    import pprint
#    pprint.pprint(data)



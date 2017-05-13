#!/usr/bin/env python
# coding: UTF-8 

import ansible.runner

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


if __name__ == '__main__':
    datastructure = get_data()
    data = get_info(datastructure, '192.168.10.135')
    print(data)
#    get_info('192.168.10.129')
#    import pprint
#    pprint.pprint(data)



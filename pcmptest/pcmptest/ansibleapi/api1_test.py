#!/usr/bin/env python
# coding: UTF-8 

import ansible.runner


runner = ansible.runner.Runner(module_name='setup', module_args='', pattern='all', forks=2)
datastructure = runner.run()
hostname = datastructure['contacted']['192.168.10.129']['ansible_facts']['ansible_hostname']
print(hostname)


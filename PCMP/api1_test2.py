#!/usr/bin/env python
# coding: UTF-8 

import ansible.runner
import urllib
import httplib
import httplib2
import time
import json


def get_data():
    runner = ansible.runner.Runner(module_name='setup', module_args='', pattern='awshosts', forks=2)
    datastructure = runner.run()
    return datastructure




if __name__ == '__main__':
    data = get_data()
    print(data)



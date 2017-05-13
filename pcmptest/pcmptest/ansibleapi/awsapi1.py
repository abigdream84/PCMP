#!/usr/bin/env python

import ansible.runner

def get_data():
    runner = ansible.runner.Runner(module_name='setup', module_args='', pattern='all', forks=2)
    datastructure = runner.run()
    return datastructure




if __name__ == '__main__':
    data = get_data()
    print(data)

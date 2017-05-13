#!/usr/bin/env python
#conding:utf-8 
import argparse
import sys
import json
#import sql
import sqlite3

def lists():
    r = {}
    h = []
    conn = sqlite3.connect('pcmpdb')
    cursor = conn.execute("SELECT ipaddrs from cmdb_host where ipaddrs!='192.168.10.129'")
    for row in cursor:
        h.append(row[0])  
    hosts={'hosts': h}
    r['awshosts'] = hosts
    r['localhosts'] = {'hosts':['192.168.10.129']}
    return json.dumps(r,indent=4)

def hosts():
    r = {'ansible_ssh_pass': '123456'}
    cpis=dict(r.itmes())
    return json.dumps(cpis)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', help='hosts list', action='store_true')
    parser.add_argument('-H', '--host', help='hosts vars')
    args = vars(parser.parse_args())

    if args['list']:
        print lists()
    elif args['hosts']:
        print hosts(args['host'])
    else:
        parser.print_help()


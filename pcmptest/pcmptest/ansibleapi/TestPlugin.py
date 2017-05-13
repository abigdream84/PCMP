#!/usr/bin/env python


import os
import subprocess



class TestPlugin(object):

    def parse(self,content):
        pass
    
    def execute(self):
        try:
            shell_command = "sudo ansible all -m setup"
            status,output = subprocess.getstatusoutput(shell_command)
            if status != 0:
                raise Exception('linux command fail!')
            return output
        except Exception as e:
            raise Exception('linux command failed!')
        
        
        
t = TestPlugin()
data = t.execute()
print(data)
        
        

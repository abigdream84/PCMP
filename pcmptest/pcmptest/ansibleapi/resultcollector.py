#!/usr/bin/env python

import json
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import os
import subprocess
import commands



class ResultsCollector(CallbackBase):  
  
    def __init__(self, *args, **kwargs):  
        super(ResultsCollector, self).__init__(*args, **kwargs)  
        self.host_ok = {}  
        self.host_unreachable = {}  
        self.host_failed = {}  
  
    def v2_runner_on_unreachable(self, result):  
        self.host_unreachable[result._host.get_name()] = result  
  
    def v2_runner_on_ok(self, result,  *args, **kwargs):  
        self.host_ok[result._host.get_name()] = result  
  
    def v2_runner_on_failed(self, result,  *args, **kwargs):  
        self.host_failed[result._host.get_name()] = result


class TestPlugin(object):

    def parse(self,content):
        pass

    def execute(self):
        try:
            shell_command = "sudo ansible all -m setup"
            status,output = commands.getstatusoutput(shell_command)
            if status != 0:
                raise Exception('linux command fail!')
            return output
        except Exception as e:
            raise Exception('linux command failed!')


result_callback = ResultsCollector()
t = TestPlugin()
data = t.execute()
result_callback.v2_runner_on_ok(data)



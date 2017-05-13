#!/usr/bin/env python


import platform
from plainbox.impl import result
from reportlab.lib.colors import chartreuse


class BasePlugin(object):
    
    @classmethod
    def instance(cls):
        if hasattr(cls, 'instance'):
            return getattr(cls(),'instance')
        else:
            obj = cls()
            setattr(cls, 'instance', obj)
            return obj
    
    def is_os_32(self):
        os_bit, executable_type = platform.architecture()
        if os_bit == '32bit':
            return True
        elif os_bit == '64bit':
            return False
        raise Exception('unknow os bit')
    
    def execute(self):
        result = platform.system()
        if result == 'Linux':
            return self.linux()
        elif result == 'Windows':
            return self.windows()
        else:
            raise Exception('unknow os')
            
    def windows(self):
        pass
    
    def linux(self):
        pass













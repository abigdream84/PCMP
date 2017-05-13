'''
Created on 29Mar.,2017

@author: wyh
'''


def is_login(request, sessionid):
    username = request.session.get(sessionid,None)
    if not username:
        return False
    else:
        return username





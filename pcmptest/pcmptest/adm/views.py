from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse
from adm import models
from adm import httphelper

# Create your views here.

def register(request):
    '''
    t1 = models.usertype.objects.create(name='superadmin')
    t2 = models.usertype.objects.create(name='admin')
    t3 = models.usertype.objects.create(name='operator')
    
    u1 = models.user.objects.create(username='eric',password='123',email='eric@123.com',user_type=t1)
    u2 = models.user.objects.create(username='alex',password='321',email='alex@123.com',user_type=t2)
    
    g1 = models.group.objects.create(groupname='group1')
    g2 = models.group.objects.create(groupname='group2')
    g1.user.add(u1)
    g2.user.add(u1)
    '''

    return HttpResponse('register success')


def login(request):
    
    ret = {'status':''}
    
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        is_auth = all([username,password])
        if is_auth:
            count = models.user.objects.filter(username=username,password=password).count()
            if count == 1:
                request.session['is_login'] = {'user':username}           
                return redirect('/adm/index/')
            else:
                ret['status'] = 'Username or Password error!'
        else:
            ret['status'] = 'Username or Password should not be empty!'
    return render_to_response('adm/login.html',ret)
    

def index(request):
    username = httphelper.is_login(request, 'is_login')
    if username == False:
        return render_to_response('adm/login.html')
    else:
        return render_to_response('adm/index.html')

#def cmdb(request):
#    return render_to_response('adm/CMDB.html')

def host(request):
    username = request.session.get('is_login',None)
    ret={'status':'', 'data':None, 'group':None}
    print(username)
    if not username:
        return render_to_response('adm/login.html',ret)
    
    else:
        usergroup = models.group.objects.all()
        ret['group']= usergroup
        
        if request.method == 'POST':
            hostname=request.POST.get('hostname',None)
            ip = request.POST.get('ip',None)
            groupID = request.POST.get('group',None)
            
            is_auth = all([hostname,ip])
            if is_auth:
                groupObj = models.group.objects.get(id=groupID)
                models.host.objects.create(hostname=hostname,ip=ip,user_group=groupObj)
            else:
                ret['status']='Hostname or IP should not be empty.'
    
        data = models.host.objects.all()
        ret['data']=data
    
        return render_to_response('adm/CMDB.html',ret)





















  
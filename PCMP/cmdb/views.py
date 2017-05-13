from django.shortcuts import render,render_to_response, redirect
from django.shortcuts import HttpResponse
from cmdb import models
import json
import argparse
from botocore.vendored.requests.api import request
import boto
import PCMP.settings
from adm import httphelper


#import boto.ec2.instance.Instance


# Create your views here.

# Create your views here.



#@api_view(['GET','PUT','POST'])
def list_config(request):
    username = httphelper.is_login(request, 'is_login')
    if username == False:
        return render_to_response('adm/login.html')
    else:
        if request.method == 'GET':
    
            aws_access_key = PCMP.settings.AWS_ACCESS_KEY
            aws_access_secret = PCMP.settings.AWS_ACCESS_SECRET
            conn = boto.connect_ec2(aws_access_key, aws_access_secret)
            reservations = conn.get_all_instances()
            count = len(reservations)
            ipaddr_aws = ['192.168.10.129']
            for i in range(count):
                instance = reservations[i].instances[0]
                ip_address = instance.ip_address
                ipaddr_aws.append(ip_address)
            
            ipaddr_cmdb=[]
            all_server = models.Host.objects.all()
            for item in all_server:
                ipaddr_cmdb.append(item.ipaddrs)
    
            ip_add = list(set(ipaddr_aws).difference(set(ipaddr_cmdb)))
            ip_omit = list(set(ipaddr_cmdb).difference(set(ipaddr_aws)))
    
            for item in ip_add:
                models.Host.objects.create(ipaddrs=item)
                
            for item in ip_omit:
                t = models.Host.objects.filter(ipaddrs=item) 
                t.delete()  
    
            all_server = models.Host.objects.all()
            ser_list= []
            for item in all_server:
                ser = {}
                ser['hostname'] = item.hostname
                ser['ipaddrs'] = item.ipaddrs
                ser['cpu'] = item.cpu
                ser['memory'] = item.memory
                ser['disk'] = item.disk
                ser['status'] = item.status
                ser_list.append(ser)
    
    
            return render(request,'cmdb/ListConfig.html',{'data':ser_list})    
        
        
def receive_server_info(request):

    data = request.POST.get('data')
    data = json.loads(data)
    print(data)
    
    
    for index in data:
        flag = models.Host.objects.filter(ipaddrs=index)
        if flag:
            for item in flag:
                if item.hostname != data[index]['hostname']:
                    item.hostname = data[index]['hostname']
                    item.save()
                if item.cpu != data[index]['cpu']:
                    item.cpu = data[index]['cpu']
                    item.save()
                if item.memory != data[index]['memory']:
                    item.memory = data[index]['memory']
                    item.save()
                if item.disk != data[index]['disk']:
                    item.disk = data[index]['disk']
                    item.save()
                
        else:
            hostname=data[index]['hostname']
            ipaddrs=data[index]['ip']
            cpu=data[index]['cpu']
            memory=data[index]['memory']
            disk=data[index]['disk']
            s1 = models.Status.objects.get(name='running')
            status=s1
            models.Host.objects.create(hostname=hostname,ipaddrs=ipaddrs,cpu=cpu,memory=memory,disk=disk,status=status)
     
    return HttpResponse('ok')


'''
def test(request):
    data = {'disk': u'120.00 GB', 'ip': u'192.168.10.129', 'hostname': u'ubuntu1', 'cpu': 5, 'memory': 2965}
    hostname = data['hostname']
#    models.Status.objects.create(name='down')

#    s1 = models.Status.objects.get(name='running')
#    models.Host.objects.create(hostname='h1',ipaddrs='1.1.1.1',cpu=4,memory=2048,disk='100G',status=s1)
    flag = models.Host.objects.filter(hostname=hostname)
    if flag:
        print(type(flag))
        for item in flag:
            if item.ipaddrs != data['ip']:
                item.ipaddrs = data['ip']
                item.save()
            if item.cpu != data['cpu']:
                item.cpu = data['cpu']
                item.save()
            if item.memory != data['memory']:
                item.memory = data['memory']
                item.save()
            if item.disk != data['disk']:
                item.disk = data['disk']
                item.save()
            
    else:
        hostname=data['hostname']
        ipaddrs=data['ip']
        cpu=data['cpu']
        memory=data['memory']
        disk=data['disk']
        s1 = models.Status.objects.get(name='running')
        status=s1
        models.Host.objects.create(hostname=hostname,ipaddrs=ipaddrs,cpu=cpu,memory=memory,disk=disk,status=status)
        
    


    
    
    return HttpResponse('ok')
#    models.Host.objects.get()

'''


def create_server(request):

    username = httphelper.is_login(request, 'is_login')
    if username == False:
        return render_to_response('adm/login.html')
    else:
        if request.method == 'GET':
            return render_to_response('cmdb/CreateServer.html')
        else:
            aws_access_key = PCMP.settings.AWS_ACCESS_KEY
            aws_access_secret = PCMP.settings.AWS_ACCESS_SECRET
            image_id = request.POST['image_id']
            key_name = request.POST['key_name']
            instance_type = request.POST['instance_type']        
            subnet_id_tmp = request.POST['subnet_id']
            if subnet_id_tmp == 'None':
                subnet_id = None
            security_group_ids_tmp = request.POST['security_group_ids']
            if security_group_ids_tmp == 'None':
                security_group_ids = None     
            count_str = request.POST['count']
            count = int(count_str)
            conn = boto.connect_ec2(aws_access_key, aws_access_secret)
            for index in range(count):
                conn.run_instances(image_id=image_id, instance_type=instance_type, subnet_id=subnet_id, security_group_ids=security_group_ids, key_name=key_name)              
        return render(request,'cmdb/CreateServer.html')
        
def manage_server(request):
    username = httphelper.is_login(request, 'is_login')
    if username == False:
        return render_to_response('adm/login.html')
    else:
        if request.method == 'GET':
            aws_access_key = PCMP.settings.AWS_ACCESS_KEY
            aws_access_secret = PCMP.settings.AWS_ACCESS_SECRET
            conn = boto.connect_ec2(aws_access_key, aws_access_secret)
            reservations = conn.get_all_instances()
            count = len(reservations)
            ec2_list=[]
            for i in range(count):
                ins = {}
                instance = reservations[i].instances[0]
                ins['ip_address'] = instance.ip_address
                ins['instance_type'] = instance.instance_type
                ins['availability_zone'] = instance.placement
                ins['private_ip'] = instance.private_ip_address
                ins['state'] = instance.state
                ec2_list.append(ins)
                ins = {}
        return render(request,'cmdb/ManageServer.html',{'data':ec2_list})



from django.shortcuts import render
from django.shortcuts import HttpResponse 
#from rest_framework.decorators import api_view
from pcmptest.cmdb import models

# Create your views here.




#@api_view(['GET','PUT','POST'])
def receive_server_info(request):
    
    print(request.POST.get('data'))
    data = {'disk': u'120.00 GB', 'ip': u'192.168.10.129', 'hostname': u'ubuntu1', 'cpu': 6, 'memory': 2965}
    hostname = data['hostname']
#    if models.Host.objects.get(hostname=hostname)
    



    return HttpResponse('ok222')




def test():
    data = {'disk': u'120.00 GB', 'ip': u'192.168.10.129', 'hostname': u'ubuntu1', 'cpu': 6, 'memory': 2965}
    hostname = data['hostname']
    print(hostname)
#    models.Host.objects.get()



if __name__ == '__main__':
    test()









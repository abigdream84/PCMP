from django.conf.urls import url, include
from django.contrib import admin
#from api import views

from django.contrib.auth.models import User
from api.models import test
from api import views
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = test
        fields = ('url', 'c1', 'c2')

# ViewSets define the view behavior.
class TestViewSet(viewsets.ModelViewSet):
    queryset = test.objects.all()
    serializer_class = TestSerializer



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'test', TestViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^receive_server_info/',views.receive_server_info)


]

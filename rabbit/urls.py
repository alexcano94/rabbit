from django.conf.urls import url, include
from rest_framework import routers
from rabbit import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    url('', include(router.urls)),
]

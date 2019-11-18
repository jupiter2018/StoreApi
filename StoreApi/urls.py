"""StoreApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from StoreApi.Store import views
from StoreApi.Store.models import Manufacturer, ShoeType,ShoeColor,Shoe
admin.site.register(Manufacturer)
admin.site.register(Shoe)
admin.site.register(ShoeColor)
admin.site.register(ShoeType)
 
router = routers.DefaultRouter()
router.register(r'manufacturers', views.ManufacturerViewSet)
router.register(r'shoes', views.ShoeViewSet)
router.register(r'shoecolors', views.ShoeColorViewSet)
router.register(r'shoetypes', views.ShoeTypeViewSet)


urlpatterns = [
     path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

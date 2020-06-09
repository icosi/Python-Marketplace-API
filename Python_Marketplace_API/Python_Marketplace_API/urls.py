"""Python_Marketplace_API URL Configuration

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
from django.urls import path
from django.conf.urls import url, include
from marketplace import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^user/create/$', views.user_create, name='user_create'),
    url(r'^user/cart/$', views.user_cart, name='user_cart'),
    url(r'^user/add_product/$', views.user_add_product, name='user_add_product'),
    url(r'^user/checkout/$', views.user_checkout, name='user_checkout'),
    url(r'^product/all/$', views.product_all, name='product_all'),
    url(r'^product/id/$', views.product_id, name='product_id'),
    url(r'^product/new/$', views.product_new, name='product_new'),

]

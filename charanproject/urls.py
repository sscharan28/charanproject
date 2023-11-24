"""
URL configuration for charanproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Userapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('charan/',views.Home.as_view()),
    path('charan/reginput',views.RegInput.as_view()),
    path('charan/logininput',views.LoginInput.as_view()),
    path('charan/reg',views.Regview.as_view()),
    path('charan/login',views.Loginview.as_view()),
    path('charan/delete_view',views.delete_view),
    path('charan/create_view',views.create_view),
    path('charan/list_view',views.list_view),
    path('charan/update_view',views.update_view),
    path('charan/detail_view',views.detail_view),

]

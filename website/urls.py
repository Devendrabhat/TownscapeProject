"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from dataForms.views import home,template,ClientInfo,WaterProofingView, SoundVibrationVIew, ProjectConsultancyView,ProjectVarianceVIew,BankingView,MarketServeyView

urlpatterns = [
    path('', home, name = 'home'),
    path('admin/', admin.site.urls, name = 'admin'),
    path('template/',template, name = 'template'),
    path('clientInfo/',ClientInfo.as_view(), name = 'ClientInfo'),
    path('WaterProofingView/',WaterProofingView.as_view(), name = 'WaterProofingView'),
    path('SoundVibrationVIew/',SoundVibrationVIew.as_view(), name = 'SoundVibrationVIew'),
    path('ProjectConsultancyView/',ProjectConsultancyView.as_view(), name = 'ProjectConsultancyView'),
    path('ProjectVarianceVIew/',ProjectVarianceVIew.as_view(), name = 'ProjectVarianceVIew'),
    path('BankingView/',BankingView.as_view(), name = 'BankingView'),
    path('MarketServeyView/',MarketServeyView.as_view(), name = 'MarketServeyView'),
]

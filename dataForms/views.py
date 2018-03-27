from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import TemplateView

import re
# Create your views here.


# Template

def template(request):
    return render(request,'discrete/ClientInfo.html',{})

def home(request):
    views = ['ClientInfo','WaterProofingView', 'SoundVibrationVIew', 'ProjectConsultancyView','ProjectVarianceVIew','BankingView','MarketServeyView']
    forms = ['ClientInfo','WaterProofingForm', 'SoundVibrationForm', 'ProjectConsultancyForm','ProjectVarianceForm','BankingForm','MarketServeyForm']
    allViews = []
    for iterator in range(len(views)):
        allViews.append((views[iterator],forms[iterator]))
    # print(allViews)
    return render(request,'home.html',{'allViews':allViews})

# Client Info

# 1)
class ClientInfo(TemplateView):
    template_name = 'discrete/ClientInfo.html'
    def get(self,request, *args, **kwargs):
        return render(request,self.template_name,{})

# Technical consulatancy

# 2)
class WaterProofingView(TemplateView):
    template_name = 'discrete/WaterProofingView.html'
    def get(self,request, *args, **kwargs):
        return render(request,self.template_name,{})


# 3)
class SoundVibrationVIew(TemplateView):
    template_name = 'discrete/SoundVibrationVIew.html'
    def get(self,request, *args, **kwargs):
        return render(request,self.template_name,{})


# 4)
class ProjectConsultancyView(TemplateView):
    template_name = 'discrete/ProjectConsultancyView.html'
    def get(self,request, *args, **kwargs):
        return render(request,self.template_name,{})


# 5)
class ProjectVarianceVIew(TemplateView):
    template_name = 'discrete/ProjectVarianceVIew.html'
    def get(self,request, *args, **kwargs):
        return render(request,self.template_name,{})


# Banking & Finance

# 6)
class BankingView(TemplateView):
    template_name = 'discrete/BankingView.html'
    def get(self,request, *args, **kwargs):
        return render(request,self.template_name,{})

# Market Survey

# 7)
class MarketServeyView(TemplateView):
    template_name = 'discrete/MarketServeyView.html'
    def get(self,request, *args, **kwargs):
        return render(request,self.template_name,{})
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import TemplateView

# Create your views here.

class MainPage(TemplateView):
    template_name = 'index.html'

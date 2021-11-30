from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import TemplateView

# Create your views here.


class MainPage(TemplateView):
    template_name = 'index.html'


class NotFound(TemplateView):
    template_name = '404.html'

    def page_not_found_view(request, exception):
        return render(request, '404.html', status=404)

# from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from django.views.generic.base import View
from django.views.generic import TemplateView
from frost_met_app.models import Stations


class MainPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = dict()
        context["stations"] = Stations.objects.all().order_by(
            'validfrom')[:10]
        return context


class NotFound(TemplateView):
    template_name = '404.html'

    def page_not_found_view(request, exception):
        return render(request, '404.html', status=404)

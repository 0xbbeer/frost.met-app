from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from frost_met_app.models import Stations, MeasuringBegin, WindDirection
from django.contrib import messages
from frost_met_app import get_stations
from frost_met_app import get_wind_direction


class MainPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):

        context = dict()

        context["stations"] = \
            MeasuringBegin.objects.select_related(
                'station').all().order_by('start_date')[:10]

        context["wind"] = \
            WindDirection.objects.select_related(
                'station').all()

        context["wind"] = WindDirection.objects.all()

        return context


class NotFound(TemplateView):

    template_name = '404.html'

    def page_not_found_view(request, exception):

        return render(request, '404.html', status=404)


class DeleteData(TemplateView):

    def delete(request):
        if request.method == 'POST':

            action = request.POST.get("delete")

            if action == "delete":

                result = "Success"

                Stations.objects.all().delete()

                messages.info(request, result)

            else:
                result = "Failed"

                messages.info(request, result)

            return HttpResponseRedirect("/index/")


class GetData(TemplateView):

    def get_data(request):

        if request.method == 'POST':

            action = request.POST.get("get")

            if action == "get":

                result = "Success"

                Stations.objects.all().delete()

                get_stations.get_stations('GET')

                messages.info(request, result)

            else:

                result = "Failed"

                messages.info(request, result)

            return HttpResponseRedirect("/index/")


class AllStations(TemplateView):

    template_name = 'all_stations.html'

    def get_context_data(self, *args, **kwargs):

        context = dict()

        context["stations"] = Stations.objects.all().order_by(
            'validfrom')

        return context


class GetWindDirection(TemplateView):

    def get_data(request):

        if request.method == 'POST':

            action = request.POST.get("wind_direction")

            if action == "wind_direction":

                result = "Success"

                get_wind_direction.wind_direction('GET')

                messages.info(request, result)

            else:

                result = "Failed"

                messages.info(request, result)

            return HttpResponseRedirect("/index/")

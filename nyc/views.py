from django.shortcuts import render
from django.views import View

from nyc.boroughs import boroughs


class CityView(View):
    def get(self, request):
        return render(request=request, template_name='city.html', context={'boroughs': boroughs.keys()})


class BoroughView(View):
    def get(self, request, borough):
        return render(
            request=request,
            template_name='borough.html',
            context={'borough': borough, 'activities': boroughs[borough].keys()},
        )


class ActivityView(View):
    def get(self, request, borough, activity):
        print('borough', borough)
        print('activity', activity)
        return render(
            request = request,
            template_name = 'activities.html',
            context= {'activity': activity, 'activities': boroughs[borough][activity].keys(), }
        )


class VenueView(View):
    def get(self, request):
        pass

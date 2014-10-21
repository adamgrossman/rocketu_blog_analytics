from django.conf import settings
from ipware.ip import get_real_ip
import requests
from analytics.models import Page, Location, View


class LocationMiddleware(object):
    def process_request(self, request):
        # Get the IP Address of this request
        ip = get_real_ip(request)

        # If we didn't get an IP Address and we're developing locally,
        # make an API call to get our IP Address.
        if ip is None and settings.DEBUG:
            ip = requests.get('http://icanhazip.com/').text

        # ip = '152.122.42.1'

        if ip is not None:
            response = requests.get('http://ipinfo.io/{}/json'.format(ip))
            if response.status_code == 200:
                request.location = response.json()
                # Split out the lat and long from the location
                request.location['latitude'], request.location['longitude'] = request.location['loc'].split(',')

        request.ip = ip


class UserMiddleware(object):
    def process_request(self, request):
        page, created = Page.objects.get_or_create(url=request.META['PATH_INFO'])
        print page

        location, created = Location.objects.get_or_create(city=request.location['city'],
                                                           country=request.location['country'],
                                                           region=request.location['region'])
        # print location

        view, created = View.objects.get_or_create(location=location,
                                                   page=page,
                                                   latitude=request.location['latitude'],
                                                   longitude=request.location['longitude'],
                                                   ip_address=request.location['ip'])
        # print created

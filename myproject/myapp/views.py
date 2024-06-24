from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#def home(request):
#    return HttpResponse("Hello, Django!")


from django.shortcuts import render

def iframe_view(request):
    return render(request, 'iframe_page.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import utm

@csrf_exempt
def convert_utm(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        utm_x = float(data.get('utmX'))
        utm_y = float(data.get('utmY'))
        zone_number = int(data.get('zoneNumber'))
        hemisphere = data.get('hemisphere')
        northern = True if hemisphere == 'N' else False

        try:
            lat, lon = utm.to_latlon(utm_x, utm_y, zone_number, northern=northern)
            return JsonResponse({'latitude': lat, 'longitude': lon})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)



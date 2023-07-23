from django.shortcuts import render
from .models import City
from .forms import CityForm
from django.http import HttpResponse
import requests









def index1(request):

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&unitsimperial&appid=25c0f3d462221082c7df9658312102e0"
    

    form = CityForm()
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

   

    cities = City.objects.all()[:3]

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()
        try:
            weather = {
                'city': city.name,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon']

            }
        

            weather_data.append(weather)
        except KeyError:
            return HttpResponse('Check your spellings and try again')

    print(request.POST.get('name'))

    context = {'weather_data': weather_data, 'form': form}
        
    return render(request, 'current/index.html', context)
    # 524901










def index(request):

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&unitsimperial&appid=25c0f3d462221082c7df9658312102e0"
    
    cities = City.objects.all()[:3]

    
    if request.method == 'POST':
        city = request.POST.get('name')

        r = requests.get(url.format(city)).json()
        try:
            weather = {
                'city': city,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon']

            }
        except KeyError:
            return HttpResponse('Check your spellings and try again')   

        form = CityForm(request.POST)
        form.save()

    form = CityForm()





    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()
        
        weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }

        weather_data.append(weather)
   

    context = {'weather_data': weather_data, 'form': form}
        
    return render(request, 'current/index.html', context)
    # 524901






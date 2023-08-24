import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    appid = 'a577d2001cffb2ae7dfe9460ef6bdc9d'
    url = 'https://api.openweathermap.org/data/2.5/weather?q=Bishkek&units=metric&appid=' + appid   #https://api.openweathermap.org/data/2.5/weather?q=Bishkek&units=metric&appid=a577d2001cffb2ae7dfe9460ef6bdc9d

    if(request.method=="POST"):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        city_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'.format(city.name, appid)
        res = requests.get(city_url).json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, "form": form}

    return render(request, 'weather/index.html', context)

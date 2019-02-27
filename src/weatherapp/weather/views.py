
import requests
from django.shortcuts import render
from .models import city
from .forms import CityForm
# Create your views here.



def weather_home(request,*args,**kwargs):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b3cefc1ef44d1d56d313daeb7efab1b8'

    cities = city.objects.all()

    if request.method =='POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    weather_data = []

    # try:
    for cit in cities:
        # print(cit)
        r = requests.get(url.format(cit)).json()
        try:
            context = {
                'city': cit.name,
                'temperature': r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],

                    # 'city': cit,
                    # 'temperature': 'gg',
                    # 'description': 'guy',
                    # 'icon': 551,
            }
            weather_data.append(context)
        except:
            city.objects.get(name = cit).delete()
    #print(weather_data)
    weather_data.reverse()
    context1 = {'weather_data' : weather_data, 'form':form ,}
    # except:
    #
    # context1 = {'weather_data': weather_data, 'form': form, }
    return render(request, 'weather/weather.html', context1)

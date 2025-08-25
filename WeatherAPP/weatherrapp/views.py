from django.shortcuts import render
from django.shortcuts import HttpResponse
import requests
import datetime


def home(request):
    if request.method == 'POST':
        city = request.POST.get('city', 'jaipur')
    else:
        city = 'jaipur'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={ city }&appid=30f9d4617e8f1b11e387da9e7665cdc2'
    PARAMS = {'units':'metric'}
    data = requests.get(url,PARAMS).json()
    desc = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']
    date = datetime.datetime.today()

    return render(request,'weather.html',{'data':data,'temp':temp,'desc':desc,'icon':icon,'date':date,'city':city})
# Create your views here.

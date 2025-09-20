from django.shortcuts import render, HttpResponse
import json
import requests

# Create your views here.
def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid="
        list_of_data = requests.get(source.format(city)).json()
        

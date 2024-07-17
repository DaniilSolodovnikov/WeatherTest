from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import WeatherData  # If you're using a model
from openweathermap import OpenWeatherMap

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        try:
            api_key = 'ВАШ_API_KEY_OPENWEATHERMAP'
            owm = OpenWeatherMap(api_key)
            observation = owm.weather_at_place(city)
            weather = observation.current
            context = {
                'город' : city,
                'температура': weather.temperature('По цельсию'),
                'описание': weather.description,
            }
            return render(request, 'weather/index.html', context)
        except Exception as e:
            context = {'ошибка': f'Неверное название города или значение API ключа: {e}'}
            return render(request, 'weather/index.html', context)
        else:
            return render(request, 'weather/index.html')



import os
from django.shortcuts import render
from django.conf import settings
import requests
from datetime import datetime, timedelta

def get_weather_data(city):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    current_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        current_response = requests.get(current_url)
        current_data = current_response.json()
        
        if current_data['cod'] != 200:
            return None
            
        return {
            'temperature': current_data['main']['temp'],
            'humidity': current_data['main']['humidity'],
            'pressure': current_data['main']['pressure'],
            'description': current_data['weather'][0]['description'],
            'icon': current_data['weather'][0]['icon']
        }
        
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city', 'London')
        weather_data = get_weather_data(city)
        
        if weather_data:
            context = {
                'city': city,
                'temperature': weather_data['temperature'],
                'humidity': weather_data['humidity'],
                'pressure': weather_data['pressure'],
                'description': weather_data['description'],
                'icon': weather_data['icon']
            }
            return render(request, 'weather/index.html', context)
    
    return render(request, 'weather/index.html')

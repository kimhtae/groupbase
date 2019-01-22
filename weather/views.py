from django.shortcuts import render
import requests

def weather_search(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d441503e5c0fee2a41398bfd8a438028'
    #cities = City.objects.all() #return all the cities in the database
    cities =['Las Vegas','London']
    #city = 'Las Vegas'
    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather) #add the data for the current city into our list

    #context = {'weather' : weather}
    context = {'weather_data' : weather_data}
    
    return render(request, 'weather/weather_search.html', context) #returns the index.html template

   

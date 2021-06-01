from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def results(request):
    receivedcity = request.GET.get('receivedcity', 'default')

    import requests, json  # Importing Modules
    city = receivedcity # City Name
    api_key = "acea9fc1c2f727054048dcc964ee5cbe" #API Key received from openweathermap.org
    base_url = "https://api.openweathermap.org/data/2.5/weather?"   # Base URL Address
    url = base_url + "appid=" + api_key + "&q=" + city  # Complete URL address
    response = requests.get(url)    # Return response object
    x = response.json()
    # print (x)

    if x['cod'] == 200:
        city = x['name']
        country = x['sys']['country']
        weather = x['weather'][0]['main']
        icon = x['weather'][0]['icon']
        temperature = "{:.0f}".format(x['main']['temp'] - 273.15)
        min_temperature = "{:.0f}".format(x['main']['temp_min'] - 273.15)
        max_temperature = "{:.0f}".format(x['main']['temp_max'] - 273.15)
        kelvin_temp = "{:.0f}".format(x['main']['temp'])
        kelvin_mintemp = "{:.0f}".format(x['main']['temp_min'])
        kelvin_maxtemp = "{:.0f}".format(x['main']['temp_max'])
        humidity = x['main']['humidity']
        wind_speed = x['wind']['speed']

    else:
        return render(request, 'error404.html') # if the city is not found

    params = {'city': city, 'country': country, 'weather': weather, 'icon': icon, 'temperature': temperature, 'min_temperature': min_temperature, 'max_temperature': max_temperature, 'humidity': humidity, 'wind_speed': wind_speed, 'kelvin_temp': kelvin_temp, 'kelvin_mintemp': kelvin_mintemp, 'kelvin_maxtemp': kelvin_maxtemp}

    return render(request, 'results.html', params)


    

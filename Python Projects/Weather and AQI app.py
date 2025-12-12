import requests
from pprint import pprint
from colorama import Fore, Style

# API Key
API_key = #your api key.

# Getting User Input
City = input("Enter a city: ")

# Constructing the URL for the API
base_weather_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_key+"&q="+City
base_aqi_url = "http://api.openweathermap.org/data/2.5/air_pollution?appid="+API_key+"&lat={lat}&lon={lon}"

# Now Requesting the URL for weather
Weather = requests.get(base_weather_url).json()

# Check if the entered city is found or not
if Weather["cod"] == 200:
    # Getting the Weather Data along with the City
    print(Fore.LIGHTWHITE_EX + "Weather Details of " + City.capitalize() + " City are as following : " + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + "Tempreature :" + str(round(Weather['main']['temp'] - 273.15,2)) + " Degrees" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "Weather :" + Weather['weather'][0]['description'].capitalize() + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + "Humidity :" + str(Weather['main']['humidity']) + "%" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "Pressure :" + str(Weather['main']['pressure']) + " hPa" + Style.RESET_ALL)

    # Fetching latitude and longitude for the City
    lat = Weather['coord']['lat']
    lon = Weather['coord']['lon']

    # Now for AQI, requesting URL from base AQI
    aqi_url = base_aqi_url.format(lat=lat, lon=lon)
    AQI = requests.get(aqi_url).json()

    if 'list' in AQI:
        aqi = AQI['list'][0]['main']['aqi']

        # Mapping the AQI
        if aqi == 1:
            aqi_status, aqi_color = "Good", Fore.GREEN
        elif aqi == 2:
            aqi_status, aqi_color = "Fair", Fore.YELLOW
        elif aqi == 3:
            aqi_status, aqi_color = "Moderate", Fore.LIGHTRED_EX
        elif aqi == 4:
            aqi_status, aqi_color = "Poor", Fore.RED
        else :
            aqi_status, aqi_color = "Very Poor", Fore.MAGENTA

        # Printing AQI information with colors
        print(aqi_color + "Air Quality Index (AQI) :" + aqi_status + Style.RESET_ALL)
    else :
        
        # If the user inputs the wrong city name, this will return an error
        print(Fore.RED + "Error fetching AQI data: Unable to retrieve AQI information." + Style.RESET_ALL)
else : 
    # If user inputs wrong city name, this will return an error
    print(Fore.RED + "Error: " + Weather.get('message', 'Unknown error') + Style.RESET_ALL)       

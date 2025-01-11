import requests
from bs4 import BeautifulSoup

def fetch_weather(city):
    url = f"http://wttr.in/{city}?format=j1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current_condition = data['current_condition'][0]
        return {
            'temperature': current_condition['temp_C'],
            'humidity': current_condition['humidity'],
            'weather_desc': current_condition['weatherDesc'][0]['value']
        }
    else:
        return None

def main():
    city = input("Enter the city name: ")
    weather = fetch_weather(city)
    if weather:
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Weather Description: {weather['weather_desc']}")
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()
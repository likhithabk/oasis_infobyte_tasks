import requests
import os,sys

def get_weather_data(location):
    api_key = '3f6e055fe8cb4cb1a910544f738000ba'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    # Build the URL for the API request
    url = f'{base_url}q={location}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()

        # Check if the request was successful
        if response.status_code == 200:
            return data
        else:
            print("Error: Unable to retrieve weather data.")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def display_weather_data(weather_data):
    if weather_data:
        city = weather_data['name']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_conditions = weather_data['weather'][0]['description']

        print(f"Weather for {city}:")
       
        print(f"Temperature: {temperature}\u00b0C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Conditions: {weather_conditions}")
    else:
        print("No weather data available.")

def main():
    print("Welcome to the Basic Weather App!")
    location = input("Enter a city or ZIP code: ")

    weather_data = get_weather_data(location)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()

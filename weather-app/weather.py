import requests

API_KEY = "your_api_key_here"  # OpenWeatherMap se milega
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            return f"Error: {data['message']}"

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]

        return (f"\nWeather in {city}:\n"
                f"Temperature: {temp}°C\n"
                f"Humidity: {humidity}%\n"
                f"Condition: {desc.capitalize()}\n")

    except:
        return "Something went wrong!"

if __name__ == "__main__":
    city = input("Enter city name: ")
    print(get_weather(city))

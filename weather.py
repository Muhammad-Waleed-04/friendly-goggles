import requests

def get_weather(city):
    API_KEY = "one-call-3"  # ← Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/3.0new/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print("❌ City not found.")
    else:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        print(f"🌤️ Weather in {city}: {temp}°C, {desc.capitalize()}")

# Main
print("🌦️ Weather App")
city = input("Enter city name: ")
get_weather(city)


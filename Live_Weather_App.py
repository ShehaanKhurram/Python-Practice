import requests
API = "1f139e1b5647dad807ce0077d6e3a1a9"

while True:
    city_name = input("Enter city name ('exit' to quit): ")
    if city_name.lower() == 'exit':
        print(f"Good Bye!")
        break
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API}&units=metric"

    r = requests.get(url)
    if r.status_code == 200:
        print(f"\n______ Weather in City {city_name.capitalize()} ______\n")
        data = r.json()

        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather = data['weather'][0]['description'].capitalize()
        wind = data['wind']["speed"]
        print(f"Temperature: {temperature}\u00B0C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather}")
        print(f"Wind speed: {wind} m/s\n")

    elif r.status_code == 404:
        print("City not found! Please try again.\n")
   
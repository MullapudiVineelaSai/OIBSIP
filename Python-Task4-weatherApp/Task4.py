import requests

API_KEY = "598636650dea1c01e22f21e129d85370" # <<<<<< IDI CHANGE CHEY
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(location):
    # [ ] Input validation: reject empty city input
    if not location or location.strip() == "":
        print("Error: Please enter a City Name or ZIP Code.")
        return

    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric" # Celsius
    }

    try:
        # [ ] Make an API call to OpenWeatherMap and parse the JSON response
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        # [ ] Handle API errors gracefully
        if response.status_code == 200:
            # [ ] Display: current temperature, humidity, weather condition, wind speed
            print("\n========== Weather Report ==========")
            print(f"Location: {data['name']}, {data['sys']['country']}")
            print(f"Current Temperature: {data['main']['temp']} °C")
            print(f"Feels Like: {data['main']['feels_like']} °C")
            print(f"Humidity: {data['main']['humidity']} %")
            print(f"Weather Condition: {data['weather'][0]['description'].title()}") # e.g. Partly Cloudy
            print(f"Wind Speed: {data['wind']['speed']} m/s")
            print("====================================\n")

        elif response.status_code == 404:
            print("Error: City/ZIP not found. Please check spelling.")
        elif response.status_code == 401:
            print("Error: Invalid API Key. Please get a new key from openweathermap.org")
        else:
            print(f"Error: {data.get('message', 'Something went wrong')}")

    except requests.exceptions.Timeout:
        print("Error: Network timeout. Please check your internet connection.")
    except requests.exceptions.RequestException:
        print("Error: Could not connect to server. Please try again later.")


# [ ] Prompt user to enter a city name or ZIP code
if __name__ == "__main__":
    print("===== Basic Weather App - Oasis Infobyte =====")
    user_input = input("Enter City Name or ZIP Code: ")
    get_weather(user_input)

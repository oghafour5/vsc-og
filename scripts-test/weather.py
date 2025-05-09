"""
Weather Information Fetcher

This script provides a simple command-line interface to fetch and display current weather information
for any city using the wttr.in weather API. It retrieves and displays:
- Current weather conditions
- Temperature in both Celsius and Fahrenheit
- "Feels like" temperature
- Humidity percentage

Usage:
    python weather.py
    Then enter the city name when prompted.

Example:
    Enter the city name: London
    Weather in London:
    Current condition: Partly cloudy
    Temperature: 18°C / 64°F
    Feels like: 17°C / 63°F
    Humidity: 65%

Dependencies:
    - requests: For making HTTP requests to the weather API

Note:
    The script uses the free wttr.in API service which may have rate limits.
    Internet connection is required for the script to work.
"""

import requests

def get_weather(city):
    base_url = f"http://wttr.in/{city}?format=j1"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(base_url, headers=headers)
    response.raise_for_status()  # This will raise an HTTPError if the request failed
    weather_data = response.json()
    return weather_data

def print_weather(weather_data: dict) -> None:
    # Validate weather data structure
    if not weather_data.get('nearest_area') or not weather_data.get('current_condition'):
        print("Invalid or incomplete weather data received.")
        return

    print(f"Weather in {weather_data['nearest_area'][0]['areaName'][0]['value']}:")
    print(f"Current condition: {weather_data['current_condition'][0]['weatherDesc'][0]['value']}")
    print(f"Temperature: {weather_data['current_condition'][0]['temp_C']}°C / {weather_data['current_condition'][0]['temp_F']}°F")
    print(f"Feels like: {weather_data['current_condition'][0]['FeelsLikeC']}°C / {weather_data['current_condition'][0]['FeelsLikeF']}°F")
    print(f"Humidity: {weather_data['current_condition'][0]['humidity']}%")
def main() -> None:
    city = input("Enter the city name: ")
    if not city.strip():
        print("City name cannot be empty. Please try again.")
        return

    try:
        weather_data = get_weather(city)
        print_weather(weather_data)
    except requests.HTTPError as e:
        print(f"HTTP Error occurred: {e}")
    except requests.ConnectionError:
        print("Connection Error: Please check your internet connection.")
    except requests.Timeout:
        print("Request timed out. The weather service might be slow or unavailable.")
    except (ValueError, KeyError) as e:
        print(f"Data Error: Could not process the weather information: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
if __name__ == "__main__":
    main()


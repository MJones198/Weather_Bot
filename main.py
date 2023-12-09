# from geopy.geocoders import Nominatim
# import requests
# from datetime import datetime, timedelta
#
# # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
# with open("APIKey.txt", 'r') as file:
#     API_KEY = file.read()
#
# # Locations to fetch weather data for
# locations = ["Corfe Castle", "The Cotswolds", "Cambridge", "Cumbria", "Bristol, Oxford, Norwich, Stonehenge",
#              "Watergate Bay", "Birmingham"]
#
# def get_coordinates(location):
#     geolocator = Nominatim(user_agent="weather_app")
#     location_data = geolocator.geocode(location, language="en")
#     if location_data:
#         return location_data.latitude, location_data.longitude
#     else:
#         return None
#
# def get_weather_data(api_key, latitude, longitude):
#     base_url = "http://api.openweathermap.org/data/2.5/forecast"
#     params = {
#         'lat': latitude,
#         'lon': longitude,
#         'appid': api_key,
#         'units': 'metric'  # You can change to 'imperial' for Fahrenheit
#     }
#     response = requests.get(base_url, params=params)
#     data = response.json()
#     return data['list']
#
# def parse_weather_data(weather_data):
#     parsed_data = []
#     for entry in weather_data:
#         date = datetime.utcfromtimestamp(entry['dt']).strftime('%Y-%m-%d')
#         min_temp = entry['main']['temp_min']
#         max_temp = entry['main']['temp_max']
#         parsed_data.append({'date': date, 'min_temp': min_temp, 'max_temp': max_temp})
#     return parsed_data
#
# def get_forecast_data(api_key, locations):
#     forecast_data = {}
#     for location in locations:
#         coordinates = get_coordinates(location)
#         if coordinates:
#             latitude, longitude = coordinates
#             weather_data = get_weather_data(api_key, latitude, longitude)
#             forecast_data[location] = parse_weather_data(weather_data)
#     return forecast_data
#
#
#     # # Print the forecast data
#     # for location, data in forecast_data.items():
#     #     print(f"\n{location} 5-Day Forecast:")
#     #     for entry in data:
#     #         print(f"Date: {entry['date']}, Min Temp: {entry['min_temp']}°C, Max Temp: {entry['max_temp']}°C")
#
# if __name__ == "__main__":
#     forecast_data = get_forecast_data(API_KEY, locations)
#
#     print("\nCorfe Castle 5-Day Forecast:")
#     for entry in forecast_data["Corfe Castle"]:
#         print(f"Date: {entry['date']}, Min Temp: {entry['min_temp']}°C, Max Temp: {entry['max_temp']}°C")
#
#     print("\nThe Cotswolds 5-Day Forecast:")
#     for entry in forecast_data["The Cotswolds"]:
#         print(f"Date: {entry['date']}, Min Temp: {entry['min_temp']}°C, Max Temp: {entry['max_temp']}°C")
#
#     print("\nCambridge 5-Day Forecast:")
#     for entry in forecast_data["Cambridge"]:
#         print(f"Date: {entry['date']}, Min Temp: {entry['min_temp']}°C, Max Temp: {entry['max_temp']}°C")
#
#     print("\nCumbria 5-Day Forecast:")
#     for entry in forecast_data["Cumbria"]:
#         print(f"Date: {entry['date']}, Min Temp: {entry['min_temp']}°C, Max Temp: {entry['max_temp']}°C")
#
#     print("\nBristol 5-Day Forecast:")
#     for entry in forecast_data["Bristol"]:
#         print(f"Date: {entry['date']}, Min Temp: {entry['min_temp']}°C, Max Temp: {entry['max_temp']}°C")
#
#     print("\nOxford 5-Day Forecast:")
#     for entry in forecast_data["Oxford"]:
#         print(f"Date: {entry['date']}, Min Temp: {entry['min_temp']}°C, Max Temp: {entry['max_temp']}°C")
#
#     print("\nNorwich 5-Day Forecast:")
#     for entry in forecast_data["Norwich"]:
#         print(f"Date: {entry['date']}, Min Temp: {entry['min_temp']}°C, Max Temp: {entry['max_temp']}°C")
#
#     print("\nStonehenge 5-Day Forecast:")
#     for entry in forecast_data["Stonehenge"]:
#         print(f"Date: {entry['date']}, Min Temp: {entry['min_temp']}°C, Max Temp: {entry['max_temp']}°C")
#
#     # Repeat the above print statements for each location
#     # ...
#
#     print("\nBirmingham 5-Day Forecast:")
#     for entry in forecast_data["Birmingham"]:
#         print(f"Date: {entry['date']}, Min Temp: {entry['min_temp']}°C, Max Temp: {entry['max_temp']}°C")
#

'''

BREAK

'''

# import requests
# from geopy.geocoders import Nominatim
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
#
# # Function to get coordinates using geopy
# def get_coordinates(location):
#     geolocator = Nominatim(user_agent="my_geocoder")
#     location_data = geolocator.geocode(location)
#
#     if location_data:
#         return location_data.latitude, location_data.longitude
#     else:
#         print(f"Couldn't find coordinates for {location}")
#         return None, None
#
# # Function to get 5-day forecast using OpenWeatherMap API
# def get_5_day_forecast(api_key, latitude, longitude):
#     base_url = "http://api.openweathermap.org/data/2.5/forecast"
#     params = {
#         "lat": latitude,
#         "lon": longitude,
#         "appid": api_key,
#         "units": "metric",  # You can change the units to imperial if needed
#     }
#
#     response = requests.get(base_url, params=params)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Error fetching forecast for coordinates {latitude}, {longitude}")
#         return None
#
# # Set your OpenWeatherMap API key here
# with open("APIKey.txt", 'r') as file:
#     openweathermap_api_key = file.read()
#
# # Initialize ChatterBot
# chatbot = ChatBot("My ChatterBot")
# trainer = ListTrainer(chatbot)
#
# # Train ChatterBot with conversation data
# conversation_data = [
#     "Hi",
#     "Hello!",
#     "How are you?",
#     "I'm good, thank you.",
#     "What is your name?",
#     "I am a chat bot.",
#     "Tell me a joke",
#     "Why don't scientists trust atoms? Because they make up everything!",
# ]
#
# # Add questions for each location and responses with 5-day forecast
# locations = [
#     "Corfe Castle", "The Cotswolds", "Cambridge", "Cumbria",
#     "Bristol", "Oxford", "Norwich", "Stonehenge", "Watergate Bay", "Birmingham"
# ]
#
# for location in locations:
#     question = f"What is the weather for {location}?"
#
#     # Get coordinates and forecast data for the current location
#     latitude, longitude = get_coordinates(location)
#     forecast = get_5_day_forecast(openweathermap_api_key, latitude, longitude)
#
#     if forecast:
#         daily_forecast = {}
#         for entry in forecast['list']:
#             date = entry['dt_txt'].split(' ')[0]
#             if date not in daily_forecast:
#                 daily_forecast[date] = {
#                     "temperature": entry['main']['temp'],
#                     "description": entry['weather'][0]['description']
#                 }
#
#         response = f"The 5-day forecast for {location} is:\n"
#         for date, details in sorted(daily_forecast.items()):
#             response += f"{date}: {details['temperature']}°C, {details['description']}\n"
#
#         conversation_data.extend([question, response])
#
# trainer.train(conversation_data)
#
# # Start the conversation loop with the chat bot
# print("\nYou can start chatting with the chat bot. Type 'exit' to end the conversation.")
# while True:
#     user_input = input("You: ")
#
#     if user_input.lower() == 'exit':
#         print("Goodbye!")
#         break
#
#     # Check for the specific questions about the weather for each location
#     for location in locations:
#         if f"weather for {location}" in user_input.lower():
#             # Print the 5-day forecast for the specified location
#             location_data = next((data for data in forecast_data if data["location"] == location), None)
#             if location_data:
#                 print(f"\n{location_data['location']} Forecast:")
#                 for date, details in sorted(location_data['forecast'].items()):
#                     print(f"{date}: {details['temperature']}°C, {details['description']}")
#             else:
#                 print(f"No data found for {location}.")
#             break
#     else:
#         # Get the chat bot's response for general conversation
#         response = chatbot.get_response(user_input)
#         print(f"Bot: {response}")
import requests
from geopy.geocoders import Nominatim
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Function to get coordinates using geopy
def get_coordinates(location):
    geolocator = Nominatim(user_agent="my_geocoder")
    location_data = geolocator.geocode(location)

    if location_data:
        return location_data.latitude, location_data.longitude
    else:
        print(f"Couldn't find coordinates for {location}")
        return None, None

# Function to get 5-day forecast using OpenWeatherMap API
def get_5_day_forecast(api_key, latitude, longitude):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "units": "metric",  # You can change the units to imperial if needed
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching forecast for coordinates {latitude}, {longitude}")
        return None

# Set your OpenWeatherMap API key here
with open("APIKey.txt", 'r') as file:
    openweathermap_api_key = file.read()

# Initialize ChatterBot
chatbot = ChatBot("My ChatterBot")
trainer = ListTrainer(chatbot)

# Train ChatterBot with conversation data
conversation_data = [
    "Hi",
    "Hello!",
    "How are you?",
    "I'm good, thank you.",
    "What is your name?",
    "I am a chat bot.",
    "Tell me a joke",
    "Why don't scientists trust atoms? Because they make up everything!",
]

# Add questions for each location and responses with 5-day forecast
locations = [
    "Corfe Castle", "The Cotswolds", "Cambridge", "Cumbria",
    "Bristol", "Oxford", "Norwich", "Stonehenge", "Watergate Bay", "Birmingham"
]

for location in locations:
    question = f"What is the weather for {location}?"

    # Get coordinates and forecast data for the current location
    latitude, longitude = get_coordinates(location)
    forecast = get_5_day_forecast(openweathermap_api_key, latitude, longitude)

    if forecast:
        forecast_string = ""
        for entry in forecast['list']:
            date = entry['dt_txt'].split(' ')[0]
            forecast_string += f"{date}: {entry['main']['temp']}°C, {entry['weather'][0]['description']}\n"

        response = f"The 5-day forecast for {location} is:\n{forecast_string}"
        conversation_data.extend([question, response])

trainer.train(conversation_data)

# Start the conversation loop with the chat bot
print("\nYou can start chatting with the chat bot. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Check for the specific questions about the weather for each location
    for location in locations:
        if f"weather for {location}" in user_input.lower():
            # Print the 5-day forecast for the specified location
            for data in conversation_data:
                if f"{location} Forecast:" in data:
                    print(data)
                    break
            else:
                print(f"No data found for {location}.")
            break
    else:
        # Get the chat bot's response for general conversation
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")

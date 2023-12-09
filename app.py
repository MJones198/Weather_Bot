from flask import Flask, render_template, request
import requests
from geopy.geocoders import Nominatim
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

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

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    user_input = None
    bot_response = None

    if request.method == 'POST':
        user_input = request.form['user_input']

        # Check for the specific questions about the weather for each location
        for location in locations:
            if f"weather for {location}" in user_input.lower():
                # Get the 5-day forecast for the specified location
                for data in conversation_data:
                    if f"{location} Forecast:" in data:
                        bot_response = data
                        break
                else:
                    bot_response = f"No data found for {location}."
                break
        else:
            # Get the chat bot's response for general conversation
            bot_response = chatbot.get_response(user_input)

    return render_template('index.html', user_input=user_input, bot_response=bot_response)

if __name__ == '__main__':
    app.run(debug=True)

project Report: Real-Time Weather App
1. Introduction
This project is a Real-Time Weather Application developed using Python, Streamlit, and OpenWeatherMap API.
The main objective is to provide users with the current weather information for any city in the world in a simple and interactive interface.

2. Objectives
Display current weather details (temperature, humidity, condition).
Provide a user-friendly interface using Streamlit.
Fetch real-time weather data using OpenWeatherMap API.
Ensure accuracy and easy usability.

3. Tools & Technologies
Python – Programming language.
Streamlit – To create the web-based interface.
Requests – For sending HTTP requests to the API.
OpenWeatherMap API – To fetch real-time weather data.

4. Methodology
Step 1: Input
The user enters the city name in the app.

Step 2: API Request
The app sends a GET request to OpenWeatherMap API using:
http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric

Step 3: Processing
The API responds with weather details in JSON format.
The app extracts temperature, humidity, and weather condition.

Step 4: Output
The details are displayed in a Streamlit web app with simple formatting and icons.

6. Results
The application successfully displays:
Temperature in Celsius
Humidity in percentage
Weather condition (clear, cloudy, rainy, etc.)

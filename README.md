## GitHub User & City Weather API
A FastAPI project demonstrating the use of query parameters and path parameters to fetch data from external APIs.

This application provides two endpoints:
1. GitHub User Endpoint – Retrieve GitHub user details via a query parameter.
2. City Weather Endpoint – Retrieve current weather information for a city via a path parameter.

## Features
1. Query Parameter Endpoint: Fetch GitHub user information including login, name, public_repos, followers, and following.
2. Path Parameter Endpoint: Fetch current weather details for a specified city, including temperature in Celsius and weather description.
3. Error Handling: Handles invalid usernames, invalid city names, and API rate limits gracefully.

## Setup Instructions
1. Clone the Repository
git clone https://github.com/your-username/weather_github_api.git
cd weather_github_api

2. Install Dependencies
pip install -r requirements.txt

3. Run the Application
uvicorn main:app --reload --port 3400

API Endpoints
1. GitHub User Endpoint (Query Parameter)
GET http://localhost:3400/get_github_user?username=octocat

2. City Weather Endpoint (Path Parameter)
GET http://localhost:3400/get_weather/London

## Note
Replace "your_api_key_here" in main.py with a valid OpenWeather API Key.
Without a valid API key, the weather endpoint will not return data.



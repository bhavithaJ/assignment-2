from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

GITHUB_URL = "https://api.github.com/users/"
OPENWEATHER_API_KEY = "your_api_key_here"  # put your API key here

# Endpoint 1: GitHub User
@app.get("/get_github_user")
def get_github_user(username: str):
    r = requests.get(f"{GITHUB_URL}{username}")
    if r.status_code == 404:
        raise HTTPException(status_code=404, detail="User not found")
    if r.status_code == 403:
        raise HTTPException(status_code=403, detail="Rate limit exceeded")
    data = r.json()
    return {
        "login": data.get("login"),
        "name": data.get("name"),
        "public_repos": data.get("public_repos"),
        "followers": data.get("followers"),
        "following": data.get("following"),
    }

# Endpoint 2: Weather
@app.get("/get_weather/{city}")
def get_weather(city: str):
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={OPENWEATHER_API_KEY}"
    geo_data = requests.get(geo_url).json()
    if not geo_data:
        raise HTTPException(status_code=404, detail="City not found")
    lat, lon = geo_data[0]["lat"], geo_data[0]["lon"]

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
    weather_data = requests.get(weather_url).json()

    return {
        "city": city,
        "temperature": weather_data["main"]["temp"],
        "weather": weather_data["weather"][0]["description"],
    }

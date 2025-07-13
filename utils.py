import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_HOST = os.getenv("RAPIDAPI_HOST", "concerts-artists-events-tracker.p.rapidapi.com")
HEADERS = {
    "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
    "x-rapidapi-host": API_HOST
}
BASE_URL = f"https://{API_HOST}"

MOCK_DIR = "mock"

def load_mock(filename):
    path = os.path.join(MOCK_DIR, filename)
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Mock file {filename} not found")
        return None

def search_artist_or_event(keyword):
    print(f"Searching for '{keyword}'")
    data = load_mock("search.json")
    if data:
        return data
    try:
        resp = requests.get(f"{BASE_URL}/search",
                            headers=HEADERS,
                            params={"keyword": keyword, "types": "artist,event"})
        data = resp.json()
        print("API response:", data)
        return data
    except Exception as e:
        print("Error calling /search:", e)
        return {"data": []}

def get_artist_bio(artist_id):
    print(f"Getting artist bio for ID {artist_id}")
    bio_data = load_mock("bio.json")
    if bio_data:
        for item in bio_data.get("data", []):
            if item.get("id") == artist_id:
                return item
        print(f"No bio for artist_id {artist_id} in mock")
    try:
        resp = requests.get(f"{BASE_URL}/artist/bio",
                            headers=HEADERS,
                            params={"artist_id": artist_id})
        return resp.json()
    except Exception as e:
        print("Error calling /artist/bio:", e)
        return {}

def get_artist_events(artist_id):
    print(f"Getting events for artist ID {artist_id}")
    ev_data = load_mock("events.json")
    if ev_data:
        filtered = [e for e in ev_data.get("data", []) if e.get("artist_id") == artist_id]
        return {"data": filtered}
    try:
        resp = requests.get(f"{BASE_URL}/artist/events",
                            headers=HEADERS,
                            params={"artist_id": artist_id})
        return resp.json()
    except Exception as e:
        print("Error calling /artist/events:", e)
        return {"data": []}

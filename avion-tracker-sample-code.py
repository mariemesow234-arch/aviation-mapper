# AVIATION TRACKER - SAMPLE CODE
import requests
import json

def get_my_location():
    """Get user location via IP"""
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        return {
            'city': data.get('city', 'Unknown'),
            'country': data.get('country', 'Unknown'),
            'lat': data.get('lat', 0),
            'lon': data.get('lon', 0)
        }
    except:
        return None

def get_nearby_planes(lat, lon, radius=150):
    """Get aircraft near location"""
    try:
        url = f"https://api.airplanes.live/v2/point/{lat}/{lon}/{radius}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('ac', [])
    except:
        return []

# Demo execution
print("🚀 AVIATION TRACKER RUNNING...")
my_location = get_my_location()

if my_location:
    print(f"📍 You are in: {my_location['city']}, {my_location['country']}")
    
    planes = get_nearby_planes(my_location['lat'], my_location['lon'])
    print(f"✈  Found {len(planes)} aircraft nearby")
    
    # Show first 3 planes
    for plane in planes[:3]:
        flight = plane.get('flight', 'Unknown')
        alt = plane.get('altitude', 'N/A')
        print(f"   - {flight} at {alt} feet")
else:
    print("❌ Could not determine location")
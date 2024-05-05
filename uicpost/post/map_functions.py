from geopy.distance import geodesic
import json
import requests


def geo(lon, lat, lang):
    params = {'lat': lat, 'lon': lon, 'accept-language': lang}
    req = requests.get("https://nominatim.openstreetmap.org/reverse?format=geojson", params=params)
    out = json.loads(req.text)
    return out#['features'][0]['properties']['address']['city']

def pos(country):
    params = {'q': country, 'format': 'json'}
    req = requests.get("https://nominatim.openstreetmap.org/search", params=params)
    out = json.loads(req.text)
    return out[0]['lon'], out[0]['lat']

def decode_polyline(polyline_str):
    index = 0
    coordinates = []
    lat = 0
    lon = 0
    while index < len(polyline_str):
        shift = 0
        result = 0
        while True:
            byte = ord(polyline_str[index]) - 63
            index += 1
            result |= (byte & 0x1f) << shift
            shift += 5
            if not byte >= 0x20:
                break
        dlat = ~(result >> 1) if result & 1 else result >> 1
        lat += dlat

        shift = 0
        result = 0
        while True:
            byte = ord(polyline_str[index]) - 63
            index += 1
            result |= (byte & 0x1f) << shift
            shift += 5
            if not byte >= 0x20:
                break
        dlon = ~(result >> 1) if result & 1 else result >> 1
        lon += dlon

        coordinates.append([lat * 1e-5, lon * 1e-5])

    return coordinates

def calculate_distance(coords):
    total_distance = 0
    for i in range(len(coords) - 1):
        total_distance += geodesic(coords[i], coords[i+1]).kilometers
    return total_distance

def calculate_order(pick_up_address, drop_off_address, car_type):
    pick_coords = pos(pick_up_address)
    drop_coords = pos(drop_off_address)

    osrm_url = f'http://router.project-osrm.org/route/v1/driving/{pick_coords[0]},{pick_coords[1]};{drop_coords[0]},{drop_coords[1]}?overview=full&steps=true'
    response = requests.get(osrm_url)
    route_data = response.json()

    route_coordinates = []
    for leg in route_data['routes'][0]['legs']:
        for step in leg['steps']:
            geometry = step['geometry']
            coordinates = decode_polyline(geometry)
            route_coordinates.extend(coordinates)

    distance_km = calculate_distance(route_coordinates)

    prices = {
        'standard': 100,
        'comfort': 150,
        'minivan': 200
    }

    calculated_price = prices.get(car_type, 250) * distance_km

    return calculated_price, distance_km, pick_coords, drop_coords
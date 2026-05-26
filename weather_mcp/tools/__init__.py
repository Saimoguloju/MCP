import os
import httpx

BASE_URL = "https://api.openweathermap.org/data/2.5"
AIR_URL = "https://api.openweathermap.org/data/2.5/air_pollution"
GEO_URL = "http://api.openweathermap.org/geo/1.0/direct"


def _api_key() -> str:
    key = os.getenv("WEATHER_API_KEY", "")
    if not key:
        raise RuntimeError("WEATHER_API_KEY is not set in .env")
    return key


def _units_label(units: str) -> dict:
    return {"metric": "°C", "imperial": "°F", "standard": "K"}.get(units, "°C")


def get_current_weather(city: str, units: str = "metric") -> str:
    """Fetch current weather conditions for a city."""
    params = {"q": city, "appid": _api_key(), "units": units}
    r = httpx.get(f"{BASE_URL}/weather", params=params, timeout=15)
    r.raise_for_status()
    d = r.json()

    main = d["main"]
    wind = d.get("wind", {})
    weather = d["weather"][0]
    deg = _units_label(units)

    return (
        f"Weather in {d['name']}, {d['sys']['country']}\n"
        f"Condition   : {weather['description'].title()}\n"
        f"Temperature : {main['temp']}{deg}  (feels like {main['feels_like']}{deg})\n"
        f"Min / Max   : {main['temp_min']}{deg} / {main['temp_max']}{deg}\n"
        f"Humidity    : {main['humidity']}%\n"
        f"Pressure    : {main['pressure']} hPa\n"
        f"Wind Speed  : {wind.get('speed', 'N/A')} m/s\n"
        f"Visibility  : {d.get('visibility', 'N/A')} m\n"
        f"Cloud Cover : {d['clouds']['all']}%"
    )


def get_forecast(city: str, days: int = 5, units: str = "metric") -> str:
    """Fetch a multi-day weather forecast for a city (max 5 days)."""
    days = max(1, min(days, 5))
    params = {"q": city, "appid": _api_key(), "units": units, "cnt": days * 8}
    r = httpx.get(f"{BASE_URL}/forecast", params=params, timeout=15)
    r.raise_for_status()
    d = r.json()

    deg = _units_label(units)
    seen_dates: set = set()
    lines = [f"Forecast for {d['city']['name']}, {d['city']['country']}"]

    for entry in d["list"]:
        date = entry["dt_txt"].split(" ")[0]
        if date in seen_dates:
            continue
        seen_dates.add(date)
        if len(seen_dates) > days:
            break

        main = entry["main"]
        desc = entry["weather"][0]["description"].title()
        lines.append(
            f"\n{date}\n"
            f"  {desc}\n"
            f"  Temp    : {main['temp']}{deg}  (feels like {main['feels_like']}{deg})\n"
            f"  Min/Max : {main['temp_min']}{deg} / {main['temp_max']}{deg}\n"
            f"  Humidity: {main['humidity']}%"
        )

    return "\n".join(lines)


def get_weather_by_coords(lat: float, lon: float, units: str = "metric") -> str:
    """Fetch current weather by geographic coordinates (latitude, longitude)."""
    params = {"lat": lat, "lon": lon, "appid": _api_key(), "units": units}
    r = httpx.get(f"{BASE_URL}/weather", params=params, timeout=15)
    r.raise_for_status()
    d = r.json()

    main = d["main"]
    wind = d.get("wind", {})
    weather = d["weather"][0]
    deg = _units_label(units)

    return (
        f"Weather at ({lat}, {lon}) — {d.get('name', 'Unknown')}\n"
        f"Condition   : {weather['description'].title()}\n"
        f"Temperature : {main['temp']}{deg}  (feels like {main['feels_like']}{deg})\n"
        f"Humidity    : {main['humidity']}%\n"
        f"Pressure    : {main['pressure']} hPa\n"
        f"Wind Speed  : {wind.get('speed', 'N/A')} m/s\n"
        f"Cloud Cover : {d['clouds']['all']}%"
    )


def get_air_quality(city: str) -> str:
    """Fetch air quality index and pollutant levels for a city."""
    # Resolve city to coordinates first
    geo_params = {"q": city, "limit": 1, "appid": _api_key()}
    geo_r = httpx.get(GEO_URL, params=geo_params, timeout=15)
    geo_r.raise_for_status()
    geo_data = geo_r.json()
    if not geo_data:
        return f"Could not find coordinates for '{city}'."

    lat, lon = geo_data[0]["lat"], geo_data[0]["lon"]
    country = geo_data[0].get("country", "")

    params = {"lat": lat, "lon": lon, "appid": _api_key()}
    r = httpx.get(AIR_URL, params=params, timeout=15)
    r.raise_for_status()
    d = r.json()

    aqi_labels = {1: "Good", 2: "Fair", 3: "Moderate", 4: "Poor", 5: "Very Poor"}
    aqi = d["list"][0]["main"]["aqi"]
    comp = d["list"][0]["components"]

    return (
        f"Air Quality for {city.title()}, {country}\n"
        f"AQI         : {aqi} — {aqi_labels.get(aqi, 'Unknown')}\n"
        f"CO          : {comp.get('co', 'N/A')} μg/m³\n"
        f"NO₂         : {comp.get('no2', 'N/A')} μg/m³\n"
        f"O₃          : {comp.get('o3', 'N/A')} μg/m³\n"
        f"PM2.5       : {comp.get('pm2_5', 'N/A')} μg/m³\n"
        f"PM10        : {comp.get('pm10', 'N/A')} μg/m³\n"
        f"SO₂         : {comp.get('so2', 'N/A')} μg/m³"
    )

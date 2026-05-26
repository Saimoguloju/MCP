import os
import sys
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

if not os.getenv("WEATHER_API_KEY"):
    print("ERROR: WEATHER_API_KEY not set in .env", file=sys.stderr)
    sys.exit(1)

from weather_mcp.tools import (
    get_current_weather,
    get_forecast,
    get_weather_by_coords,
    get_air_quality,
)

mcp = FastMCP("Weather MCP Server")


@mcp.tool()
def current_weather(city: str, units: str = "metric") -> str:
    """Get current weather conditions for a city.
    units: 'metric' (°C), 'imperial' (°F), or 'standard' (K)
    """
    return get_current_weather(city, units)


@mcp.tool()
def weather_forecast(city: str, days: int = 5, units: str = "metric") -> str:
    """Get a day-by-day weather forecast for a city (1–5 days).
    units: 'metric' (°C), 'imperial' (°F), or 'standard' (K)
    """
    return get_forecast(city, days, units)


@mcp.tool()
def weather_by_coordinates(lat: float, lon: float, units: str = "metric") -> str:
    """Get current weather by latitude and longitude.
    units: 'metric' (°C), 'imperial' (°F), or 'standard' (K)
    """
    return get_weather_by_coords(lat, lon, units)


@mcp.tool()
def air_quality(city: str) -> str:
    """Get air quality index and pollutant levels for a city."""
    return get_air_quality(city)


if __name__ == "__main__":
    mcp.run()

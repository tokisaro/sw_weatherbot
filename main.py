import python_weather

async def getweather(city:str):
  async with python_weather.Client(unit=python_weather.METRIC, locale=python_weather.Locale.RUSSIAN) as client:
    weather = await client.get(city)
   
    return f"Город: {weather.nearest_area.name}\nТемпература: {weather.current.temperature}°C\nПогода: {weather.current.description}"
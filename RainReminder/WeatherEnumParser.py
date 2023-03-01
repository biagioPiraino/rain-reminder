from WeatherEnums import WeatherCondition

class WheatherEnumParser:
  
  @classmethod
  def ParseWeatherId(self, weather_id: int) -> WeatherCondition:
    if weather_id >  800:       return WeatherCondition.Clouds
    if weather_id == 800:       return WeatherCondition.Clear
    if 600 <= weather_id < 700: return WeatherCondition.Snow
    if 500 <= weather_id < 600: return WeatherCondition.Rain
    if 300 <= weather_id < 400: return WeatherCondition.Drizzle
    if 200 <= weather_id < 300: return WeatherCondition.Thunderstorm 
    return WeatherCondition.Unknown
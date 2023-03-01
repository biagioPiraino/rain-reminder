from datetime import datetime
from WeatherEnums import WeatherCondition
from WeatherEnumParser import WheatherEnumParser

class WeatherCondition:
  def __init__(self, 
                forecast_time: datetime, 
                wheather_id: int,
                description: str ) -> None:
      self.__forecast_time      = forecast_time
      self.__whether_id         = wheather_id
      self.__description        = description
      self.__weather_condition  = self.__parseWeatherId()

  def GetForecastTime(self) -> datetime:
    return self.__forecast_time
  
  def GetWheatherID(self) -> int:
    return self.__whether_id
  
  def GetDescription(self) -> str:
    return self.__description
  
  def GetWeatherCondition(self) -> WeatherCondition:
    return self.__weather_condition
  
  def __parseWeatherId(self) -> WeatherCondition:
    return WheatherEnumParser.ParseWeatherId(self.__whether_id)
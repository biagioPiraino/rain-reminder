from datetime import datetime

class WeatherCondition:
  def __init__(self, 
                forecast_time: datetime, 
                wheather_id: int,
                description: str ) -> None:
      self.__forecast_time = forecast_time
      self.__whether_id    = wheather_id
      self.__description   = description

  def GetForecastTime(self) -> datetime:
    return self.__forecast_time
  
  def GetWheatherID(self) -> int:
    return self.__whether_id
  
  def GetDescription(self) -> str:
    return self.__description
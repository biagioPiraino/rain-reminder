import requests as rq
from ParametersReader import ParametersReader as PR
from ApiDataFilter import ApiDataFilter as Filter
from ApiDataFormatter import ApiDataFormatter as Formatter

class ApiRequester:
  def __init__(self) -> None:
    pass

  @classmethod
  def RequestWeatherForecast(self) -> list:
    weather_params = {
      "lat"     : PR.RetrieveCurrentPosition()["lat"],
      "lon"     : PR.RetrieveCurrentPosition()["lon"],
      "exclude" : PR.RetrieveExcludeData(),
      "appid"   : PR.RetrieveApiKey()
    }
    api_endpoint = PR.RetrieveApiEndpoint()
    response = rq.get(api_endpoint, params=weather_params)
    response.raise_for_status()

    filtered_data = Filter.FilterWheaterForecast(response.json()["hourly"])
    forecast = list()
    for raw_weather_condition in filtered_data:
      forecast.append(Formatter.FormatWeatherCondition(raw_weather_condition))
    
    return forecast
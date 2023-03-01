import requests as rq
from ParametersReader import ParametersReader as PR

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

if __name__ == "__main__":
  ApiRequester.RequestWeatherForecast()

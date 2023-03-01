from ParametersReader import ParametersReader as PR

class ApiDataFilter:
  def __init__(self) -> None:
    pass

  @classmethod
  def FilterWheaterForecast(self, unfiltered_data: list) -> list:
    return unfiltered_data[:PR.RetrieveHoursRange()]
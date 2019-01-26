from termcolor import colored

from models.CachedHTTPRequest import CachedHTTPRequest
from models.Settings import Settings


class WeatherRequest:
    _ipRequest: CachedHTTPRequest = None
    _geocodeRequest: CachedHTTPRequest = None
    _weatherRequest: CachedHTTPRequest = None

    _ipRequestEndpointTemplate: str = "https://api.ipify.org?format=json"
    _geocodeEndpointTemplate: str = "http://ip-api.com/json/{ip}"
    _weatherEndpointTemplate: str = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}"

    def _getIPRequestEndpoint(self) -> str:
        return self._ipRequestEndpointTemplate

    def _getGeocodeEndpoint(self) -> str:
        return self._geocodeEndpointTemplate.format(
            ip=self._getIPRequest().json().get("ip")
        )

    def _getWeatherEndpoint(self) -> str:
        return self._weatherEndpointTemplate.format(
            lat=self._getGeocodeRequest().json().get("lat"),
            long=self._getGeocodeRequest().json().get("lon"),
            api_key=Settings.openWeatherMapsAPIKey
        )

    def _getIPRequest(self) -> CachedHTTPRequest:
        if self._ipRequest is None:
            self._ipRequest = CachedHTTPRequest(self._getIPRequestEndpoint())
        return self._ipRequest

    def _getGeocodeRequest(self) -> CachedHTTPRequest:
        if self._geocodeRequest is None:
            self._geocodeRequest = CachedHTTPRequest(self._getGeocodeEndpoint())
        return self._geocodeRequest

    def _getWeatherRequest(self) -> CachedHTTPRequest:
        if self._weatherRequest is None:
            self._weatherRequest = CachedHTTPRequest(self._getWeatherEndpoint())
        return self._weatherRequest

    def query(self) -> CachedHTTPRequest:
        return self._getWeatherRequest()

    def print(self) -> 'WeatherRequest':
        self.printLocation()
        self.printWeather()
        return self

    def printLocation(self) -> None:
        print(
            "Location: ", colored(self._getGeocodeRequest().json().get("city", "Unknown"), "blue"),
            "-", colored(self._getGeocodeRequest().json().get("country", "Unknown"), "blue"),
            "\t",
            "\t",
            "\t",
            "IP: ", colored(self._getIPRequest().json().get("ip", "Unknown"), "blue")
        )

    def printWeather(self) -> None:
        temperature: float = float(self._getWeatherRequest().json().get("main", {}).get("temp", 272.15)) - 272.15
        humidity: int = int(self._getWeatherRequest().json().get("main", {}).get("humidity", 0))

        print(
            "Temperature: ", colored("{0:.2f}°C".format(temperature), "blue" if temperature <= 0 else "red"),
            "\t",
            "Weather: ",
            ', '.join(colored(item['main'], "cyan") for item in self._getWeatherRequest().json().get("weather", [])),
            "\t",
            "Humidity: ", colored(str(humidity) + "%", "brown" if humidity <= 50 else "cyan"),
        )

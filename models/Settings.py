import os


class _Settings:
    cacheLocation: str = "/tmp/cached-weather/"
    cacheInvalidationPeriod: int = 60 * 15  # 15 minutes
    openWeatherMapsAPIKey: str = "NO_API_KEY_SET"

    def __init__(self):
        if 'CACHE_LOCATION' in os.environ:
            self.cacheLocation = os.environ.get('CACHE_LOCATION')
        if 'CACHE_INVALIDATION_PERIOD' in os.environ:
            self.cacheInvalidationPeriod = int(os.environ.get('CACHE_INVALIDATION_PERIOD'))
        if 'OPEN_WEATHER_MAPS_API_KEY' in os.environ:
            self.openWeatherMapsAPIKey = os.environ.get('OPEN_WEATHER_MAPS_API_KEY')


Settings = _Settings()

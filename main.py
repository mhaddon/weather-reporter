import threading

from models.CacheManager import CacheManager
from models.WeatherRequest import WeatherRequest

WeatherRequest().print()

threading.Thread(target=CacheManager.clearInvalidCacheEntries, args=())

import time

import base64
import os
import pickle
import stat

from models.Settings import Settings


class CacheManager:
    @staticmethod
    def clearInvalidCacheEntries() -> None:
        for cacheEntry in os.listdir(Settings.cacheLocation):
            cache = CacheManager(cacheEntry)
            if not cache.isCacheEntryValid():
                cache.clearCacheEntry()

    _name: str

    def __init__(self, path: str):
        self._name: str = path

    def getCacheName(self) -> str:
        return base64.b64encode(self._name.encode('utf-8')).decode('ascii').replace("/", "_")

    def getCacheAbsolutePath(self) -> str:
        return Settings.cacheLocation + self.getCacheName()

    def writeToCache(self, contents: object) -> None:
        if not os.path.isdir(Settings.cacheLocation):
            os.makedirs(Settings.cacheLocation)
        pickle.dump(contents, open(self.getCacheAbsolutePath(), "wb"))

    def loadFromCache(self) -> object:
        return pickle.load(open(self.getCacheAbsolutePath(), "rb"))

    def getCacheEntryAgeInSeconds(self) -> int:
        return time.time() - os.stat(self.getCacheAbsolutePath())[stat.ST_MTIME]

    def isCacheEntryValid(self) -> bool:
        return os.path.isfile(self.getCacheAbsolutePath()) and \
               self.getCacheEntryAgeInSeconds() < Settings.cacheInvalidationPeriod

    def clearCacheEntry(self) -> None:
        if os.path.isfile(self.getCacheAbsolutePath()):
            os.remove(self.getCacheAbsolutePath())

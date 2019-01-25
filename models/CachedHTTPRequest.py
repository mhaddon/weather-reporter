from models.CacheManager import CacheManager
from models.HTTPRequest import HTTPRequest


class CachedHTTPRequest(HTTPRequest):
    _cacheManager: CacheManager = None

    def __init__(self, url: str):
        super().__init__(url)
        self._cacheManager = CacheManager(url)

    def _getContents(self):
        if self._contents is None:
            if self._cacheManager.isCacheEntryValid():
                self._contents = self._cacheManager.loadFromCache()
            else:
                self._cacheManager.clearCacheEntry()
                self._cacheManager.writeToCache(super(CachedHTTPRequest, self)._getContents())

        return super(CachedHTTPRequest, self)._getContents()

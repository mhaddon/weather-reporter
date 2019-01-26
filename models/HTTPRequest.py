import requests
from json.decoder import JSONObject
from requests.models import Response


class HTTPRequest:

    _url: str
    _contents: Response = None
    _parsedJson: JSONObject = None

    def __init__(self, url: str):
        self._url: str = url

    def _getContents(self) -> Response:
        if self._contents is None:
            self._contents = requests.get(self._url, timeout=10)
            if not self._contents:
                raise Exception("An error occurred trying to query: %s" % self._url, self.getText())
        return self._contents

    def json(self) -> JSONObject:
        if self._parsedJson is None:
            self._parsedJson = self._getContents().json()
        return self._parsedJson

    def getStatusCode(self) -> int:
        return self._getContents().status_code

    def getText(self) -> str:
        return self._getContents().text

    def getEncoding(self) -> str:
        return self._getContents().encoding

    def getHeader(self, header: str) -> str:
        return self._getContents().headers[header]

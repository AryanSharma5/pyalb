class IServer:
    id: str
    url: str
    is_healthy: bool
    open_conns: int


class Server(IServer):
    def __init__(self, server_id: str, url: str, is_healthy: bool = True) -> None:
        self._id = server_id
        self._url = url
        self._is_healthy = is_healthy
        self._open_conns = 0

    @property
    def id(self) -> str:
        return self._id

    @property
    def url(self) -> str:
        return self._url

    @property
    def is_healthy(self) -> bool:
        return self._is_healthy

    @is_healthy.setter
    def is_healthy(self, value: bool) -> None:
        self._is_healthy = value

    @property
    def open_connections(self):
        return self._open_conns

    @open_connections.setter
    def open_connections(self, value: int):
        self._open_conns = value

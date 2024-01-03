import typing as t

server_health_status = t.Literal["OK", "KO"]


class IServer:
    id: str
    url: str
    health: bool


class Server(IServer):
    def __init__(
        self, server_id: str, url: str, health: server_health_status = "OK"
    ) -> None:
        self._id = server_id
        self._url = url
        self._health = health
        self._is_healthy = True

    @property
    def id(self) -> str:
        return self._id

    @property
    def url(self) -> str:
        return self._url

    @property
    def health(self) -> server_health_status:
        return self._health

    @health.setter
    def health(self, server_health: server_health_status) -> None:
        self._health = server_health
        self._is_healthy = True if self._health == "OK" else False

    @property
    def is_healthy(self) -> bool:
        return self._is_healthy

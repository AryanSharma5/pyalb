import typing as t
from itertools import cycle

from ..base import IRoutingStrategy
from ...server import IServer


class RoundRobbin(IRoutingStrategy):
    cycle_iter = None

    def __init__(self, servers: t.List[IServer]) -> None:
        self._servers = servers
        self.cycle_iter = cycle(self._servers)

    def route(self) -> IServer:
        server = self._get_next_server()
        print(f"request routed using {self.__class__.__name__} on {server}")
        return server

    def _get_next_server(self) -> IServer:
        return next(self.cycle_iter)

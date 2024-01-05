import typing as t

from ..base import IRoutingStrategy
from ...server import IServer


class LeastConnection(IRoutingStrategy):
    def __init__(self, servers: t.List[IServer]) -> None:
        self._servers = servers

    def route(self) -> IServer:
        server = self._get_least_conn_server(self._servers)
        server.open_connections += 1
        print(f"request routed using {self.__class__.__name__} on {server}")
        return server

    @staticmethod
    def _get_least_conn_server(servers: t.List[IServer]) -> IServer:
        least_conns, least_conn_server = float("inf"), None
        for server in servers:
            if server.open_connections < least_conns:
                least_conns = server.open_connections
                least_conn_server = server
        return least_conn_server

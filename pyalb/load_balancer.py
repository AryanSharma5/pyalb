from uuid import uuid4
import typing as t

from .server import IServer, Server
from .routing import RoutingContext, SUPPORTED_ROUTING_ALGORITHMS


class LoadBalancer:
    _servers: t.List[IServer] = None

    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port

    def register_servers(self, servers: t.List[IServer]) -> None:
        self._servers = [Server(server_id=uuid4(), url=server) for server in servers]
        print(f"servers registered: {self._servers}")

    def register_routing(self, routing_algorithm: str) -> None:
        self.routing_ctx = RoutingContext(
            routing_strategy=SUPPORTED_ROUTING_ALGORITHMS[routing_algorithm]
        )
        print(f"registered routing algorithm: {self.routing_ctx.routing_strategy}")

    def route(self) -> IServer:
        return self.routing_ctx.route(servers=self._servers)

    def run(self):
        print("running pyalb..")


def init_alb(host: str, port: int) -> LoadBalancer:
    return LoadBalancer(host=host, port=port)

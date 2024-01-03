import typing as t
from abc import ABC, abstractmethod

from ..server import IServer


class IRoutingStrategy(ABC):
    @abstractmethod
    def route(self, servers: t.List[IServer]) -> IServer:
        pass


class RoundRobbin(IRoutingStrategy):
    def route(self, servers: t.List[IServer]) -> IServer:
        print(f"request routed using {self.__class__.__name__} on {servers}")

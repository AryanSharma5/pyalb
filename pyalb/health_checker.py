import os
import time
import typing as t
from threading import Thread
from abc import ABC, abstractmethod

import requests
from .server import IServer


class IHealthChecker(ABC):
    @abstractmethod
    def start(self, servers: t.List[IServer]) -> None:
        """Implement this method to start your health checker service,
        which will health check on given list of servers"""


class HealthChecker(IHealthChecker):
    _health_check_daemon: Thread = None
    _unhealthy_servers: t.Set[IServer] = set()

    def __init__(self, healthcheck_endpoint: str) -> None:
        self._health_check_endpoint = "/" + healthcheck_endpoint

    def start(self, servers: t.List[IServer]) -> None:
        self._health_check_daemon = Thread(
            target=self._health_check,
            name="health check daemon",
            kwargs={"servers": servers},
            daemon=True,
        )
        self._health_check_daemon.start()

    def _health_check(self, servers: t.List[IServer]) -> None:
        while len(servers) != len(self._unhealthy_servers):
            # cold start and wait b/w consecutive health checks
            print(self._unhealthy_servers)
            time.sleep(10)
            for server in servers:
                try:
                    response = requests.get(
                        server.url + self._health_check_endpoint, timeout=3
                    )
                    response.raise_for_status()
                except (
                    requests.exceptions.ConnectionError,
                    requests.exceptions.HTTPError,
                ):
                    print(f"{server.url} server is unhealthy")
                    server.is_healthy = False
                    self._unhealthy_servers.add(server)
                else:
                    if not server.is_healthy:
                        server.is_healthy = True
                        self._unhealthy_servers.remove(server)
        self._terminate_pyalb()

    @staticmethod
    def _terminate_pyalb():
        print("No healthy server found. Shutting down pyalb!!")
        os._exit(0)

import argparse
import logging
import typing as t

from .routing.strategies import __all__

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def init_cli() -> t.Any:
    parser = argparse.ArgumentParser(
        prog="pyalb",
        description="An application load balancer",
        epilog="Thanks for using pyalb!",
    )
    parser.add_argument(
        "--servers",
        "-S",
        nargs="+",
        required=True,
        action="extend",
        dest="servers",
        help="list of backend server urls",
    )
    parser.add_argument(
        "--routing",
        "-R",
        type=str,
        default="RoundRobbin",
        dest="routing",
        choices=__all__,
        help="Routing algorithm to use [default: RoundRobbin]",
    )
    parser.add_argument(
        "--host",
        "-H",
        type=str,
        default="127.0.0.1",
        dest="host",
        help="host to use by pyalb [default: 127.0.0.1]",
    )
    parser.add_argument(
        "--port",
        "-P",
        type=str,
        default="5000",
        dest="port",
        help="port to use by pyalb [default: 5000]",
    )
    args = parser.parse_args()
    return args

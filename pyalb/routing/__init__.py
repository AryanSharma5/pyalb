import inspect

import pyalb.routing.routing_strategy as routing_strategy
from .routing_context import RoutingContext

SUPPORTED_ROUTING_ALGORITHMS = {
    cls.__name__: cls
    for _, cls in inspect.getmembers(routing_strategy, inspect.isclass)
    if issubclass(cls, routing_strategy.IRoutingStrategy)
}

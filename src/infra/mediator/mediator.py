from queue import Queue

from src.application.handler.handler import Handler
from src.domain.events.domain_event import DomainEvent


class Mediator:
    """is the responsible to publish and register the events"""

    def __init__(self) -> None:
        self.__handlers = Queue()

    def register(self, handler: Handler):
        """register evento into queue"""

        self.__handlers.put(handler)

    async def publish(self, event: DomainEvent):
        """run event handler"""

        for handler in list(self.__handlers.queue):
            if(handler.eventName == event.name):
                await handler.handle(event)

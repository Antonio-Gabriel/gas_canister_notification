from typing import List
from src.application.handler.handler import Handler
from src.domain.events.domain_event import DomainEvent

class Mediator:
    """is the responsible to publish and register the events"""

    def __init__(self) -> None:
        self.__handlers: List[Handler] = []

    def register(self, handler: Handler): 
        """register evento into queue"""

        self.__handlers.append(handler)

    async def publish(self, event: DomainEvent):
        """run event handler"""

        for handler in self.__handlers:
            if(handler.eventName == event.name):
                await handler.handle(event)

from abc import ABC, abstractproperty, abstractmethod

from src.domain.events.domain_event import DomainEvent

class Handler(ABC):
    """observe if the published event is in the queue"""    
    eventName: str = abstractproperty()

    @abstractmethod
    async def handle(self, event: DomainEvent):
        """event by domain name"""

        raise NotImplementedError("Method not implemented")

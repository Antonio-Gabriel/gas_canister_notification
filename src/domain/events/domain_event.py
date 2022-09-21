from abc import ABC, abstractproperty

class DomainEvent(ABC):
    """the base of events"""

    name: str = abstractproperty()

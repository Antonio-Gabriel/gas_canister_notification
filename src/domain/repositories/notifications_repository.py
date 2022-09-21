from typing import Type
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class ResidenceProps:
    """props of residence entity"""    
    owner: str
    contacts: list  
    building: int
    block: str

class INotificationsRepository(ABC):
    """repository for persist historic of notifications"""

    @abstractmethod
    async def register_notification(self, residence_props: Type[ResidenceProps]):
        """persist notifications history into storage"""

        raise NotImplementedError('Method not implemented')

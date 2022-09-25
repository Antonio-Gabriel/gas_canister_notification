from abc import ABC, abstractmethod

class IResidenceRepository(ABC):
    """repository for persist historic of notifications"""

    @abstractmethod
    async def find_by_residence(self, residence_id: int) -> list:
        """find by residence"""

        raise NotImplementedError('Method not implemented')

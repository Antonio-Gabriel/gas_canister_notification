from src.domain.repositories.residences_repository import IResidenceRepository

class ResidenceRepository(IResidenceRepository):
    """repository for persist historic of notifications"""

    def __init__(self) -> None:
        self.__residence: list = [
            {
                "id": 1,
                "building": 5,
                "owner": "Pedro Agostinho Múcua",
                "block": "7",
                "contacts": [923432333, 934543222]
            }
        ]
        
    async def find_by_residence(self, residence_id: int) -> list:
        """find by residence"""
        
        return list(filter(lambda residence: residence["id"] == residence_id[0], self.__residence))[0]

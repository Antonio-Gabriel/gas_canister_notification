from src.domain.entities.residence import Residence, ResidenceProps

class ResidenceAdapter:
    """adapter residence props"""

    @staticmethod
    def create(residence_id: int, owner: str, contacts: list, building: int, block: str):
        """create residence instance"""

        return Residence(
                residence_id,
                ResidenceProps(
                    owner=owner,
                    contacts=contacts,
                    building=building,
                    block=block
                )
            )

from typing import Type
from dataclasses import dataclass

@dataclass
class ResidenceProps:
    """props of residence entity"""    
    owner: str
    contacts: list  
    building: int
    block: str

class Residence:
    '''Residence entity'''

    def __init__(self, id_residence: int, props: Type[ResidenceProps]) -> None:
        self.id_residence = id_residence
        self.props = props

    @property
    def get_id(self):
        """return residence id"""
        return self.id_residence

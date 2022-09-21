from src.domain.entities.residence import Residence, ResidenceProps

def test_residence_entity():
    """shold be return a residence id"""

    residence = Residence(1, ResidenceProps(
        owner='António Gabriel',
        contacts=['+244987234554', '+244912434232'],
        building=46,
        block='24'
    ))
    assert residence.get_id is 1

from src.application.adapter.residence_adapter import ResidenceAdapter

def test_residence_adapter():
    """residence adapter"""

    residence = ResidenceAdapter.create(
        1, 'António Gabriel', [923345265, 9123445367], 30, '24'
        )

    assert residence.props.owner == 'António Gabriel'

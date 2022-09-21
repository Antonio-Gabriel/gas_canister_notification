from src.domain.entities.residence import Residence, ResidenceProps
from src.domain.events.notification_submitted_event import NotificationSubmittedEvent

def test_notification_event():
    """should be return the id of submitted event"""

    residence = Residence(1, ResidenceProps(
        owner='António Gabriel',
        contacts=['+244987234554', '+244912434232'],
        building=46,
        block='24'
    ))

    notification_submitted = NotificationSubmittedEvent(
        residence.get_id,
        ResidenceProps(
            owner='António Gabriel',
            contacts=['+244987234554', '+244912434232'],
            building=46,
            block='24'
        )
    )

    assert notification_submitted.get_notification_data['id_residence'][0] == residence.get_id

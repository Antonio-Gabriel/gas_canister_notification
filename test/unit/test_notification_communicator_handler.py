import asyncio

from src.infra.mediator.mediator import Mediator
from src.domain.entities.residence import Residence, ResidenceProps
from src.application.usecase.notification_submit_usecase import NotificationSubmittUseCase
from src.application.handler.notification_communicator_handler import NotificationCommunicatorHandler

def test_notification_communicator_handler():
    """testing the notification communicator handler"""

    mediator = Mediator()
    notification_handler = NotificationCommunicatorHandler(mediator=mediator)
    mediator.register(notification_handler)

    notification_usecase = NotificationSubmittUseCase(mediator=mediator)

    residence = Residence(1, ResidenceProps(
        owner='António Gabriel',
        contacts=['+244987234554', '+244912434232'],
        building=46,
        block='24'
    ))

    asyncio.run(notification_usecase.execute(residence=residence))

    assert 1 == 1

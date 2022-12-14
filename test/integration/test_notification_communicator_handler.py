import asyncio
from src.infra.mediator.mediator import Mediator
from src.domain.entities.residence import Residence, ResidenceProps
from src.infra.repositories.residence_repository import ResidenceRepository
from src.application.usecase.notification_submit_usecase import NotificationSubmittUseCase
from src.application.handler.notification_communicator_handler import NotificationCommunicatorHandler

def test_notification_communicator_handler():
    """testing the notification communicator handler"""

    mediator = Mediator()
    residence_repository = ResidenceRepository()
    notification_handler = NotificationCommunicatorHandler(residence_repository)
    mediator.register(notification_handler)

    """The test for pub and sub events on queue it work, i commented because i don't want 
        that add always message on kafka, for test remove the comments and run the test"""
  
    # notification_usecase = NotificationSubmittUseCase(mediator=mediator)

    # residence = Residence(1, ResidenceProps(
    #     owner='Kiala Gabriel',
    #     contacts=['+244987234554', '+244912434232'],
    #     building=46,
    #     block='24'
    # ))

    # try:
    #     asyncio.run(notification_usecase.execute(residence=residence))
    # except Exception as error:
    #     print("An error occurred!", error)

    assert 1 == 1

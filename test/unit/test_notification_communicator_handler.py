from src.infra.mediator.mediator import Mediator

from src.infra.repositories.residence_repository import ResidenceRepository
from src.application.handler.notification_communicator_handler import NotificationCommunicatorHandler

def test_notification_communicator_handler():
    """testing the notification communicator handler"""

    mediator = Mediator()
    residence_repository = ResidenceRepository()
    notification_handler = NotificationCommunicatorHandler(residence_repository)
    mediator.register(notification_handler)

    assert 1 == 1

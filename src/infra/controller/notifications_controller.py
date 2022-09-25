import asyncio

from typing import Type
from src.infra.mediator.mediator import Mediator
from src.application.adapter.residence_adapter import ResidenceAdapter
from src.infra.repositories.residence_repository import ResidenceRepository

from src.application.usecase.notification_submit_usecase import (
    NotificationSubmittUseCase
)
from src.application.handler.notification_communicator_handler import (
    NotificationCommunicatorHandler
)


class NotificationsController:
    """controller of notifications fluxe"""

    def handle(self, residence: Type[ResidenceAdapter]):
        """notifications handler"""

        mediator = Mediator()
        residence_repository = ResidenceRepository()
        notification_handler = NotificationCommunicatorHandler(residence_repository)
        mediator.register(notification_handler)

        notification_usecase = NotificationSubmittUseCase(mediator)
        asyncio.run(notification_usecase.execute(
            residence
        ))

from typing import Type
from src.infra.mediator.mediator import Mediator
from src.domain.entities.residence import Residence
from src.domain.events.notification_submitted_event import NotificationSubmittedEvent


class NotificationSubmittUseCase:
    """notify occurence usecase"""

    def __init__(self, mediator: Type[Mediator]) -> None:
        self.__mediator = mediator
    
    async def execute(self, residence: Type[Residence]):
        """run notification"""

        notify_event = NotificationSubmittedEvent(
            residence.get_id,
            residence.props
        )

        await self.__mediator.publish(event=notify_event)

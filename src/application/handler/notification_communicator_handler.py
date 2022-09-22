from typing import Type
from .handler import Handler
from src.infra.mediator.mediator import Mediator
from src.domain.events.notification_submitted_event import NotificationSubmittedEvent

class NotificationCommunicatorHandler(Handler):
    """handler for resolve notifications submitted events"""

    eventName: str = "NotificationSubmitted"

    def __init__(self, mediator: Type[Mediator]) -> None:
        self.__mediator = mediator

    async def handle(self, event: NotificationSubmittedEvent):
        """resolve the event"""

        # first i must to finding the residence that notify per problem
        # i need to notify on owner of residence after to agence        

        print(event)

        # notification_submitt_event = NotificationSubmittedEvent(
        #     event.id_residence[0],
        #     event.props
        # )

        # await self.__mediator.publish(notification_submitt_event)

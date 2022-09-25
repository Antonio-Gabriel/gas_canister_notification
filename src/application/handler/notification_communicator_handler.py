from typing import Type
from src.infra.messaging.kafka.kafka_producer import KafkaProducer
from src.domain.repositories.residences_repository import IResidenceRepository
from src.domain.events.notification_submitted_event import NotificationSubmittedEvent

from .handler import Handler

class NotificationCommunicatorHandler(Handler):
    """handler for resolve notifications submitted events"""

    eventName: str = "NotificationSubmitted"

    def __init__(self, residences_repository: Type[IResidenceRepository]) -> None:
        self.__residences_repository = residences_repository

    async def handle(self, event: NotificationSubmittedEvent):
        """resolve the event"""

        producer = KafkaProducer()
        residence = await self.__residences_repository.find_by_residence(event.id_residence)
        
        producer.send('gas_canister.new_notification', {
            "building": residence['building'],
            "owner": residence['owner'],
            "block": residence['block'],
            "contacts": residence['contacts']
        })

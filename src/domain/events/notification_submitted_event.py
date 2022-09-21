from typing import Type
from .domain_event import DomainEvent
from ..entities.residence import ResidenceProps

class NotificationSubmittedEvent(DomainEvent):
    """notify the user over the level of your gas"""

    name: str = "NotificationSubmitted"

    def __init__(self, id_residence: int, props: Type[ResidenceProps]) -> None:
        self.id_residence = id_residence,
        self.props = props

    @property
    def get_notification_data(self) -> dict:
        """return notified data"""

        return {
            "id_residence": self.id_residence,
            "props": self.props
        }


    def __str__(self) -> str:
        return f"NotificationSubmitted(id_residence={self.id_residence}, props={self.props})"

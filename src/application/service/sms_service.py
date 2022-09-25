from abc import ABC, abstractmethod

class Sms(ABC):
    """send sms to phone"""

    @abstractmethod
    async def send_sms(self, phone_number: str):
        """send to singular phone"""

        raise NotImplementedError('Method not implemented')

    @abstractmethod
    async def send_bulk_sms(self, phones: list):
        """send to phone list"""

        raise NotImplementedError('Method not implemented')

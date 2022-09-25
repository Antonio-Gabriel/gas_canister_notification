from src.application.service.sms_service import ISms

class SmsService(ISms):
    """sms service"""

    async def send_sms(self, phone_number: str):
        """send to singular phone"""

        raise NotImplementedError('Method not implemented')
   
    async def send_bulk_sms(self, phones: list):
        """send to phone list"""

        raise NotImplementedError('Method not implemented')

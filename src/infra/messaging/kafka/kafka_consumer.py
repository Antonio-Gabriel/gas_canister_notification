from json import loads
from kafka import KafkaConsumer as KafkaConsumerInstance

class KafkaConsumer:
    """consumer iterator"""
    
    def __init__(self) -> None:
        self.__consumer = KafkaConsumerInstance(            
            bootstrap_servers='localhost:9092',
            auto_offset_reset='latest',    
            enable_auto_commit=True,
            group_id='gas_canister_notify_group',
            value_deserializer=lambda x: loads(x.decode('utf-8'))       
            )
    
    @property
    def get_consumer_data(self):
        """return consumer data"""        

        return self.__consumer

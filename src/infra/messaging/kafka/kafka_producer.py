import json
from kafka import KafkaProducer as KafkaProducerInstance

class KafkaProducer:
    """asynchronous message producer"""
    
    def __init__(self) -> None:
        self.__producer = KafkaProducerInstance(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        
    def send(self, topic: str, body: dict):
        """send message to queue"""

        self.__producer.send(topic, body)

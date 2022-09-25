import json
from typing import Optional
from kafka import KafkaProducer as KafkaProducerInstance

class KafkaProducer:
    """asynchronous message producer"""
    
    def __init__(self, serializer: bool = True) -> None:
        self.__producer = KafkaProducerInstance(
            bootstrap_servers='localhost:9092',            
            value_serializer= (None if serializer is False else lambda v: json.dumps(v).encode('utf-8'))
        )

    def send(self, topic: str, body: Optional[dict]):
        """send message to queue"""

        self.__producer.send(topic, body)
        self.__producer.flush()

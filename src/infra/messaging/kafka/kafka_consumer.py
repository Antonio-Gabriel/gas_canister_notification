from kafka import KafkaConsumer as KafkaConsumerInstance

class KafkaConsumer:
    """consumer iterator"""
    
    def __init__(self, topic: str) -> None:
        self.__consumer = KafkaConsumerInstance(
            topic,
            bootstrap_servers='localhost:9092'            
        )
    
    @property
    def get_consumer_data(self):
        """return consumer data"""

        return self.__consumer

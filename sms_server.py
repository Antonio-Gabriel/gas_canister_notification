from src.infra.messaging.kafka.kafka_consumer import KafkaConsumer

_instance = KafkaConsumer()

consumer = _instance.get_consumer_data
consumer.subscribe(['gas_canister.new_notification'])

for msg in consumer:
    print(msg.value)

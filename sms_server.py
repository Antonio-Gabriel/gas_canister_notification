from src.infra.messaging.kafka.kafka_consumer import KafkaConsumer

_instance = KafkaConsumer()

consumer = _instance.get_consumer_data
consumer.subscribe(['gas_canister.new_notification'])

"""
    Here i will configure the rules for send sms to users inform that your gas just finish or
    that your gas have  little time to finish, you need to carrie her
"""

for msg in consumer:
    print(msg.value)

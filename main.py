from src.infra.messaging.kafka.kafka_producer import KafkaProducer

# gas_canister.new_notification

producer = KafkaProducer()
producer.send('gas_canister.new_notification', {
    'name': "Ag"
})

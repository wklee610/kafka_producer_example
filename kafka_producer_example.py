from kafka import KafkaProducer
import json
import logging
import datetime
import time
from datetime import datetime, timezone, timedelta

# Kafka Server Address
KAFKA_SERVERS = ['localhost:9092']

# Kafka Topic Name
KAFKA_TOPIC_NAME = ""

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Logger Setting
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Send Message function
def send_message_to_kafka(
    idx: int,
):
    try:
        data = {
            'idx': f"{idx}",
            'timestamp': datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M:%S"),
            'message': 'This is test message'
        }
        producer.send(KAFKA_TOPIC_NAME, data)
        logger.info(f"Log sent to kafka: {data}")
    except Exception as e:
        logger.error(f"Error sending log to kafka: {str(e)}")

if __name__ == "__main__":
    idx = 1
    while True:
        send_message_to_kafka(idx)
        idx += 1
        time.sleep(1)      # Use time.sleep(1) or similar to avoid overwhelming your Kafka broker with too many messages per second.

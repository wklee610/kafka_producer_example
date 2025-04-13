# kafka_producer_example

This project is a simple Python-based Kafka producer example.  
It generates and sends a message to a specified Kafka topic every second.

---

## Installation
Before use, you need to download `kafka-python`

```bash
pip install kafka-python
```

## Usage
Replace `kafka_servers` and `topic_name`

```python
KAFKA_SERVERS = ["localhost:9092"]        # Replace with your Kafka broker(s)
KAFKA_TOPIC_NAME = "your_topic_name"      # Replace with your Kafka topic
```

### Run
```bash
python kafka_producer_example.py
```

from kafka import KafkaProducer
import json
import logging
from config import KAFKA_CONFIG, TOPIC, logger

class UnigapProducer:
    def __init__(self):
        self.logger = logger
        self.producer = self._create_producer()
    
    def _create_producer(self):
        """Create and return a Kafka producer instance"""
        try:
            producer = KafkaProducer(
                **KAFKA_CONFIG,
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            self.logger.info("Producer created successfully")
            return producer
        except Exception as e:
            self.logger.error(f"Failed to create producer: {str(e)}")
            raise
    
    def send_message(self, topic, message):
        """Send a message to the specified topic"""
        try:
            future = self.producer.send(topic, message)
            # Wait for the message to be delivered
            record_metadata = future.get(timeout=10)
            self.logger.info(
                f"Message sent successfully to topic {topic}, "
                f"partition {record_metadata.partition}, "
                f"offset {record_metadata.offset}"
            )
            return True
        except Exception as e:
            self.logger.error(f"Failed to send message: {str(e)}")
            return False
    
    def close(self):
        """Close the producer connection"""
        try:
            self.producer.close()
            self.logger.info("Producer closed successfully")
        except Exception as e:
            self.logger.error(f"Error closing producer: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Create producer instance
    producer = UnigapProducer()
    
    try:
        # Example message
        message = {
            "product_id": "123",
            "user_id": "user_456",
            "timestamp": "2024-03-20T10:00:00Z"
        }
        
        # Send message
        producer.send_message(TOPIC, message)
        
    finally:
        # Always close the producer
        producer.close() 
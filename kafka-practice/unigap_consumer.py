from kafka import KafkaConsumer
import json
import logging
from typing import Callable, Optional
from config import KAFKA_CONFIG, TOPIC, logger

class UnigapConsumer:
    def __init__(self, group_id: str):
        self.group_id = group_id
        self.logger = logger
        self.consumer = self._create_consumer()
    
    def _create_consumer(self):
        """Create and return a Kafka consumer instance"""
        try:
            consumer = KafkaConsumer(
                **KAFKA_CONFIG,
                group_id=self.group_id,
                auto_offset_reset='earliest',
                enable_auto_commit=True,
                value_deserializer=lambda x: json.loads(x.decode('utf-8'))
            )
            self.logger.info(f"Consumer created successfully for group {self.group_id}")
            return consumer
        except Exception as e:
            self.logger.error(f"Failed to create consumer: {str(e)}")
            raise
    
    def consume_messages(self, topic: str, message_handler: Optional[Callable] = None):
        """
        Consume messages from the specified topic
        
        Args:
            topic: The topic to consume messages from
            message_handler: Optional callback function to handle messages
        """
        try:
            self.consumer.subscribe([topic])
            self.logger.info(f"Subscribed to topic: {topic}")
            
            while True:
                try:
                    # Poll for messages
                    messages = self.consumer.poll(timeout_ms=1000)
                    
                    for tp, msgs in messages.items():
                        for msg in msgs:
                            self.logger.info(
                                f"Received message from topic {msg.topic}, "
                                f"partition {msg.partition}, "
                                f"offset {msg.offset}: {msg.value}"
                            )
                            
                            # Call message handler if provided
                            if message_handler:
                                message_handler(msg.value)
                            
                except Exception as e:
                    self.logger.error(f"Error while consuming messages: {str(e)}")
                    continue
                    
        except KeyboardInterrupt:
            self.logger.info("Stopping consumer...")
        finally:
            self.close()
    
    def close(self):
        """Close the consumer connection"""
        try:
            self.consumer.close()
            self.logger.info("Consumer closed successfully")
        except Exception as e:
            self.logger.error(f"Error closing consumer: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Example message handler
    def handle_message(message):
        print(f"Processing message: {message}")
    
    # Create consumer instance
    consumer = UnigapConsumer(group_id="test-consumer-group")
    
    # Start consuming messages
    consumer.consume_messages(TOPIC, message_handler=handle_message) 
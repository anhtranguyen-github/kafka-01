import time
import threading
from unigap_producer import UnigapProducer
from unigap_consumer import UnigapConsumer
from config import TOPIC, logger

def test_single_consumer():
    logger.info("\n=== Testing Single Consumer Scenario ===")
    
    # Create producer
    producer = UnigapProducer()
    
    # Create consumer
    consumer = UnigapConsumer(group_id="single-consumer-group")
    
    # Start consumer in a separate thread
    def run_consumer():
        consumer.consume_messages(TOPIC)
    
    consumer_thread = threading.Thread(target=run_consumer)
    consumer_thread.daemon = True
    consumer_thread.start()
    
    # Send some test messages
    try:
        for i in range(5):
            message = {
                "product_id": f"prod_{i}",
                "user_id": f"user_{i}",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "scenario": "single_consumer"
            }
            producer.send_message(TOPIC, message)
            time.sleep(1)
    finally:
        producer.close()
        time.sleep(2)  # Wait for messages to be processed

def test_multiple_consumers():
    logger.info("\n=== Testing Multiple Consumers Scenario ===")
    
    # Create producer
    producer = UnigapProducer()
    
    # Create two consumers
    consumer1 = UnigapConsumer(group_id="multi-consumer-group")
    consumer2 = UnigapConsumer(group_id="multi-consumer-group")
    
    # Start consumers in separate threads
    def run_consumer1():
        consumer1.consume_messages(TOPIC)
    
    def run_consumer2():
        consumer2.consume_messages(TOPIC)
    
    consumer1_thread = threading.Thread(target=run_consumer1)
    consumer2_thread = threading.Thread(target=run_consumer2)
    
    consumer1_thread.daemon = True
    consumer2_thread.daemon = True
    
    consumer1_thread.start()
    consumer2_thread.start()
    
    # Send some test messages
    try:
        for i in range(10):
            message = {
                "product_id": f"prod_{i}",
                "user_id": f"user_{i}",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "scenario": "multiple_consumers"
            }
            producer.send_message(TOPIC, message)
            time.sleep(1)
    finally:
        producer.close()
        time.sleep(2)  # Wait for messages to be processed

if __name__ == "__main__":
    logger.info("Starting Kafka test scenarios...")
    
    # Test single consumer scenario
    test_single_consumer()
    
    # Wait a bit between scenarios
    time.sleep(5)
    
    # Test multiple consumers scenario
    test_multiple_consumers()
    
    logger.info("\nTest scenarios completed. Check the logs for message distribution.")
    logger.info("You can also check the consumer group information in the AKHQ interface.") 
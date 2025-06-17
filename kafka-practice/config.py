import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Kafka Configuration
KAFKA_CONFIG = {
    'bootstrap_servers': '46.202.167.130:9094,46.202.167.130:9194,46.202.167.130:9294',
    'security_protocol': 'SASL_PLAINTEXT',
    'sasl_mechanism': 'PLAIN',
    'sasl_plain_username': 'kafka',
    'sasl_plain_password': 'UnigapKafka@2024'
}

# Topic Configuration
TOPIC = 'product_view' 
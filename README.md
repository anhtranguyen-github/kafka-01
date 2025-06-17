
## 📂 Project Layout

```text
├── kafka-practice/         
│   ├── config.py            
│   ├── unigap_producer.py  
│   ├── unigap_consumer.py   
│   └── main.py       
│
├── bin/                     
├── libs/                   
├── config/                  
├── .gitignore               
└── README.md                
```


## 🚀 Quick Start

### 1. Clone & enter the repo
```bash
git clone https://github.com/anhtranguyen-github/kafka-01.git
cd kafka-01
```

### 2. Create a virtual environment & install dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r kafka-practice/requirements.txt
```

### 3. Configure broker connection (optional)
Edit `kafka-practice/config.py` and set:
* `bootstrap_servers`
* `security_protocol`, `sasl_mechanism`
* `sasl_plain_username`, `sasl_plain_password`

### 4. Send a test message
```bash
python kafka-practice/unigap_producer.py
```

### 5. Consume messages
Open another terminal window:
```bash
python kafka-practice/unigap_consumer.py
```

### 6. Run the demo scenarios
```bash
python kafka-practice/main.py
```
You will see logs illustrating how Kafka distributes messages across consumer instances.

#### 📋 Sample consumer output
```text
2025-06-17 13:37:42,581 - config - INFO - Received message from topic product_view, partition 0, offset 12156021:
{
  "_id": "5ecab65178aa7636ca41f58d",
  "time_stamp": 1749296185,
  "ip": "66.220.149.12",
  "user_agent": "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
  "resolution": "2000x2000",
  "user_id_db": "",
  "device_id": "cb702e6e-e2ef-4fd6-bd21-d96a67dfdd48",
  "api_version": "1.0",
  "store_id": "38",
  "local_time": "2025-06-07 18:36:25",
  "show_recommendation": null,
  "current_url": "https://www.glamira.ca/womens-ring-celtic-way.html?fbclid=IwAR0gvlgv1KvCc4DJbwgmaAdIl8UxIRv8P9YS_K8zFSJtcFlDtIkpQ9wEpJw&alloy=white_yellow-585",
  "referrer_url": "https://www.facebook.com/",
  "email_address": "",
  "recommendation": false,
  "utm_source": false,
  "utm_medium": false,
  "collection": "view_product_detail",
  "product_id": "90476",
  "option": [
    {
      "option_label": "alloy",
      "option_id": "108219",
      "value_label": "",
      "value_id": "791145"
    },
    {
      "option_label": "diamond",
      "option_id": "",
      "value_label": "",
      "value_id": ""
    }
  ],
  "id": "bbafc2a1-16c8-442b-bb2e-03df21059e45"
}
```

---

## 🧪 Running Kafka Locally (Optional)
The repository ships with a trimmed-down Kafka 3.0.0 KRaft distribution (in `bin/`, `libs/`, and `config/`).  To spin up a single-broker cluster:
```bash
# Format storage (first time only)
bin/kafka-storage.sh format -t $(uuidgen) -c config/kraft/server.properties

# Start broker
bin/kafka-server-start.sh config/kraft/server.properties
```
The broker listens on `localhost:9092`.  Update `bootstrap_servers` accordingly.

> NOTE: The above scripts require Java 11+ in your `PATH`.

---

## ⚙️ Customisation
* **Topic name** – set the `TOPIC` constant in `config.py`.
* **Message schema** – modify the JSON object in `unigap_producer.py` and adapt handling in `unigap_consumer.py`.
* **Consumer group** – change the `group_id` when instantiating `UnigapConsumer`.


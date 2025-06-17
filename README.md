
## 📂 Project Layout

```text
.
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
python kafka-practice/test_kafka.py
```
You will see logs illustrating how Kafka distributes messages across consumer instances.

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

---

## 🤝 Contributing
Pull requests are welcome!  Feel free to open issues for suggestions or bugs.

---

## 📖 References
* [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
* [kafka-python Library](https://github.com/dpkp/kafka-python)
* [AKHQ – Kafka Web UI](https://akhq.io/)

---

## 📝 License

Distributed under the **Apache 2.0 License**.  See `LICENSE` for more information. 
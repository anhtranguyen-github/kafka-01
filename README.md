### 📂 Project Structure

```
.
├── kafka-practice/          # Python source code (producer, consumer, tests)
│   ├── config.py            # Centralised Kafka & topic settings
│   ├── unigap_producer.py   # Producer wrapper around kafka-python
│   ├── unigap_consumer.py   # Consumer wrapper around kafka-python
│   └── test_kafka.py        # Demo script that launches sample scenarios
│
├── bin/                     # Convenience shell scripts from the Kafka distribution
├── config/                  # Kafka KRaft mode configuration (if you want to run Kafka locally)
├── libs/                    # JARs required to run the vanilla Kafka distribution (optional)
└── requirements.txt         # Python dependencies for the examples
```

---

### 🛠 Prerequisites

* Python **3.8+** (any modern 3.x release will work)
* An accessible Kafka cluster (public or local)
  * The default settings in `kafka-practice/config.py` point at a remote **SASL_PLAINTEXT** cluster.  Update them to match your own environment.
* `git`, `make`, or equivalent tooling if you plan to extend the repository

> **Running Kafka locally?**  The `config/kraft` folder plus the content of `bin/` and `libs/` is a trimmed-down Kafka 3.0.0 distribution.  You can start a single-node broker with:
>
> ```bash
> bin/kafka-storage.sh format -t $(uuidgen) -c config/kraft/server.properties
> bin/kafka-server-start.sh config/kraft/server.properties
> ```
> 
> You will need Java 11+ on your path for the above to work.

---

### 🚀 Quick Start

1. **Clone** the repository and enter the directory

   ```bash
   git clone <repo-url>
   cd kafka-learn
   ```

2. **Create a virtualenv** and install Python dependencies

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r kafka-practice/requirements.txt
   ```

3. **Configure** your broker connection (optional).  Edit `kafka-practice/config.py` and set:

   * `bootstrap_servers`
   * `security_protocol`, `sasl_mechanism`, `sasl_plain_username`, `sasl_plain_password`

4. **Run the producer example**

   ```bash
   python kafka-practice/unigap_producer.py
   ```

5. **Run the consumer example** in another terminal window to see incoming messages

   ```bash
   python kafka-practice/unigap_consumer.py
   ```

6. **Try the test scenarios** which spin up producers & multiple consumers automatically:

   ```bash
   python kafka-practice/test_kafka.py
   ```

---

### 🧩 Customising the Examples

* **Topic name** – change the constant `TOPIC` in `kafka-practice/config.py`.
* **Message format** – update the JSON payload in `unigap_producer.py` or handle the value in `unigap_consumer.py`.
* **Consumer group** – pass a different `group_id` when instantiating `UnigapConsumer`.

---

### 📖 Helpful Resources

* [Apache Kafka documentation](https://kafka.apache.org/documentation/)
* [kafka-python project](https://github.com/dpkp/kafka-python)
* [AKHQ – Web UI for Kafka](https://akhq.io/)  (handy for observing topics & consumer groups)

---

### 📝 License

This repository is provided under the **Apache 2.0 License**.  See `LICENSE` for details. 
# 🐍 Py App
By Anthony Vilarim Caliani

![#](https://img.shields.io/badge/license-MIT-blue.svg) ![#](https://img.shields.io/badge/python-3.8.x-yellow.svg)

## Quick Start
```sh
# Initializing Virtual Env
python3 -m venv .venv \
    && source .venv/bin/activate \
    && pip install -r requirements.txt

# Kafka Producer
python producer.py

# In another terminal execute "kafka consumer"
# Don't forget to activate python venv before running ;)
python consumer.py
```

Now, keep your eyes on application console because everything will be logged 😉

## Related Links
- [Kafka Python Docs: Usage](https://kafka-python.readthedocs.io/en/master/usage.html)

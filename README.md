## Running Locally

```The easiest way to install Celery is using pip:
pip install Celery
```

```bash
git clone https://github.com/djsaeedkhan/django-celery-random-number.git
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

```bash
celery -A test1 worker -l info
```

Make sure you have RabbitMQ service running.

```bash
rabbitmq-server
```

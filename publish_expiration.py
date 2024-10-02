import pika
import json

# Configuración de credenciales de RabbitMQ
credentials = pika.PlainCredentials('inventimax', 'inventimax')  # Reemplaza con tus credenciales

def publish_expiration_event(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange='expiration_events', exchange_type='fanout')

    message = json.dumps(data)
    channel.basic_publish(exchange='expiration_events', routing_key='', body=message)

    print(" [x] Sent expiration event")
    connection.close()

publish_expiration_event({"product": "huevos", "expiration_date": "2025-10-01"})

import pika
import json

# Configuración de credenciales de RabbitMQ
credentials = pika.PlainCredentials('inventimax', 'inventimax')

def publish_promotion_event(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange='promotion_events', exchange_type='fanout')

    message = json.dumps(data)
    channel.basic_publish(exchange='promotion_events', routing_key='', body=message)

    print(" [x] Sent promotion event")
    connection.close()

publish_promotion_event({"product": "Pan", "promotion": "50% descuento"})

import pika
import json

# Configuración de credenciales de RabbitMQ
credentials = pika.PlainCredentials('inventimax', 'inventimax')

def publish_redistribution_event(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
    channel = connection.channel()

    # Declarar el exchange para eventos de redistribución
    channel.exchange_declare(exchange='redistribution_events', exchange_type='fanout')

    message = json.dumps(data)
    channel.basic_publish(exchange='redistribution_events', routing_key='', body=message)

    print(" [x] Sent redistribution event")
    connection.close()

# Ejemplo de publicación de evento de redistribución
publish_redistribution_event({"product": "Pan", "location_from": "Bodega A", "location_to": "Bodega B"})

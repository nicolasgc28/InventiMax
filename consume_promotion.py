import pika
import json

# Configuración de credenciales de RabbitMQ
credentials = pika.PlainCredentials('inventimax', 'inventimax')

def callback(ch, method, properties, body):
    event = json.loads(body)
    print(f" [x] Received promotion event: {event}")

def consume_promotion_events():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange='promotion_events', exchange_type='fanout')
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='promotion_events', queue=queue_name)

    print(' [*] Waiting for promotion events. To exit press CTRL+C')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

consume_promotion_events()

import pika
import json

# Configuración de credenciales de RabbitMQ
credentials = pika.PlainCredentials('inventimax', 'inventimax')  # Reemplaza 'usuario' y 'contraseña' con las credenciales correctas

# Conexión a RabbitMQ con credenciales

def publish_report_event(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
    channel = connection.channel()


    channel.exchange_declare(exchange='report_events', exchange_type='fanout')

    message = json.dumps(data)
    channel.basic_publish(exchange='report_events', routing_key='', body=message)

    print(" [x] Sent report event")
    connection.close()

publish_report_event({"event": "inventory_update", "details": "Productos actualizados en bodega A"})

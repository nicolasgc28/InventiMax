import pika
import json

# Configuración de credenciales de RabbitMQ
credentials = pika.PlainCredentials('inventimax', 'inventimax')

def callback(ch, method, properties, body):
    # Decodifica el mensaje recibido
    event = json.loads(body)
    print(f" [x] Received report event: {event}")
    # Aquí puedes agregar lógica adicional, como generar el reporte con los datos recibidos

def consume_report_events():
    try:
        # Conexión con RabbitMQ usando credenciales personalizadas
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
        channel = connection.channel()

        # Declara el exchange y conecta la cola al exchange
        channel.exchange_declare(exchange='report_events', exchange_type='fanout')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        # Vincula la cola al exchange de reportes
        channel.queue_bind(exchange='report_events', queue=queue_name)

        print(' [*] Waiting for report events. To exit press CTRL+C')

        # Configura el consumo de mensajes y mantén la conexión "activa"
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()

    except pika.exceptions.AMQPConnectionError as e:
        print(f"Error connecting to RabbitMQ: {e}")
        connection.close()

if __name__ == "__main__":
    consume_report_events()

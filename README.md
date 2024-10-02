# Sistema de Mensajería Asíncrona para Inventario y Promociones

Este proyecto utiliza **RabbitMQ** para implementar un sistema de mensajería asíncrona que facilita la gestión de inventario, seguimiento de fechas de caducidad, redistribución de productos y generación de promociones de ventas en un entorno de retail.

## Descripción del Proyecto

El sistema utiliza un patrón de mensajería asíncrona basado en **RabbitMQ** con un modelo de publicador-suscriptor, diseñado para administrar de manera eficiente:
- Generación y envío de reportes de inventario.
- Seguimiento y notificación de fechas de caducidad de productos.
- Redistribución de inventario entre diferentes ubicaciones.
- Generación y aplicación de promociones de ventas.

## Componentes Clave

- **Generación de Reportes**: Publica y consume eventos relacionados con actualizaciones del inventario.
- **Seguimiento de Caducidad**: Envía y recibe eventos sobre fechas de vencimiento de productos.
- **Redistribución de Inventario**: Publica y consume eventos para la transferencia de productos entre ubicaciones.
- **Generación de Promociones**: Gestiona eventos para crear promociones que incentiven las ventas.

## Flujo de Trabajo del Sistema

1. Publicador de reportes envía eventos de actualización de inventario.
2. Publicador de fechas de caducidad notifica productos próximos a vencerse.
3. Publicador de promociones envía eventos con detalles de descuentos para ventas.
4. Suscriptores reciben estos eventos y toman acciones para ajustar el inventario, generar reportes y aplicar promociones.

## Tecnologías Utilizadas

- **RabbitMQ**: Sistema de mensajería para la comunicación asíncrona.
- **Python (Pika)**: Librería para conectar y gestionar eventos de RabbitMQ.

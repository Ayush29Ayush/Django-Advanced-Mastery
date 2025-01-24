import pika
import json


def publish_message(data):
    # Convert the Python object to a JSON string once
    data_json = json.dumps(data)

    # Setup RabbitMQ connection and publish the message
    params = pika.URLParameters(
        "amqps://gwnqkeqo:8IT2tus9p512mHCPcAfhhILXmAaafQcZ@rabbit.lmq.cloudamqp.com/gwnqkeqo"
    )
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue="my_queue")

    # Send the JSON string to RabbitMQ
    channel.basic_publish(exchange="", routing_key="my_queue", body=data_json)
    print(f"Message published: {data_json}")

    # Close the connection
    connection.close()

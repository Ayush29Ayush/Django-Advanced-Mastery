import pika
import pandas as pd
import json
import uuid


def generateExcel(message):
    message = json.loads(message)
    names = message["names"]
    df = pd.DataFrame(names)
    df.to_excel(f"output_{uuid.uuid4()}.xlsx", index=False)


def callback(ch, method, properties, body):
    message = body.decode()
    print(message)
    generateExcel(message)


params = pika.URLParameters(
    "amqps://gwnqkeqo:8IT2tus9p512mHCPcAfhhILXmAaafQcZ@rabbit.lmq.cloudamqp.com/gwnqkeqo"
)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue="my_queue")
channel.basic_consume(queue="my_queue", on_message_callback=callback, auto_ack=True)
print("\n" + "---------------------Consumer Started---------------------" + "\n")
channel.start_consuming()

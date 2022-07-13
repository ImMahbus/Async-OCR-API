from multiprocessing import connection
import queue
import pika
import time
import ocr_engine
import json
import databases.database as db

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue = 'task_queue', durable = True)

def callback(ch, method, properties, body):
    task_info = body.decode()
    id = task_info[0:20]
    image_data = task_info[20:]
    db.sent_to_ocr_engine(id)
    data = ocr_engine.b64string_to_text(id, image_data)
    db.add_to_db(id, data)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback = callback)
channel.start_consuming()
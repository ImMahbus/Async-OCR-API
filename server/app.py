from concurrent.futures import thread
from email import message
from http import client
import json
from multiprocessing import connection
from flask import Flask, jsonify, request
import importlib
import shortuuid as uuid
import pika
import databases.database as db

app = Flask(__name__)

@app.route("/image/", methods=["POST"])
def read_text():
    image_info = request.get_json()
    id = str(uuid.ShortUUID().random(length=20))
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    message = id+str(image_info["image_data"])
    db.added_to_queue(id)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body = message,
        properties=pika.BasicProperties(
            delivery_mode=2, 
        )
    )
    connection.close()
    
    return jsonify({"task_id": id})


@app.route("/image/", methods=["GET"])
def get_text():
    task_info = request.get_json()
    data = db.find_by_id(str(task_info["task_id"]))
    return jsonify({
        "task_id": data["task_id"],
        "recognized_text": data["recognized_text"],
        "status":data["status"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, threaded=True)

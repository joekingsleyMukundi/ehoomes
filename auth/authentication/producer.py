import pika, json, os
from dotenv import load_dotenv
load_dotenv()
# package to help send events
params = pika.URLParameters(os.getenv('RABBITMQURLPARAMS'))
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
  properties = pika.BasicProperties(method)
  channel.basic_publish(exchange='',routing_key='auth',body=json.dump(body), properties=properties)
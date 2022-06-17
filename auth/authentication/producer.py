import pika, json, os
from dotenv import load_dotenv
load_dotenv()
# package to help send events
params = pika.URLParameters('amqps://nqsdtgdi:CBnX14b-56LW_49P7SFMRudTTAFg8keX@rat.rmq2.cloudamqp.com/nqsdtgdi')
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
  properties = pika.BasicProperties(method)
  channel.basic_publish(exchange='',routing_key='auth',body=json.dump(body), properties=properties)
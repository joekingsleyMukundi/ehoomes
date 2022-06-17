import pika, json, os
from dotenv import load_dotenv
load_dotenv()
# package to help consume events
params = pika.URLParameters(os.getenv('RABBITMQURLPARAMS'))
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue = 'admin')

def callback(ch, method, properties, body):
  print('messge recived in auth')
  print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)
print('started consuming')
channel.start_consuming()
channel.close()
import pika
# package to help send events
params = pika.URLParameters('amqps://nqsdtgdi:CBnX14b-56LW_49P7SFMRudTTAFg8keX@rat.rmq2.cloudamqp.com/nqsdtgdi')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue = 'auth')

def callback(ch, method, properties, body):
  print('messge recived in consumer')
  print(body)

channel.basic_consume(queue='auth', on_message_callback=callback, auto_ack=True)
print('started consuming')
channel.start_consuming()
channel.close()
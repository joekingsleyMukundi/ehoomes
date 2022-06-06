import pika
# package to help send events
params = pika.URLParameters('amqps://nqsdtgdi:CBnX14b-56LW_49P7SFMRudTTAFg8keX@rat.rmq2.cloudamqp.com/nqsdtgdi')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue = 'admin')

def callback(ch, method, properties, body):
  print('messge recived in admin')
  print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)
print('started consuming')
channel.start_consuming()
channel.close()
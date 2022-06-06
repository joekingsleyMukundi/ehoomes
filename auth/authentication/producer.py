import pika
# package to help send events
params = pika.URLParameters('amqps://nqsdtgdi:CBnX14b-56LW_49P7SFMRudTTAFg8keX@rat.rmq2.cloudamqp.com/nqsdtgdi')
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish():
  channel.basic_publish(exchange='',routing_key='admin',body='hello')
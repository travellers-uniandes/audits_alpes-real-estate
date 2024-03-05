from pulsar import Client

pulsar_url = "pulsar://localhost:6650"
topic_name = "persistent://public/default/audit-events"

client = Client(pulsar_url)
producer = client.create_producer(topic_name)

try:
    mensaje = "Hola, esto es un mensaje de ejemplo"
    producer.send(mensaje.encode('utf-8'))
except Exception as e:
    print("Error:", str(e))

finally:
    producer.close()
    client.close()

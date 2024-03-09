import json
import pulsar
from app.seedwork.infrastructure import utils
import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


class Despachador:
    def publicar_evento(self, evento, topico):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico)
        serialized_data = json.dumps(evento.data).encode('utf-8')
        publicador.send(serialized_data)
        publicador.close()

    def publicar_comando(self, comando, topico):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico)
        serialized_data = json.dumps(comando.data).encode('utf-8')
        publicador.send(serialized_data)
        publicador.close()

import pulsar, _pulsar
from pulsar.schema import *
import logging
import traceback
from app.moduls.audits.infrastructure.schema.v1.events import EventoReservaCreada
from app.moduls.audits.infrastructure.schema.v1.commands import ComandoCrearReserva
from app.seedwork.infrastructure import utils


def suscribirse_a_eventos():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('eventos-reserva', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='aeroalpes-sub-eventos',
                                       schema=AvroSchema(EventoReservaCreada))

        while True:
            mensaje = consumer.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            consumer.acknowledge(mensaje)

        client.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if client:
            client.close()


def suscribirse_a_comandos():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('comandos-reserva', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='aeroalpes-sub-comandos',
                                       schema=AvroSchema(ComandoCrearReserva))

        while True:
            mensaje = consumer.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumer.acknowledge(mensaje)

        client.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if client:
            client.close()

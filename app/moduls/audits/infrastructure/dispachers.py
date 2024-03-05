import pulsar
from pulsar.schema import *
from app.moduls.audits.infrastructure.schema.v1.events import EventoReservaCreada, ReservaCreadaPayload
from app.moduls.audits.infrastructure.schema.v1.commands import ComandoCrearReserva, ComandoCrearReservaPayload
from app.seedwork.infrastructure import utils
import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


class Despachador:
    def _publicar_mensaje(self, mensaje, topico):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoReservaCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = ReservaCreadaPayload(
            id_reserva=str(evento.id_reserva),
            id_cliente=str(evento.id_cliente),
            estado=str(evento.estado),
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = EventoReservaCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoReservaCreada))

    def publicar_comando(self, comando, topico):
        payload = ComandoCrearReservaPayload(
            id_usuario=str(comando.id_usuario)
        )
        comando_integracion = ComandoCrearReserva(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearReserva))

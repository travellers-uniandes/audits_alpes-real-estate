from app.modules.audits.aplication.commands.delete_audit import DeleteAudit
from app.modules.audits.aplication.mappers import MapperAuditDTOJson as MapApp
from app.modules.audits.aplication.commands.create_audit import CreateAudit
from app.seedwork.aplication.commands import execute_command
from app.modules.audits.infrastructure.dispachers import Despachador
from app.seedwork.infrastructure import utils
import pulsar
from app.seedwork.infrastructure.schema.v1.comandos import CommandResponseCreateAuditJson, \
    CommandResponseRollbackCreateAuditJson


def suscribe_create_command(app):
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('create-audit', consumer_type=pulsar.ConsumerType.Shared,
                                    subscription_name='audit-sub-commands')

        while True:
            message = consumer.receive()
            print("Mensaje recibido: {}".format(message.data().decode('utf-8')))

            with app.test_request_context():
                audit_dict = get_info()
                map_audit = MapApp()
                audit_dto = map_audit.external_to_dto(audit_dict)
                error = False
                if error:
                    despachador = Despachador()
                    command = CommandResponseRollbackCreateAuditJson()
                    command.data = str(-1)
                    despachador.publicar_comando_rollback(command, 'response-rollback-create-audit')
                else:
                    command = CreateAudit(audit_dto)
                    execute_command(command)
                    despachador = Despachador()
                    command = CommandResponseCreateAuditJson()
                    command.data = str(-1)
                    despachador.publicar_comando_respuesta(command, 'response-create-audit')

            consumer.acknowledge(message)

        client.close()
    except Exception as e:
        despachador = Despachador()
        command = CommandResponseRollbackCreateAuditJson()

        command.data = str(-1)
        despachador.publicar_comando_rollback(command, 'response-rollback-create-audit')

        print(e)
        print('ERROR: Suscribiéndose al tópico de comandos!')
    finally:
        if client:
            client.close()


def get_info():
    audit_dict = {
        "location_id": "5a9d0736-11b6-4854-98e4-a297027cfdd9",
        "code": "1a",
        "score": 90,
        "approved_audit": True
    }
    return audit_dict


def suscribe_delete_command(app):
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('delete-audit', consumer_type=pulsar.ConsumerType.Shared,
                                    subscription_name='audit-sub-commands')

        while True:
            mensaje = consumer.receive()
            print("Mensaje recibido: {}".format(mensaje.data().decode('utf-8')))

            with app.test_request_context():
                audit_id = -1
                command = DeleteAudit(audit_id)
                execute_command(command)

                despachador = Despachador()
                command = CommandResponseRollbackCreateAuditJson()

                command.data = str(-1)
                despachador.publicar_comando(command, 'response-rollback-create-audit')
            consumer.acknowledge(mensaje)

        client.close()
    except Exception as e:
        print(e)
        print('ERROR: Suscribiéndose al tópico de comandos!')
    finally:
        if client:
            client.close()

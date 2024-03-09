import json
import uuid
from flask import Flask
from app.moduls.audits.infrastructure.dispachers import Despachador
from app.moduls.audits.infrastructure.dto import Audit
from app.seedwork.infrastructure import utils
import pulsar
from app.config.db import init_db
from app.seedwork.infrastructure.schema.v1.commands import CommandResponseCreateAuditJson, \
    CommandResponseRollbackCreateAuditJson
from config import Setting

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = Setting.DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
app.config['SESSION_TYPE'] = 'filesystem'
init_db(app)
from app.config.db import db


def suscribirse_a_comandos():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('create-audit', consumer_type=pulsar.ConsumerType.Shared,
                                    subscription_name='audit-sub-commands')

        while True:
            mensaje = consumer.receive()
            print("Mensaje recibido: {}".format(mensaje.data().decode('utf-8')))
            with app.app_context():
                db.create_all()
                print(f"Current app name: {app.name}")
                entity = Audit()
                entity.id = str(uuid.uuid4())
                entity.location_id = 1
                entity.code = "name"
                entity.score = 1
                entity_id_json = json.dumps({"id": entity.id})
                db.session.add(entity)
                db.session.commit()
                db.session.close()

                despachador = Despachador()
                command = CommandResponseCreateAuditJson()

                command.data = entity_id_json
                despachador.publicar_comando(command, 'response-create-audit')

            consumer.acknowledge(mensaje)

        client.close()
    except Exception as e:
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
    finally:
        if client:
            client.close()


def suscribirse_a_comandos_delete():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('delete-audit', consumer_type=pulsar.ConsumerType.Shared,
                                    subscription_name='audit-sub-commands')

        while True:
            mensaje = consumer.receive()
            print("Mensaje recibido: {}".format(mensaje.data().decode('utf-8')))
            with app.app_context():
                db.create_all()
                print(f"Current app name: {app.name}")
                json_data = json.loads(mensaje.data().decode('utf-8'))
                id_value = json_data.get("id")

                db.session.query(Audit).filter(Audit.id == id_value).delete()
                db.session.commit()
                db.session.close()

                despachador = Despachador()
                command = CommandResponseRollbackCreateAuditJson()

                command.data = id_value
                despachador.publicar_comando(command, 'response-rollback-create-audit')

            consumer.acknowledge(mensaje)

        client.close()
    except Exception as e:
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
    finally:
        if client:
            client.close()

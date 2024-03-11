import json
import uuid
from flask import Flask
from app.modules.audits.infrastructure.dispachers import Despachador
from app.modules.audits.infrastructure.dto import Audit, Location
from app.seedwork.infrastructure import utils
import pulsar,_pulsar  
from pulsar.schema import *
from app.config.db import init_db
from app.seedwork.infrastructure.schema.v1.comandos import CommandResponseCreateAuditJson, CommandResponseRollbackCreateAuditJson
from config import Setting
#from app.moduls.audits.infrastructure.dto

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
            consumer.acknowledge(mensaje)

            with app.app_context():
                print(f"Current app name: {app.name}")
                
                error = False
                if error:
                    despachador = Despachador()
                    command = CommandResponseRollbackCreateAuditJson()
                    command.data = "Rollback"
                    despachador.publicar_comando_rollback(command, 'response-rollback-create-audit')
                else:
                    db.create_all()
                    
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
                    command.data = str(-1)              
                    despachador.publicar_comando_respuesta(command, 'response-create-audit')

            consumer.acknowledge(mensaje)

        client.close()
    except Exception as e:
        despachador = Despachador()
        command = CommandResponseRollbackCreateAuditJson()

        command.data = str(-1)
        despachador.publicar_comando_rollback(command, 'response-rollback-create-audit')

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

                latest_audit = db.session.query(Audit).order_by(Audit.id.desc()).first()
                if latest_audit:
                    latest_audit_id = latest_audit.id
                    db.session.query(Audit).filter(Audit.id == latest_audit_id).delete()
                    db.session.commit()
                db.session.close()

                despachador = Despachador()
                command = CommandResponseRollbackCreateAuditJson()
                
                command.data =  str(-1)              
                despachador.publicar_comando(command, 'response-rollback-create-audit')

            consumer.acknowledge(mensaje)

        client.close()
    except Exception as e:
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
    finally:
        if client:
            client.close()

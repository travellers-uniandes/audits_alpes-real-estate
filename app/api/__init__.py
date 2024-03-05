import os
from flask import Flask
from config import settings

basedir = os.path.abspath(os.path.dirname(__file__))


def registrar_handlers():
    ...


def importar_modelos_alchemy():
    ...


def comenzar_consumidor():
    """
    Este es un código de ejemplo. Aunque esto sea funcional puede ser un poco peligroso tener 
    threads corriendo por si solos. Mi sugerencia es en estos casos usar un verdadero manejador
    de procesos y threads como Celery.
    """
    import app.moduls.audits.infrastructure.consumers as list_consumer
    import threading

    # Suscripción a eventos
    threading.Thread(target=list_consumer.suscribirse_a_eventos).start()

    # Suscripción a comandos
    threading.Thread(target=list_consumer.suscribirse_a_comandos).start()


def create_app(configuracion={}):
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

    from app.config.db import init_db
    init_db(app)

    from app.config.db import db
    from . import audit_router
    importar_modelos_alchemy()
    registrar_handlers()

    with app.app_context():
        db.create_all()
        comenzar_consumidor()

    app.register_blueprint(audit_router.bp)

    @app.route("/")
    def health():
        return {"status": "up"}

    return app
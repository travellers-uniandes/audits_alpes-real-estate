import os
from flask import Flask
from config import settings

basedir = os.path.abspath(os.path.dirname(__file__))


def register_handlers():
    import app.modules.audits.aplication


def import_models_alchemy():
    import app.modules.audits.infrastructure.dto


def start_consumers(app):
    import app.modules.audits.infrastructure.consumers as consumers
    import threading

    # Subscription to commands
    threading.Thread(target=consumers.suscribe_create_command, args=[app]).start()
    threading.Thread(target=consumers.suscribe_delete_command, args=[app]).start()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'

    from app.config.db import init_db, db
    init_db(app)

    from . import audit_router
    import_models_alchemy()
    register_handlers()

    with app.app_context():
        db.create_all()
        start_consumers(app)

    app.register_blueprint(audit_router.bp)

    @app.route("/")
    def health():
        return {"status": "up"}

    return app

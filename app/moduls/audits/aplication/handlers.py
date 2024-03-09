from app.seedwork.aplication.handlers import Handler
from app.moduls.audits.infrastructure.dispachers import Despachador


class HandlerAuditIntegration(Handler):
    @staticmethod
    def handle_audit_created(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'response-audit')

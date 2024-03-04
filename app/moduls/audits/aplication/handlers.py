from app.seedwork.aplication.handlers import Handler
from app.moduls.audits.infrastructure.dispachers import Despachador


class HandlerAuditIntegration(Handler):
    @staticmethod
    def handle_audit_created(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-audit')

    @staticmethod
    def handle_audit_canceled(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-audit')

    @staticmethod
    def handle_audit_approved(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-audit')

    @staticmethod
    def handle_audit_paid(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-audit')

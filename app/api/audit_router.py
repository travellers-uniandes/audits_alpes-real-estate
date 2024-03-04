import app.seedwork.presentation.apiflask as apiflask
import json
from flask import request
from flask import Response
from app.moduls.audits.aplication.querys.get_states import GetEstate
from app.moduls.audits.aplication.services import AuditService
from app.moduls.audits.aplication.mappers import MapperAuditDTOJson as MapApp
from app.moduls.audits.aplication.commands.create_estate import CreateEstate
from app.seedwork.domain.exceptions import DomainException
from app.seedwork.aplication.commands import execute_command
from app.seedwork.aplication.queries import execute_query

bp = apiflask.create_blueprint('audit_router', '/audits')


@bp.route("/", methods=('GET',))
def get_audit():
    map_audits = MapApp()
    sr = AuditService()
    return map_audits.dto_to_external(sr.get_audits())


@bp.route("/query", methods=('GET',))
def get_audit_query(audit_id=None):
    query_resultado = execute_query(GetEstate(audit_id))
    map_audits = MapApp()

    return map_audits.dto_to_external(query_resultado.resultado)


@bp.route("/command", methods=('POST',))
def create_audit():
    try:
        audit_dict = request.json
        map_audit = MapApp()
        audit_dto = map_audit.external_to_dto(audit_dict)

        command = CreateEstate(audit_dto)
        execute_command(command)
        return Response('{}', status=201, mimetype='application/json')
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

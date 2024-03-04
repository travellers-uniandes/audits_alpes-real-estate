import app.seedwork.presentation.apiflask as apiflask
import json
from flask import request
from flask import Response
from app.moduls.audits.aplication.querys.get_audit import GetAudit
from app.moduls.audits.aplication.querys.get_audits import GetAudits
from app.moduls.audits.aplication.mappers import MapperAuditDTOJson as MapApp
from app.moduls.audits.aplication.commands.create_audit import CreateAudit
from app.seedwork.domain.exceptions import DomainException
from app.seedwork.aplication.commands import execute_command
from app.seedwork.aplication.queries import execute_query

bp = apiflask.create_blueprint('audit_router', '/audits')


@bp.route("/", methods=('GET',))
def get_audits():
    query_resultado = execute_query(GetAudits())
    map_audits = MapApp()
    return map_audits.dto_to_external(query_resultado.resultado)


@bp.route("/<int:audit_id>", methods=('GET',))
def get_audit(audit_id: int):
    query_resultado = execute_query(GetAudit(audit_id))
    map_audit = MapApp()
    return map_audit.dto_to_external(query_resultado.resultado)


@bp.route("/command", methods=('POST',))
def create_audit():
    try:
        audit_dict = request.json
        map_audit = MapApp()
        audit_dto = map_audit.external_to_dto(audit_dict)

        command = CreateAudit(audit_dto)
        execute_command(command)
        return Response('{}', status=201, mimetype='application/json')
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

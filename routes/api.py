from flask import Blueprint, jsonify, make_response, request
from CONTROLADOR.DaoServidorPublicoControl import DaoServidorPublicoControl
from flask_cors import CORS
api = Blueprint('api', __name__)
#get para presentar los datos
#post para enviar los datos, modificar y iniciar sesion
CORS(api)
cors = CORS(api, resources={
    r"/*": {
        "origins": "*"
        }
    })


@api.route('/')
def home():
    return make_response(
        jsonify({"msg":"OK", "code": 200}),
        200
    )
# LISTA PERSONA GET
@api.route('/api/personas')
def lista_personas():
    sp = DaoServidorPublicoControl()
    return make_response(
        jsonify({"msg":"OK", "code": 200, "data":sp.to_dict() }),
        200
    )
# GUARDAR PERSONA POST
@api.route('/api/personas/guardar', methods=['POST'])
def guardar_personas():
    sp = DaoServidorPublicoControl()
    data = request.json
    print(type(data))
    if "apellidos" not in data:
        return make_response(
            jsonify({"msg":"Falta apellidos", "code": 400, data: []}),
            400
        )
    #TODO validar
    sp._servidorPublico._nombres = data['nombres']
    sp._servidorPublico._apellidos = data['apellidos']
    sp._servidorPublico.__numeroPila = data['numeroPila']
    sp.save
    return make_response(
        jsonify({"msg":"OK, la persona se ha agregado correctamente", "code": 200, "data":[] }),
        200
    )
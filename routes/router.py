from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort
from CONTROLADOR.DaoServidorPublicoControl import DaoServidorPublicoControl
from flask_cors import CORS
router = Blueprint('router', __name__)
#get para presentar los datos
#post para enviar los datos, modificar y iniciar sesion
CORS(router)
cors = CORS(router, resources={
    r"/*": {
        "origins": "*"
        }
    })


@router.route('/')
def home():
    # return make_response(
    #     jsonify({"msg":"OK", "code": 200}),
    #     200
    # )
    return render_template("template.html", nombre = "Joe")
    
    
# LISTA PERSONA GET
@router.route('/personas')
def lista_personas():
    pd = DaoServidorPublicoControl()
    #return render_template("nene/lista.html", lista = pd.to_dict())
    return render_template("nene/lista.html", lista = pd.to_dict())

# LISTA PERSONA GET
@router.route('/personas/ver')
def ver_guardar():
    return render_template("nene/guardar.html")

# LISTA PERSONA GET
@router.route('/personas/editar/<pos>')
def ver_editar(pos):
    pd = DaoServidorPublicoControl()
    nene = pd._lista.get(int(pos) -1 )
    print(nene)
    print("vamos bien!!!")
    return render_template("nene/editar.html", data = nene)

# GUARDAR PERSONA POST
@router.route('/personas/guardar', methods=['POST'])
def guardar_personas():
    pd = DaoServidorPublicoControl()
    data = request.form
    
    if "apellidos" not in data.keys():
        abort(400)
    #TODO validar
    pd._servidorPublico._nombres = data['nombres']
    pd._servidorPublico._apellidos = data['apellidos']
    pd._servidorPublico._numeroPila = data['numeroPila']
    pd.save
    return redirect("/personas", code = 302)


# MODIFICAR PERSONA POST
@router.route('/personas/modificar', methods=['POST'])
def modificar_personas():
    pd = DaoServidorPublicoControl()
    data = request.form
    pos = data["id"]
    nene = pd._lista.get(int(pos) - 1)
    
    if "apellidos" not in data.keys():
        abort(400)
        

    #TODO validar
    pd._servidorPublico = nene
    pd._servidorPublico._nombres = data['nombres']
    pd._servidorPublico._apellidos = data['apellidos']
    pd._servidorPublico._numeroPila = data['numeroPila']
    pd.merge(int(pos) - 1)
    return redirect("/personas", code = 302)
from flask import Flask, redirect, request
from flask import render_template, request, jsonify
from flask_migrate import Migrate

from .database import db
from .models import Empresas
from .forms import EmpresasForm

app = Flask(__name__)

db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)

app.config['SECRET_KEY'] = 'llave secreta XD'
#se infica cual es la url que usara para la conexion a la base de datos
#credenciales de conecction
db_user = 'jencinas'
db_pswd = 'megustanlasquesadillas23'
db_host = '127.0.0.1'
db_name = 'vacaciones'
db_port = 5432
Full_url_db = 'postgresql://jencinas:megustanlasquesadillas23@127.0.0.1:5432/vacaciones'

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = Full_url_db
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


@app.route('/', methods=['GET', 'POST'])
def home():
    listemp = Empresas.query.order_by('id')
    empresa = Empresas()
    empresaform = EmpresasForm(obj=empresa)
    if request.method == 'POST':
        if empresaform.validate_on_submit():
            empresaform.populate_obj(empresa)
            db.session.add(empresa)
            db.session.commit()
            return redirect(request.url)
    return render_template('index.html', form=empresaform, listemp=listemp)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='9000', debug=True)

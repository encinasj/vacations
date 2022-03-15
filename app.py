from os import urandom
from flask import Flask, flash, redirect, request, url_for
from flask import render_template, request, jsonify
from flask_migrate import Migrate

from .database import db
from .models import Empresas
from .forms import EmpresasForm

app = Flask(__name__)

db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)
app.secret_key = urandom(24)
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
    if request.method == 'POST' and empresaform.validate():
        if empresaform.validate_on_submit():
            empresaform.populate_obj(empresa)
            db.session.add(empresa)
            db.session.commit()
            flash("Micronegocio Agregado!!")
        else:
            flash('whoops hubo un error!...')
            return redirect(request.url)
    return render_template('index.html', form=empresaform, listemp=listemp)


@app.route("/delete/<int:id>")
def delete_company(id):
    delete_to_company = Empresas.query.get_or_404(id)
    try:
        db.session.delete(delete_to_company)
        db.session.commit()
        flash("Micronegocio Eliminado!!")
        return redirect(url_for('home'))
    except:
        flash("whoops hubo un error!..")
        return redirect(url_for('home'))


@app.route('/micronegocio/<int:id>', methods=['GET', 'POST'])
def detaillcompany(id):
    namecomp = Empresas.query.get_or_404(id)
    
    return render_template('micronegocio.html', id=id, name=namecomp)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='9000', debug=True)

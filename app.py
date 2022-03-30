from os import urandom
from flask import Flask, flash, redirect, request, url_for, render_template, jsonify
from flask_migrate import Migrate

from .database import db
from .models import Employee
from .forms import EmployeesForm

app = Flask(__name__)

db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)
app.secret_key = urandom(24)

#se infica cual es la url que usara para la conexion a la base de datos
#credenciales de conecction
'''
'''
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


#db testing
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#conditions variables
#days per year
days_per_year = 365

#years 
Year = 1

#vacations days per year
days_of_vacations1 = 6
days_of_vacations2 = 8
days_of_vacations3 = 10
days_of_vacations4 = 12
days_of_vacations5 = 14
days_of_vacations6 = 16
days_of_vacations7 = 18
days_of_vacations8 = 20
days_of_vacations9 = 22


@app.route('/', methods=['GET', 'POST'])
def home():
    listemp = Employee.query.order_by('id')
    employee = Employee()
    employeesform = EmployeesForm(obj=employee)
    if request.method == 'POST' and employeesform.validate():
        if employeesform.validate_on_submit():
            employeesform.populate_obj(employee)
            db.session.add(employee)
            db.session.commit()
            flash("Colaborador Agregado!!")
        else:
            flash('whoops hubo un error!...')
            return redirect(request.url)
    return render_template('index.html', employeesform=employeesform, listemp=listemp)

@app.route("/delete/<int:id>")
def delete_employee(id):
    delete_employee = Employee.query.get_or_404(id)
    try:
        db.session.delete(delete_employee)
        db.session.commit()
        flash("Colaborador Eliminado!!")
        return redirect(url_for('home'))
    except:
        flash("whoops hubo un error!..")
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='5000', debug=True)

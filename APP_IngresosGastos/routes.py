from flask import redirect, render_template, request, url_for, flash
from APP_IngresosGastos import app
from APP_IngresosGastos.forms import MovementsForm
from APP_IngresosGastos.models import delete_by, edit_by, insert, select_all, select_by
from datetime import datetime, date

def validateForm(requestForm):
    error = []
    requestDate = datetime.strptime(requestForm["Date"], '%Y-%m-%d').date()
    if requestForm["Date"] == "" or requestDate > date.today():
        error.append("Fecha inválida: La fecha introducida es en el futuro o está vacía")
    if requestForm["Description"] == "":
        error.append("Concepto vacío: Introduce una descripción")
    if requestForm["Value"] == "" or float(requestForm["Value"]) == 0.0:
        error.append("Cantidad vacío o cero: Debes introducir un monto válido")
    return error

@app.route("/")
def index():
    dataBase = select_all()
    return render_template("index.html", pageTitle = "Todos", dataBase = dataBase)

@app.route("/new", methods=["GET", "POST"])
def create():
    form = MovementsForm()
    if request.method == "GET":
        return render_template("new.html", pageTitle = "Nuevo registro", requestForm = form)
    else:
        if form.validate_on_submit():
            insert([form.Date.data, form.Description.data, form.Value.data])
            flash("Movimiento registrado correctamente")
            return redirect(url_for("index")) # Otra forma de dirigirse a otra URL llamando la función
        else:
            return render_template("new.html", pageTitle = "Nuevo registro", requestForm = form)

@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    if request.method == "GET":
        record = select_by(id)
        return render_template("delete.html", pageTitle = "Eliminar registro", data = record)
    else:
        delete_by(id)
        flash("Movimiento eliminado correctamente")
        return redirect("/")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "GET":
        record = select_by(id)
        return render_template("edit.html", pageTitle = "Modificar registro", data = record)
    else:
        edit_by(id)
        return redirect("/")

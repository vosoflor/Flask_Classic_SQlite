from flask import redirect, render_template, request, url_for
from APP_IngresosGastos import app
from APP_IngresosGastos.models import delete_by, insert, select_all, select_by
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
    if request.method == "GET":
        return render_template("new.html", pageTitle = "Nuevo registro", requestForm = {})
    else:
        error = validateForm(request.form)
        if error:
            return render_template("new.html", pageTitle = "Nuevo registro", msgError = error, requestForm = request.form)
        else:
            insert([request.form["Date"], request.form["Description"], request.form["Value"]])
            return redirect(url_for("index")) # Otra forma de dirigirse a otra URL llamando la función

@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    if request.method == "GET":
        record = select_by(id)
        return render_template("delete.html", pageTitle = "Eliminar registro", data = record)
    else:
        delete_by(id)
        return redirect("/")


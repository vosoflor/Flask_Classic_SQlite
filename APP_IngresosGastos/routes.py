from flask import redirect, render_template, request, url_for, flash
from APP_IngresosGastos import app
from APP_IngresosGastos.forms import MovementsForm
from APP_IngresosGastos.models import delete_by, edit_by, insert, select_all, select_by, total_earnings, total_expenses
from datetime import datetime, date

@app.route("/")
def index():
    dataBase = select_all()
    earnings = total_earnings()
    expenses = total_expenses()
    return render_template("index.html", pageTitle = "Todos", dataBase = dataBase, ingreso = earnings, gasto = expenses, saldo = earnings + expenses)

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
    form = MovementsForm()
    if request.method == "GET":
        record = select_by(id)
        form.Date.data = datetime.strptime(record[1], "%Y-%m-%d")
        form.Description.data = record[2]
        form.Value.data = record[3]
        return render_template("edit.html", pageTitle = "Modificar registro", requestForm = form, identifier = id)
    else:
        if form.validate_on_submit():
            edit_by(id, [form.Date.data, form.Description.data, form.Value.data])
            flash("Movimiento actualizado correctamente")
            return redirect("/")
        else:
            return render_template("edit.html", pageTitle = "Modificar registro", requestForm = form, identifier = id)

from flask import render_template
from APP_IngresosGastos import app

@app.route("/")
def index():
    dataBase = [
        {"id":1, "Date":"2022-01-01", "Description":"Sueldo", "Value":1500},
        {"id":2, "Date":"2022-01-05", "Description":"Regalo reyes", "Value":-150},
        {"id":3, "Date":"2022-01-06", "Description":"Almuerzo", "Value":-100},
    ]
    return render_template("index.html", pageTitle = "Todos", dataBase = dataBase)


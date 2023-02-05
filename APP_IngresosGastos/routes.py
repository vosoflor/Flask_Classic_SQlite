from APP_IngresosGastos import app

@app.route("/")
def index():
    return "Esto funciona, como mola Flask!!!"
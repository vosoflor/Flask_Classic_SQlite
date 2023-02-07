from flask import Flask

app = Flask(__name__, instance_relative_config = True)
app.config.from_object("config") # Para que reconozca la clave secreta desde config.py

from APP_IngresosGastos.routes import *
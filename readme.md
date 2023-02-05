# Aplicación web ingresos-gastos

Programa hecho en Python con el framework Flask con motor de base de datos SQlite

## Instalación

En su entorno de Python ejecutar el comando:
    ```
    pip install -r requirements.txt
    ```
La librería utilizada es Flask (https://flask.palletsprojects.com/en/2.2.x/quickstart/).

## Ejecución del programa

1. Comando para inicializar el servidor del programa:

    - Renombrar el archivo .env_template a .env e incluir la información requerida, ejemplo a continuación:
        ```
        FLASK_APP = main.py
        FLASK_DEBUG = true
        ```

2. Comando para ejecutar el servidor:
    ```
    flask run
    ```
    
    Al ejecutar el servidor aparece la ruta que en este caso sería el localhost http://127.0.0.1:5000.

3. Comando especial para lanzar el servidor en un puerto diferente. Ésto se utiliza en los casos que el puerto 5000 esté ocupado.
    ```
    flask run -p 5001
    ```
from flask import Flask, render_template
import routes.login_rutas
import routes.panel_rutas
import routes.gestion_admin
import routes.home
import routes.clientes_rutas
import routes.gestion_aseo
from conexion import app


# Ruta principal (home)
@app.route('/')
def home_main():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
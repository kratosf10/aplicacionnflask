from flask import (Flask, config, render_template, request, flash, json, send_file, session, jsonify, redirect, url_for)
#pip install mysql-connector - pip install Flask
from controllers.car_controller import CarController

app = Flask(__name__)
app.secret_key = "crudpythonmysql"

# Ruta principal que muestra las estadísticas
@app.route('/')
def main():
    return CarController.show_stats()

# Ruta para agregar nuevas estadísticas
@app.route('/addstats', methods=['POST', 'GET'])
def addstats():
    if request.method == 'POST':
        CarController.insert_stats()
    return redirect(url_for('main'))

# Ruta para ver estadísticas
@app.route('/viewstats', methods=['POST','GET']) 
def viewstats():
    if request.method == 'POST':
        return CarController.view_stats()

# Ruta para borrar estadísticas  
@app.route('/deletestats/<string:id>', methods=['POST', 'GET']) 
def deletestats(id): 
    if request.method == 'GET': 
       CarController.delete_stats(id)
    return redirect(url_for('main'))

# Ruta para actualizar estadísticas
@app.route('/updatestats', methods=['GET','POST']) 
def updatestats(): 
    if request.method == 'POST':
        CarController.update_stats()
    return redirect(url_for('main'))

# Ruta para mostrar la interfaz de "Sacar Ticket"
@app.route('/ticket')
def ticket():
    return render_template('ticket.html')  # Renderiza el archivo ticket.html

@app.route('/submit_ticket', methods=['POST'])
def submit_ticket():
    inconveniente = request.form.get('inconveniente')
    if inconveniente:
        flash("Ticket enviado con éxito.")
        return redirect('/ticket')  # Redirige al mismo formulario de ticket
    else:
        flash("Por favor, escribe tu inconveniente.")  # Muestra un mensaje si no se ingresa nada
        return redirect('/ticket')  # Redirige nuevamente al formulario


# Ejecutar aplicacion
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)




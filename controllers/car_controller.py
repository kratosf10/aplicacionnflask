from flask import (Flask, config, render_template, request, flash, json, send_file, session, jsonify, redirect, url_for)
from models.car_model import CarModel

class CarController:
    @staticmethod
    def show_stats():
        car_model = CarModel()
        pstats = car_model.get_all_stats()
        car_model.close()
        return render_template('index.html', pstats=pstats)
    
    @staticmethod
    def view_stats():
        try:
            car_model = CarModel()
            id = request.form['id']
            data = car_model.get_one_stat(id)
            car_model.close()
            return jsonify({'htmlresponse': render_template('viewstats.html', pstats=data)})
        except:
            flash('¡Ah ocurrido un error!')
    
    @staticmethod
    def insert_stats():
        try:
            car_model = CarModel()
            Nombre = request.form['Nombre'] 
            Raza = request.form['Raza'] 
            Nivel = request.form['Nivel'] 
            Daño = request.form['Daño'] 
            Resistencia = request.form['Resistencia'] 
            car_model.insert_Stats(Nombre, Raza, Nivel, Daño, Resistencia)
            car_model.close()
            flash('Stat registrado correctamente!!!')      
        except:
            flash('¡Ah ocurrido un error!')
    
    @staticmethod
    def delete_stats(id):
        try:
            car_model = CarModel()
            car_model.delete_stats(id)
            car_model.close()
            flash('Stat eliminado correctamente!!!') 
        except:
            flash('¡Ah ocurrido un error!')

    @staticmethod
    def update_stats():
        try:
            car_model = CarModel()
            Nombre = request.form['id'] 
            Raza = request.form['Raza'] 
            Nivel = request.form['Nivel'] 
            Daño = request.form['Daño'] 
            Resistencia = request.form['Resistencia'] 
            car_model.update_Stats(Nombre, Raza, Nivel, Daño, Resistencia)
            car_model.close()
            flash('Stat actualizado correctamente!!!')      
        except:
            flash('¡Ah ocurrido un error!')

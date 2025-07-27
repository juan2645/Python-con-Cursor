from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import uuid

# Configuración de la aplicación
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'

# Lista en memoria para almacenar las tareas
tareas = []
contador_id = 1

# Modelo simple de tarea
class Tarea:
    def __init__(self, texto, hecho=False):
        global contador_id
        self.id = contador_id
        contador_id += 1
        self.texto = texto
        self.hecho = hecho
        self.fecha_creacion = datetime.now()

# Agregar algunas tareas de ejemplo
tareas.append(Tarea("Comprar víveres"))
tareas.append(Tarea("Hacer ejercicio"))
tareas.append(Tarea("Estudiar Python"))

@app.route('/')
def index():
    """Página principal: mostrar lista de tareas y formulario para añadir nueva"""
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['POST'])
def agregar_tarea():
    """Procesar formulario de nueva tarea y redirigir a /"""
    texto = request.form.get('texto', '').strip()
    
    if not texto:
        flash('El texto de la tarea no puede estar vacío', 'error')
    else:
        nueva_tarea = Tarea(texto)
        tareas.append(nueva_tarea)
        flash('Tarea agregada exitosamente', 'success')
    
    return redirect(url_for('index'))

@app.route('/completar/<int:id>')
def completar_tarea(id):
    """Marcar una tarea como completada"""
    for tarea in tareas:
        if tarea.id == id:
            tarea.hecho = not tarea.hecho
            estado = "completada" if tarea.hecho else "pendiente"
            flash(f'Tarea marcada como {estado}', 'success')
            break
    else:
        flash('Tarea no encontrada', 'error')
    
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id>')
def eliminar_tarea(id):
    """Eliminar una tarea"""
    global tareas
    tareas = [t for t in tareas if t.id != id]
    flash('Tarea eliminada exitosamente', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

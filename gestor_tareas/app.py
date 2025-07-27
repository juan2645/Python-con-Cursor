from flask import Flask, request, redirect, render_template, flash
from datetime import datetime

# Configuración de la aplicación
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'

# Lista en memoria para almacenar las tareas
tareas = []
contador_id = 1

# Funciones auxiliares
def agregar_tarea(texto):
    """Agregar una nueva tarea a la lista"""
    global contador_id
    nueva_tarea = {
        'id': contador_id,
        'texto': texto,
        'hecho': False,
        'fecha_creacion': datetime.now()
    }
    tareas.append(nueva_tarea)
    contador_id += 1
    # Solo mostrar flash si estamos en contexto de petición
    try:
        flash('Tarea agregada exitosamente', 'success')
    except RuntimeError:
        pass  # Ignorar error fuera de contexto

def completar_tarea(id):
    """Marcar una tarea como completada/pendiente"""
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['hecho'] = not tarea['hecho']
            estado = "completada" if tarea['hecho'] else "pendiente"
            try:
                flash(f'Tarea marcada como {estado}', 'success')
            except RuntimeError:
                pass
            break
    else:
        try:
            flash('Tarea no encontrada', 'error')
        except RuntimeError:
            pass

def inicializar_tareas():
    """Inicializar tareas de ejemplo"""
    global contador_id
    tareas_ejemplo = ["Comprar víveres", "Hacer ejercicio", "Estudiar Python"]
    for texto in tareas_ejemplo:
        nueva_tarea = {
            'id': contador_id,
            'texto': texto,
            'hecho': False,
            'fecha_creacion': datetime.now()
        }
        tareas.append(nueva_tarea)
        contador_id += 1

@app.route('/')
def index():
    # Ordenar tareas: incompletas primero, luego completadas
    tareas_ordenadas = sorted(tareas, key=lambda t: t['hecho'])
    return render_template('index.html', tareas=tareas_ordenadas)

@app.route('/agregar', methods=['POST'])
def agregar():
    texto_tarea = request.form.get('texto_tarea')
    if texto_tarea:
        agregar_tarea(texto_tarea)
    return redirect('/')

@app.route('/completar/<int:id>')
def completar(id):
    completar_tarea(id)
    return redirect('/')

@app.route('/eliminar/<int:id>')
def eliminar(id):
    """Eliminar una tarea"""
    global tareas
    tareas = [t for t in tareas if t['id'] != id]
    flash('Tarea eliminada exitosamente', 'success')
    return redirect('/')

if __name__ == '__main__':
    inicializar_tareas()
    app.run(debug=True, host='0.0.0.0', port=5000)

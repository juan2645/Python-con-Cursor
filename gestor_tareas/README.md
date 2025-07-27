# Gestor de Tareas Simple - Aplicación Flask

Una aplicación web simple para gestionar tareas, desarrollada con Flask y almacenamiento en memoria.

## Características

- ✅ Crear y eliminar tareas
- ✅ Marcar tareas como completadas/pendientes
- ✅ Interfaz moderna y responsive con Bootstrap
- ✅ Almacenamiento simple en memoria
- ✅ Diseño intuitivo y fácil de usar

## Instalación

1. **Navegar al directorio del proyecto**

   ```bash
   cd gestor_tareas
   ```

2. **Crear un entorno virtual (recomendado)**

   ```bash
   python -m venv venv
   
   # En Windows:
   venv\Scripts\activate
   
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. **Ejecutar la aplicación**

   ```bash
   python app.py
   ```

2. **Abrir en el navegador**

   ```
   http://localhost:5000
   ```

## Estructura del Proyecto

```
gestor_tareas/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Este archivo
└── templates/            # Plantillas HTML
    ├── base.html         # Plantilla base
    └── index.html        # Página principal con formulario y lista
```

## Rutas de la Aplicación

- **`/`** - Página principal: muestra la lista de tareas y formulario para agregar nueva
- **`/agregar`** (POST) - Procesa el formulario de nueva tarea y redirige a `/`
- **`/completar/<id>`** - Marca una tarea como completada/pendiente
- **`/eliminar/<id>`** - Elimina una tarea

## Funcionalidades

### Gestión de Tareas

- **Agregar**: Usar el formulario en la página principal
- **Completar**: Hacer clic en el botón de check/undo junto a cada tarea
- **Eliminar**: Hacer clic en el botón de basura junto a cada tarea

### Interfaz de Usuario

- Diseño responsive que funciona en móviles y escritorio
- Iconos intuitivos de Font Awesome
- Notificaciones flash para feedback del usuario
- Confirmaciones antes de eliminar tareas
- Tareas completadas se muestran tachadas

## Tecnologías Utilizadas

- **Backend**: Flask
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Almacenamiento**: Lista en memoria (se reinicia al reiniciar la app)
- **Iconos**: Font Awesome

## Estructura de Datos

Cada tarea es un objeto con:

```python
{
    'id': 1,
    'texto': 'Comprar víveres',
    'hecho': False,
    'fecha_creacion': datetime.now()
}
```

## Personalización

### Agregar más campos a las tareas

En `app.py`, modifica la clase `Tarea`:

```python
class Tarea:
    def __init__(self, texto, hecho=False):
        global contador_id
        self.id = contador_id
        contador_id += 1
        self.texto = texto
        self.hecho = hecho
        self.fecha_creacion = datetime.now()
        # Agregar nuevos campos aquí
        self.prioridad = 'media'
```

### Cambiar el puerto

Modifica en `app.py`:

```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

## Solución de Problemas

### Error de dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Puerto ocupado

Modifica el puerto en `app.py`:

```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

## Limitaciones

- Los datos se pierden al reiniciar la aplicación (almacenamiento en memoria)
- No hay persistencia de datos
- Funcionalidad básica sin características avanzadas

## Próximos Pasos

Para expandir la aplicación, podrías:

- Agregar persistencia con SQLite o archivos JSON
- Implementar edición de tareas
- Agregar fechas límite
- Implementar categorías o etiquetas
- Agregar autenticación de usuarios

---

¡Disfruta usando tu gestor de tareas simple! 🚀

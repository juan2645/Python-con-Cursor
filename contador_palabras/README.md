# Contador de Palabras

Un programa en Python para analizar y contar palabras en archivos de texto.

## Características

- ✅ Cuenta palabras totales y únicas
- ✅ Muestra las palabras más frecuentes
- ✅ Filtra palabras comunes (stop words) automáticamente
- ✅ Interfaz de línea de comandos y modo interactivo
- ✅ Soporte para archivos UTF-8
- ✅ Estadísticas detalladas con porcentajes

## Instalación

1. Asegúrate de tener Python 3.6+ instalado
2. Activa el entorno virtual:
   ```bash
   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   
   # Windows (CMD)
   .\venv\Scripts\activate.bat
   
   # Linux/macOS
   source venv/bin/activate
   ```

## Uso

### Modo Interactivo
```bash
python contador_palabras.py
```

### Modo Línea de Comandos
```bash
# Análisis básico
python contador_palabras.py archivo.txt

# Mostrar top 20 palabras más frecuentes
python contador_palabras.py archivo.txt --top 20

# Incluir palabras comunes en el conteo
python contador_palabras.py archivo.txt --incluir-comunes

# Ver ayuda
python contador_palabras.py --help
```

## Ejemplo de Salida

```
📊 ANÁLISIS DEL ARCHIVO: ejemplo.txt
==================================================
📝 Total de palabras: 245
🔤 Palabras únicas: 89
📈 Palabras más frecuentes (top 10):
------------------------------
 1. 'que':  15 veces ( 6.1%)
 2. 'de':  12 veces ( 4.9%)
 3. 'la':  10 veces ( 4.1%)
 4. 'y':   9 veces ( 3.7%)
 5. 'el':   8 veces ( 3.3%)
 6. 'a':    7 veces ( 2.9%)
 7. 'en':   6 veces ( 2.4%)
 8. 'con':  5 veces ( 2.0%)
 9. 'su':   5 veces ( 2.0%)
10. 'los':  4 veces ( 1.6%)

✅ Análisis completado exitosamente!
```

## Archivos Incluidos

- `contador_palabras.py` - Programa principal
- `ejemplo.txt` - Archivo de ejemplo para pruebas
- `README.md` - Este archivo de documentación

## Funcionalidades

### Limpieza de Texto
- Convierte todo a minúsculas
- Elimina caracteres especiales
- Normaliza espacios múltiples

### Filtrado de Palabras Comunes
Por defecto, el programa ignora palabras comunes en español como:
- Artículos: el, la, de, que, y, a, en, un, es, se, no...
- Preposiciones: por, con, para, al, del...
- Conjunciones: pero, ni, contra...
- Pronombres: me, te, lo, le, da, su...

### Estadísticas
- Total de palabras
- Número de palabras únicas
- Frecuencia de cada palabra
- Porcentaje de aparición

## Requisitos

- Python 3.6 o superior
- Módulos estándar de Python (no requiere instalaciones adicionales)

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT. 
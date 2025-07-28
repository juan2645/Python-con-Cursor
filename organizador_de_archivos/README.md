# Organizador de Archivos Automático

Este script organiza automáticamente los archivos en una carpeta, distribuyéndolos en subcarpetas según su tipo de archivo.

## Características

- **Clasificación automática**: Organiza archivos por tipo (Imágenes, Documentos, Videos, Audio, etc.)
- **Manejo de conflictos**: Renombra automáticamente archivos con nombres duplicados
- **Logging completo**: Registra todas las operaciones en archivos de log
- **Ejecución manual o programada**: Puede ejecutarse manualmente o programarse para ejecutarse automáticamente
- **Estadísticas**: Muestra estadísticas de archivos organizados
- **Seguro**: No elimina archivos, solo los mueve

## Tipos de archivos soportados

### Categorías predefinidas:
- **Imágenes**: .jpg, .jpeg, .png, .gif, .bmp, .tiff, .svg, .webp
- **Documentos**: .pdf, .doc, .docx, .txt, .rtf, .odt, .xls, .xlsx, .ppt, .pptx
- **Videos**: .mp4, .avi, .mov, .wmv, .flv, .mkv, .webm, .m4v
- **Audio**: .mp3, .wav, .flac, .aac, .ogg, .wma, .m4a
- **Comprimidos**: .zip, .rar, .7z, .tar, .gz, .bz2
- **Programas**: .exe, .msi, .dmg, .pkg, .deb, .rpm

### Categorías automáticas:
- **Sin_Extension**: Archivos sin extensión
- **Nuevas categorías**: Se crean automáticamente para cualquier extensión no clasificada
  - Ejemplo: archivos `.psd` se van a carpeta `PSD`
  - Ejemplo: archivos `.ai` se van a carpeta `AI`

## Instalación

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Ejecución manual

#### Modo interactivo (recomendado):
```bash
python organizar.py
```
El script te preguntará qué carpeta quieres organizar con opciones como:
- Carpeta actual
- Carpeta de Descargas
- Carpeta de Escritorio
- Otra carpeta (especificar ruta)

#### Organizar un directorio específico:
```bash
python organizar.py "C:\Users\TuUsuario\Downloads"
```

#### Ejecutar sin confirmación:
```bash
python organizar.py --auto
```

#### Mostrar estadísticas después de organizar:
```bash
python organizar.py --estadisticas
```

### Ejecución programada

#### Programar para ejecutarse cada 24 horas:
```bash
python programador.py "C:\Users\TuUsuario\Downloads"
```

#### Programar con intervalo personalizado (cada 6 horas):
```bash
python programador.py "C:\Users\TuUsuario\Downloads" --intervalo 6
```

#### Ver programación sin ejecutar:
```bash
python programador.py "C:\Users\TuUsuario\Downloads" --mostrar
```

## Estructura de carpetas creada

Después de la organización, se creará la siguiente estructura:

```
Directorio_Origen/
├── Imagenes/
├── Documentos/
├── Videos/
├── Audio/
├── Comprimidos/
├── Programas/
├── Sin_Extension/          # Archivos sin extensión
├── PSD/                   # Ejemplo de categoría automática
├── AI/                    # Ejemplo de categoría automática
└── [Otras categorías automáticas]/
```

### Categorías automáticas:
El organizador crea automáticamente nuevas carpetas para tipos de archivo no clasificados:
- **Sin_Extension**: Para archivos sin extensión
- **Categorías por extensión**: Se crean basándose en la extensión del archivo
  - `.psd` → carpeta `PSD`
  - `.ai` → carpeta `AI`
  - `.sketch` → carpeta `SKETCH`
  - etc.

## Archivos de log

El script genera archivos de log para rastrear las operaciones:

- `organizador_archivos.log`: Log del organizador principal
- `programador_organizador.log`: Log del programador automático

## Ejemplos de uso

### Ejemplo 1: Organizar carpeta de Descargas
```bash
# Navegar al directorio del script
cd organizador_de_archivos

# Organizar la carpeta de Descargas
python organizar.py "C:\Users\TuUsuario\Downloads" --estadisticas
```

### Ejemplo 2: Programar organización automática
```bash
# Programar para organizar cada 12 horas
python programador.py "C:\Users\TuUsuario\Downloads" --intervalo 12
```

### Ejemplo 3: Organizar directorio actual
```bash
# Organizar archivos en el directorio actual
python organizar.py --auto --estadisticas
```

## Características de seguridad

- **No elimina archivos**: Solo los mueve a subcarpetas
- **Manejo de duplicados**: Renombra automáticamente archivos con nombres existentes
- **Logging completo**: Registra todas las operaciones para auditoría
- **Confirmación manual**: Por defecto pide confirmación antes de ejecutar
- **Manejo de errores**: Continúa procesando otros archivos si uno falla
- **Exclusión de archivos del sistema**: No mueve scripts, logs ni archivos del sistema
- **Uso de pathlib**: Manejo moderno y seguro de rutas de archivos

## Personalización

### Agregar nuevos tipos de archivo

Puedes modificar el diccionario `extensiones` en la clase `OrganizadorArchivos`:

```python
self.extensiones = {
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp'],
    'Documentos': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.m4v'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
    'Comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    'Programas': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm'],
    'Nuevo_Tipo': ['.nueva_extension'],  # Agregar aquí
    'Otros': []
}
```

## Solución de problemas

### Error: "El directorio no existe"
- Verifica que la ruta del directorio sea correcta
- Asegúrate de usar comillas si la ruta contiene espacios

### Error: "Permiso denegado"
- Ejecuta el script como administrador
- Verifica que tengas permisos de escritura en el directorio

### Los archivos no se mueven
- Verifica los logs para ver si hay errores
- Asegúrate de que los archivos no estén siendo usados por otras aplicaciones

## Notas importantes

- El script solo procesa archivos, no subcarpetas
- Los archivos sin extensión se clasifican como "Otros"
- El programador automático se ejecuta en segundo plano hasta que se detenga con Ctrl+C
- Se recomienda hacer una copia de seguridad antes de usar en directorios importantes 
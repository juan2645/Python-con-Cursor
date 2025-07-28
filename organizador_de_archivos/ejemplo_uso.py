#!/usr/bin/env python3
"""
Ejemplo de uso del Organizador de Archivos
Este script demuestra cómo usar el organizador programáticamente
"""

import os
import tempfile
from pathlib import Path
from organizar import OrganizadorArchivos

def crear_archivos_ejemplo():
    """
    Crea archivos de ejemplo para demostrar el organizador.
    """
    # Crear directorio temporal para la demostración
    directorio_temp = Path(tempfile.mkdtemp(prefix="organizador_demo_"))
    
    # Lista de archivos de ejemplo con diferentes extensiones
    archivos_ejemplo = [
        "imagen1.jpg",
        "documento1.pdf", 
        "video1.mp4",
        "musica1.mp3",
        "comprimido1.zip",
        "programa1.exe",
        "archivo_sin_extension",
        "imagen2.png",
        "documento2.docx",
        "video2.avi"
    ]
    
    print(f"Creando archivos de ejemplo en: {directorio_temp}")
    
    # Crear archivos de ejemplo
    for archivo in archivos_ejemplo:
        ruta_archivo = directorio_temp / archivo
        with open(ruta_archivo, 'w') as f:
            f.write(f"Contenido de ejemplo para {archivo}")
        print(f"Creado: {archivo}")
    
    return directorio_temp

def demostrar_organizador():
    """
    Demuestra el uso del organizador de archivos.
    """
    print("=== DEMOSTRACIÓN DEL ORGANIZADOR DE ARCHIVOS ===\n")
    
    # Crear archivos de ejemplo
    directorio_ejemplo = crear_archivos_ejemplo()
    
    print(f"\nDirectorio antes de organizar:")
    print(f"Ubicación: {directorio_ejemplo}")
    print("Archivos:")
    for archivo in directorio_ejemplo.iterdir():
        if archivo.is_file():
            print(f"  - {archivo.name}")
    
    print("\n" + "="*50)
    
    # Crear instancia del organizador
    organizador = OrganizadorArchivos(directorio_ejemplo)
    
    # Organizar archivos
    print("Organizando archivos...")
    organizador.organizar_archivos()
    
    print("\n" + "="*50)
    
    # Mostrar estadísticas
    print("Resultado de la organización:")
    organizador.mostrar_estadisticas()
    
    print(f"\nEstructura final:")
    for item in directorio_ejemplo.iterdir():
        if item.is_dir():
            archivos = list(item.iterdir())
            print(f"  {item.name}/ ({len(archivos)} archivos)")
            for archivo in archivos:
                if archivo.is_file():
                    print(f"    - {archivo.name}")
    
    print(f"\nLos archivos han sido organizados en: {directorio_ejemplo}")
    print("Puedes revisar manualmente la estructura creada.")
    
    return directorio_ejemplo

def limpiar_directorio(directorio):
    """
    Limpia el directorio de ejemplo (opcional).
    """
    respuesta = input(f"\n¿Deseas eliminar el directorio de ejemplo {directorio}? (s/n): ")
    if respuesta.lower() in ['s', 'si', 'sí', 'y', 'yes']:
        import shutil
        try:
            shutil.rmtree(directorio)
            print("Directorio eliminado.")
        except Exception as e:
            print(f"Error al eliminar directorio: {e}")
    else:
        print("Directorio conservado para revisión manual.")

if __name__ == "__main__":
    try:
        # Ejecutar demostración
        directorio_resultado = demostrar_organizador()
        
        # Preguntar si limpiar
        limpiar_directorio(directorio_resultado)
        
    except KeyboardInterrupt:
        print("\nDemostración interrumpida por el usuario.")
    except Exception as e:
        print(f"Error en la demostración: {e}") 
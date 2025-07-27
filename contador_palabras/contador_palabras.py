#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contador de Palabras
Programa para contar palabras en archivos de texto
"""

import os
import sys
import argparse
from collections import Counter
import re


def limpiar_texto(texto):
    """
    Limpia el texto eliminando caracteres especiales y normalizando espacios
    """
    # Convertir a minúsculas
    texto = texto.lower()
    # Eliminar caracteres especiales excepto espacios y letras
    texto = re.sub(r'[^\w\s]', ' ', texto)
    # Normalizar espacios múltiples
    texto = re.sub(r'\s+', ' ', texto)
    return texto.strip()


def contar_palabras(texto, ignorar_palabras_comunes=True):
    """
    Cuenta las palabras en el texto
    """
    # Lista de palabras comunes a ignorar (stop words en español)
    palabras_comunes = {
        'el', 'la', 'de', 'que', 'y', 'a', 'en', 'un', 'es', 'se', 'no', 'te', 'lo', 'le', 'da',
        'su', 'por', 'son', 'con', 'para', 'al', 'del', 'los', 'las', 'una', 'como', 'pero',
        'sus', 'me', 'hasta', 'hay', 'donde', 'han', 'quien', 'están', 'estado', 'desde',
        'todo', 'nos', 'durante', 'todos', 'uno', 'les', 'ni', 'contra', 'otros', 'ese',
        'eso', 'ante', 'ellos', 'e', 'esto', 'mí', 'antes', 'algunos', 'qué', 'unos', 'yo',
        'otro', 'otras', 'otra', 'él', 'tanto', 'esa', 'estos', 'mucho', 'quienes', 'nada',
        'muchos', 'cual', 'poco', 'ella', 'estar', 'estas', 'algunas', 'algo', 'nosotros'
    }
    
    # Limpiar el texto
    texto_limpio = limpiar_texto(texto)
    
    # Dividir en palabras
    palabras = texto_limpio.split()
    
    if ignorar_palabras_comunes:
        # Filtrar palabras comunes
        palabras = [palabra for palabra in palabras if palabra not in palabras_comunes]
    
    return palabras


def analizar_archivo(ruta_archivo, ignorar_palabras_comunes=True, mostrar_top=10):
    """
    Analiza un archivo de texto y cuenta las palabras
    """
    try:
        # Verificar que el archivo existe
        if not os.path.exists(ruta_archivo):
            print(f"❌ Error: El archivo '{ruta_archivo}' no existe.")
            return None
        
        # Leer el archivo
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        
        # Contar palabras
        palabras = contar_palabras(contenido, ignorar_palabras_comunes)
        
        if not palabras:
            print("📄 El archivo está vacío o no contiene palabras válidas.")
            return None
        
        # Contar frecuencia de palabras
        contador = Counter(palabras)
        
        # Estadísticas
        total_palabras = len(palabras)
        palabras_unicas = len(contador)
        
        # Mostrar resultados
        print(f"\n📊 ANÁLISIS DEL ARCHIVO: {ruta_archivo}")
        print("=" * 50)
        print(f"📝 Total de palabras: {total_palabras}")
        print(f"🔤 Palabras únicas: {palabras_unicas}")
        print(f"📈 Palabras más frecuentes (top {mostrar_top}):")
        print("-" * 30)
        
        # Mostrar las palabras más frecuentes
        for i, (palabra, frecuencia) in enumerate(contador.most_common(mostrar_top), 1):
            porcentaje = (frecuencia / total_palabras) * 100
            print(f"{i:2d}. '{palabra}': {frecuencia:3d} veces ({porcentaje:5.1f}%)")
        
        return {
            'total_palabras': total_palabras,
            'palabras_unicas': palabras_unicas,
            'contador': contador
        }
        
    except UnicodeDecodeError:
        print(f"❌ Error: No se pudo leer el archivo '{ruta_archivo}'. Verifica que sea un archivo de texto válido.")
        return None
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return None


def main():
    """
    Función principal del programa
    """
    parser = argparse.ArgumentParser(
        description='Contador de palabras en archivos de texto',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python contador_palabras.py archivo.txt
  python contador_palabras.py archivo.txt --top 20
  python contador_palabras.py archivo.txt --incluir-comunes
        """
    )
    
    parser.add_argument('archivo', help='Ruta del archivo de texto a analizar')
    parser.add_argument('--top', type=int, default=10, 
                       help='Número de palabras más frecuentes a mostrar (default: 10)')
    parser.add_argument('--incluir-comunes', action='store_true',
                       help='Incluir palabras comunes en el conteo')
    
    args = parser.parse_args()
    
    # Verificar que se proporcionó un archivo
    if not args.archivo:
        print("❌ Error: Debes especificar un archivo de texto.")
        parser.print_help()
        return
    
    # Analizar el archivo
    resultado = analizar_archivo(
        args.archivo, 
        ignorar_palabras_comunes=not args.incluir_comunes,
        mostrar_top=args.top
    )
    
    if resultado:
        print(f"\n✅ Análisis completado exitosamente!")


if __name__ == "__main__":
    # Si no hay argumentos, mostrar modo interactivo
    if len(sys.argv) == 1:
        print("🔍 CONTADOR DE PALABRAS")
        print("=" * 30)
        archivo = input("📁 Ingresa la ruta del archivo de texto: ").strip()
        
        if archivo:
            # Verificar opciones
            incluir_comunes = input("¿Incluir palabras comunes? (s/n, default: n): ").strip().lower() == 's'
            try:
                top = int(input("¿Cuántas palabras más frecuentes mostrar? (default: 10): ").strip() or "10")
            except ValueError:
                top = 10
            
            # Analizar archivo
            resultado = analizar_archivo(archivo, not incluir_comunes, top)
            
            if resultado:
                print(f"\n✅ Análisis completado exitosamente!")
        else:
            print("❌ No se especificó ningún archivo.")
    else:
        main() 
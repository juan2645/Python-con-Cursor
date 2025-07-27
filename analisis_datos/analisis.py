import pandas as pd
import numpy as np
import os
from pathlib import Path
import matplotlib.pyplot as plt

def leer_datos(archivo):
    """
    Lee un archivo de datos (Excel o CSV) y retorna un DataFrame
    """
    extension = Path(archivo).suffix.lower()
    
    try:
        if extension == '.xlsx' or extension == '.xls':
            df = pd.read_excel(archivo)
        elif extension == '.csv':
            df = pd.read_csv(archivo)
        else:
            raise ValueError(f"Formato de archivo no soportado: {extension}")
        
        print(f"Archivo leído exitosamente: {archivo}")
        print(f"Dimensiones del dataset: {df.shape[0]} filas, {df.shape[1]} columnas")
        return df
    
    except Exception as e:
        print(f"Error al leer el archivo {archivo}: {e}")
        return None

def calcular_estadisticas(df):
    """
    Calcula estadísticas básicas para cada columna numérica
    """
    # Seleccionar solo columnas numéricas
    columnas_numericas = df.select_dtypes(include=[np.number]).columns
    
    if len(columnas_numericas) == 0:
        print("No se encontraron columnas numéricas en el dataset")
        return
    
    print("\n" + "="*60)
    print("ESTADÍSTICAS DESCRIPTIVAS")
    print("="*60)
    
    # Crear un DataFrame con las estadísticas
    estadisticas = {}
    
    for columna in columnas_numericas:
        datos = df[columna].dropna()  # Eliminar valores NaN
        
        if len(datos) > 0:
            estadisticas[columna] = {
                'Media': datos.mean(),
                'Mediana': datos.median(),
                'Desviación Estándar': datos.std(),
                'Mínimo': datos.min(),
                'Máximo': datos.max(),
                'Cantidad de datos': len(datos)
            }
    
    # Mostrar estadísticas en formato tabular
    df_estadisticas = pd.DataFrame(estadisticas).T
    print(df_estadisticas.round(4))
    
    return df_estadisticas

def crear_scatter_plot(df, col1, col2):
    """
    Crea un scatter plot de col1 vs col2
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(df[col1], df[col2], alpha=0.7, s=100, color='blue', edgecolors='black')
    plt.xlabel(col1, fontsize=12)
    plt.ylabel(col2, fontsize=12)
    plt.title(f'Scatter Plot: {col1} vs {col2}', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    # Agregar línea de tendencia
    z = np.polyfit(df[col1], df[col2], 1)
    p = np.poly1d(z)
    plt.plot(df[col1], p(df[col1]), "r--", alpha=0.8, linewidth=2)
    
    # Calcular y mostrar correlación
    correlacion = df[col1].corr(df[col2])
    plt.text(0.05, 0.95, f'Correlación: {correlacion:.3f}', 
             transform=plt.gca().transAxes, fontsize=12, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
    
    plt.tight_layout()
    plt.show()
    
    print(f"\nCorrelación entre {col1} y {col2}: {correlacion:.3f}")

def mostrar_info_dataset(df):
    """
    Muestra información general del dataset
    """
    print("\n" + "="*60)
    print("INFORMACIÓN DEL DATASET")
    print("="*60)
    
    print(f"Dimensiones: {df.shape[0]} filas × {df.shape[1]} columnas")
    print(f"Memoria utilizada: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")
    
    print("\nTipos de datos:")
    print(df.dtypes)
    
    print("\nPrimeras 5 filas:")
    print(df.head())
    
    print("\nInformación de valores faltantes:")
    valores_faltantes = df.isnull().sum()
    if valores_faltantes.sum() > 0:
        print(valores_faltantes[valores_faltantes > 0])
    else:
        print("No hay valores faltantes")

def main():
    """
    Función principal del script
    """
    # Cambiar al directorio donde está el script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Buscar archivos de datos en el directorio actual
    archivos_datos = []
    for archivo in os.listdir('.'):
        if archivo.endswith(('.xlsx', '.xls', '.csv')):
            archivos_datos.append(archivo)
    
    if not archivos_datos:
        print("No se encontraron archivos de datos (.xlsx, .xls, .csv) en el directorio actual")
        return
    
    print("Archivos de datos encontrados:")
    for i, archivo in enumerate(archivos_datos, 1):
        print(f"{i}. {archivo}")
    
    # Usar el primer archivo encontrado (o el archivo específico si solo hay uno)
    archivo_seleccionado = archivos_datos[0]
    print(f"\nAnalizando archivo: {archivo_seleccionado}")
    
    # Leer los datos
    df = leer_datos(archivo_seleccionado)
    
    if df is not None:
        # Mostrar información general
        mostrar_info_dataset(df)
        
        # Calcular y mostrar estadísticas
        estadisticas = calcular_estadisticas(df)
        
        # Crear scatter plot si hay al menos 2 columnas numéricas
        columnas_numericas = df.select_dtypes(include=[np.number]).columns
        if len(columnas_numericas) >= 2:
            print("\n" + "="*60)
            print("CREANDO SCATTER PLOT")
            print("="*60)
            crear_scatter_plot(df, columnas_numericas[0], columnas_numericas[1])
        
        print("\n" + "="*60)
        print("ANÁLISIS COMPLETADO")
        print("="*60)

if __name__ == "__main__":
    main()

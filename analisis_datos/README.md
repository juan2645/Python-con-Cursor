# Script de Análisis de Datos

Este script lee archivos de datos (Excel o CSV) y calcula estadísticas descriptivas básicas.

## Características

- **Lectura automática** de archivos Excel (.xlsx, .xls) y CSV
- **Cálculo de estadísticas** para cada columna numérica:
  - Media
  - Mediana
  - Desviación estándar
  - Mínimo y máximo
  - Cantidad de datos válidos
- **Información del dataset**: dimensiones, tipos de datos, valores faltantes
- **Interfaz amigable** con salida formateada

## Instalación

1. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

O instalar manualmente:
```bash
pip install pandas numpy openpyxl
```

## Uso

1. Coloca tu archivo de datos (Excel o CSV) en el mismo directorio que `analisis.py`
2. Ejecuta el script:
```bash
python analisis.py
```

El script automáticamente:
- Detecta archivos de datos en el directorio
- Lee el primer archivo encontrado
- Muestra información general del dataset
- Calcula y muestra estadísticas descriptivas

## Ejemplo de salida

```
Archivos de datos encontrados:
1. Datos.xlsx

Analizando archivo: Datos.xlsx
Archivo leído exitosamente: Datos.xlsx
Dimensiones del dataset: 11 filas, 2 columnas

============================================================
INFORMACIÓN DEL DATASET
============================================================
Dimensiones: 11 filas × 2 columnas
Memoria utilizada: 0.30 KB

Tipos de datos:
Ingresos    float64
Gastos      float64
dtype: object

Primeras 5 filas:
   Ingresos  Gastos
0       2.1     1.8
1       1.8     1.5
2       2.3     2.0
3       1.9     1.7
4       2.0     1.9

============================================================
ESTADÍSTICAS DESCRIPTIVAS
============================================================
           Media  Mediana  Desviación Estándar  Mínimo  Máximo  Cantidad de datos
Ingresos  1.9364      2.0               0.4105     1.2     2.5               11.0
Gastos    1.6545      1.8               0.4503     0.7     2.1               11.0
```

## Funciones principales

- `leer_datos(archivo)`: Lee archivos Excel o CSV
- `calcular_estadisticas(df)`: Calcula estadísticas para columnas numéricas
- `mostrar_info_dataset(df)`: Muestra información general del dataset
- `main()`: Función principal que coordina todo el análisis

## Requisitos

- Python 3.7+
- pandas
- numpy
- openpyxl (para archivos Excel) 
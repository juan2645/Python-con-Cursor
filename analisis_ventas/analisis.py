import pandas as pd

def cargar_datos():
    """
    Carga los datos del archivo CSV de ventas
    """
    try:
        # Cargar el archivo CSV
        df = pd.read_csv('ventas.csv')
        
        # Convertir la columna fecha a datetime
        df['fecha'] = pd.to_datetime(df['fecha'])
        
        # Calcular el total de ventas por transacción
        df['total_venta'] = df['cantidad'] * df['precio']
        
        print("Datos cargados exitosamente!")
        print(f"Total de registros: {len(df)}")
        print(f"Columnas: {list(df.columns)}")
        
        return df
    
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'ventas.csv'")
        return None
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

def calcular_ventas_por_mes(df):
    """
    Calcula las ventas totales por mes
    """
    if df is None:
        print("No hay datos para analizar")
        return
    
    # Crear columna de mes
    df['mes'] = df['fecha'].dt.to_period('M')
    
    # Agrupar por mes y sumar ventas totales
    ventas_por_mes = df.groupby('mes')['total_venta'].sum().round(2)
    
    print("\n=== VENTAS TOTALES POR MES ===")
    print(ventas_por_mes)
    
    return ventas_por_mes

# Cargar los datos
datos = cargar_datos()

if datos is not None:
    print("\nPrimeras 5 filas:")
    print(datos.head())
    
    # Calcular ventas por mes
    ventas_mensuales = calcular_ventas_por_mes(datos)

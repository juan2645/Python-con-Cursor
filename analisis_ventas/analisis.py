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

def analizar_productos(df):
    """
    Analiza el producto más vendido y el que genera mayores ingresos
    """
    if df is None:
        print("No hay datos para analizar")
        return
    
    # Agrupar por producto y calcular métricas
    analisis_productos = df.groupby('producto').agg({
        'cantidad': 'sum',
        'total_venta': 'sum',
        'precio': 'mean'
    }).round(2)
    
    analisis_productos.columns = ['Cantidad Total', 'Ingresos Totales ($)', 'Precio Promedio ($)']
    
    print("\n=== ANÁLISIS POR PRODUCTO ===")
    print(analisis_productos)
    
    # Encontrar el producto más vendido (por cantidad)
    producto_mas_vendido = analisis_productos['Cantidad Total'].idxmax()
    cantidad_maxima = analisis_productos['Cantidad Total'].max()
    
    # Encontrar el producto con mayores ingresos
    producto_mayores_ingresos = analisis_productos['Ingresos Totales ($)'].idxmax()
    ingresos_maximos = analisis_productos['Ingresos Totales ($)'].max()
    
    print(f"\n📊 PRODUCTO MÁS VENDIDO:")
    print(f"   Producto: {producto_mas_vendido}")
    print(f"   Cantidad total: {cantidad_maxima} unidades")
    
    print(f"\n💰 PRODUCTO CON MAYORES INGRESOS:")
    print(f"   Producto: {producto_mayores_ingresos}")
    print(f"   Ingresos totales: ${ingresos_maximos}")
    
    return analisis_productos

# Cargar los datos
datos = cargar_datos()

if datos is not None:
    print("\nPrimeras 5 filas:")
    print(datos.head())
    
    # Calcular ventas por mes
    ventas_mensuales = calcular_ventas_por_mes(datos)
    
    # Analizar productos
    analisis_productos = analizar_productos(datos)

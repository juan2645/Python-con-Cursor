import pandas as pd
import matplotlib.pyplot as plt

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

def graficar_ventas_por_mes(ventas_por_mes):
    """
    Crea un gráfico de las ventas por mes
    """
    if ventas_por_mes is None or ventas_por_mes.empty:
        print("No hay datos para graficar")
        return
    
    # Configurar el gráfico
    plt.figure(figsize=(10, 6))
    
    # Crear el gráfico de barras
    meses = [str(mes) for mes in ventas_por_mes.index]
    ventas = ventas_por_mes.values
    
    plt.bar(meses, ventas, color='#4ECDC4', alpha=0.7, edgecolor='black')
    
    # Personalizar el gráfico
    plt.title('Ventas Totales por Mes', fontsize=16, fontweight='bold')
    plt.xlabel('Mes', fontsize=12)
    plt.ylabel('Ventas Totales ($)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    # Agregar valores en las barras
    for i, v in enumerate(ventas):
        plt.text(i, v + 50, f'${v}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.show()

def graficar_top_productos_por_ingresos(df):
    """
    Crea un gráfico del top 5 de productos por ingresos
    """
    if df is None:
        print("No hay datos para graficar")
        return
    
    # Calcular ingresos por producto
    ingresos_por_producto = df.groupby('producto')['total_venta'].sum().sort_values(ascending=False)
    
    # Tomar los top 5 (o todos si hay menos de 5)
    top_productos = ingresos_por_producto.head(5)
    
    print(f"\n=== TOP {len(top_productos)} PRODUCTOS POR INGRESOS ===")
    print(top_productos)
    
    # Configurar el gráfico
    plt.figure(figsize=(10, 6))
    
    # Crear el gráfico de barras horizontales
    productos = top_productos.index
    ingresos = top_productos.values
    colores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFE66D']
    
    plt.barh(productos, ingresos, color=colores[:len(productos)], alpha=0.8, edgecolor='black')
    
    # Personalizar el gráfico
    plt.title(f'Top {len(top_productos)} Productos por Ingresos', fontsize=16, fontweight='bold')
    plt.xlabel('Ingresos Totales ($)', fontsize=12)
    plt.ylabel('Producto', fontsize=12)
    plt.grid(True, alpha=0.3, axis='x')
    
    # Agregar valores en las barras
    for i, v in enumerate(ingresos):
        plt.text(v + 50, i, f'${v}', ha='left', va='center', fontweight='bold')
    
    plt.tight_layout()
    plt.show()

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
    
    # Graficar ventas por mes
    print("\nGenerando gráfico de ventas por mes...")
    graficar_ventas_por_mes(ventas_mensuales)
    
    # Graficar top productos por ingresos
    print("\nGenerando gráfico de top productos por ingresos...")
    graficar_top_productos_por_ingresos(datos)
    
    # Analizar productos
    analisis_productos = analizar_productos(datos)

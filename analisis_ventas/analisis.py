import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos():
    """
    Carga los datos del archivo CSV de ventas con mejor manejo de tipos
    """
    try:
        # Cargar el archivo CSV con parse_dates para la fecha
        df = pd.read_csv('ventas.csv', parse_dates=['fecha'])
        
        # Verificar y convertir tipos de datos
        print("=== VERIFICACIÓN DE TIPOS DE DATOS ===")
        print("Tipos antes de la conversión:")
        print(df.dtypes)
        
        # Asegurar que cantidad y precio sean numéricos
        df['cantidad'] = pd.to_numeric(df['cantidad'], errors='coerce')
        df['precio'] = pd.to_numeric(df['precio'], errors='coerce')
        
        # Calcular el total de ventas por transacción
        df['total_venta'] = df['cantidad'] * df['precio']
        
        print("\nTipos después de la conversión:")
        print(df.dtypes)
        
        print("\nDatos cargados exitosamente!")
        print(f"Total de registros: {len(df)}")
        print(f"Columnas: {list(df.columns)}")
        print(f"Rango de fechas: {df['fecha'].min().strftime('%Y-%m-%d')} a {df['fecha'].max().strftime('%Y-%m-%d')}")
        
        # Verificar si hay valores nulos
        nulos = df.isnull().sum()
        if nulos.sum() > 0:
            print(f"\n⚠️ Valores nulos encontrados:")
            print(nulos[nulos > 0])
        else:
            print("\n✅ No hay valores nulos en el dataset")
        
        return df
    
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'ventas.csv'")
        return None
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

def calcular_ventas_por_mes(df):
    """
    Calcula las ventas totales por mes usando método más eficiente
    """
    if df is None:
        print("No hay datos para analizar")
        return
    
    # Crear columna de mes usando to_period
    df['mes'] = df['fecha'].dt.to_period('M')
    
    # Calcular ventas por mes de forma más directa
    ventas_por_mes = df.groupby('mes')['total_venta'].sum()
    
    # Ordenar por índice (mes)
    ventas_por_mes = ventas_por_mes.sort_index()
    
    print("\n=== VENTAS TOTALES POR MES ===")
    print("Ventas por mes:")
    print(ventas_por_mes)
    
    # Mostrar también en formato tabla
    print("\nFormato tabla:")
    print(ventas_por_mes.to_frame(name='Ventas Totales ($)'))
    
    return ventas_por_mes

def graficar_ventas_por_mes(ventas_por_mes):
    """
    Crea un gráfico de las ventas por mes usando matplotlib
    """
    if ventas_por_mes is None or ventas_por_mes.empty:
        print("No hay datos para graficar")
        return
    
    # Convertir el índice Period a string para mejor manejo
    ventas_por_mes.index = ventas_por_mes.index.astype(str)
    
    # Configurar el gráfico
    plt.figure(figsize=(10, 6))
    
    # Crear el gráfico de barras
    ventas_por_mes.plot(kind='bar', color='#4ECDC4', alpha=0.7, edgecolor='black')
    
    # Personalizar el gráfico
    plt.title("Ventas por Mes", fontsize=16, fontweight='bold')
    plt.xlabel("Mes", fontsize=12)
    plt.ylabel("Ventas ($)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    # Agregar valores en las barras
    for i, v in enumerate(ventas_por_mes.values):
        plt.text(i, v + 50, f'${v}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    
    # Guardar el gráfico
    plt.savefig("ventas_por_mes.png", dpi=300, bbox_inches='tight')
    print("✅ Gráfico guardado como 'ventas_por_mes.png'")
    
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
    
    # Calcular ingresos por transacción (ya lo tenemos como total_venta)
    # df['ingreso'] = df['cantidad'] * df['precio']  # Ya calculado como total_venta
    
    # Agrupar por producto y calcular métricas
    ventas_prod = df.groupby('producto').agg({
        'cantidad': 'sum',
        'total_venta': 'sum',  # Usamos total_venta que ya es cantidad * precio
        'precio': 'mean'  # Precio promedio por producto
    }).round(2)
    
    ventas_prod.columns = ['Cantidad Total', 'Ingresos Totales ($)', 'Precio Promedio ($)']
    
    print("\n=== ANÁLISIS POR PRODUCTO ===")
    print(ventas_prod)
    
    # Encontrar el producto más vendido (por cantidad)
    mas_vendido = ventas_prod['Cantidad Total'].idxmax()
    cantidad_maxima = ventas_prod.loc[mas_vendido, 'Cantidad Total']
    
    # Encontrar el producto con mayores ingresos
    mayor_ingreso = ventas_prod['Ingresos Totales ($)'].idxmax()
    ingresos_maximos = ventas_prod.loc[mayor_ingreso, 'Ingresos Totales ($)']
    
    print(f"\n📊 PRODUCTO MÁS VENDIDO (por cantidad):")
    print(f"   Producto: {mas_vendido}")
    print(f"   Cantidad total: {cantidad_maxima} unidades")
    print(f"   Ingresos generados: ${ventas_prod.loc[mas_vendido, 'Ingresos Totales ($)']:.2f}")
    
    print(f"\n💰 PRODUCTO CON MAYORES INGRESOS:")
    print(f"   Producto: {mayor_ingreso}")
    print(f"   Ingresos totales: ${ingresos_maximos:.2f}")
    print(f"   Cantidad vendida: {ventas_prod.loc[mayor_ingreso, 'Cantidad Total']} unidades")
    
    # Comparación y análisis
    print(f"\n🔍 ANÁLISIS COMPARATIVO:")
    if mas_vendido == mayor_ingreso:
        print(f"   ✅ El producto más vendido también genera mayores ingresos")
    else:
        print(f"   ⚠️ Diferencia entre más vendido y mayor ingreso:")
        print(f"      - Más vendido: {mas_vendido} ({cantidad_maxima} unidades)")
        print(f"      - Mayor ingreso: {mayor_ingreso} (${ingresos_maximos:.2f})")
        
        # Calcular diferencia en ingresos
        ingresos_mas_vendido = ventas_prod.loc[mas_vendido, 'Ingresos Totales ($)']
        diferencia = ingresos_maximos - ingresos_mas_vendido
        print(f"      - Diferencia en ingresos: ${diferencia:.2f}")
    
    return ventas_prod

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

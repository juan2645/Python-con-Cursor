import pandas as pd

def cargar_datos():
    """
    Carga los datos del archivo CSV de ventas
    """
    try:
        # Cargar el archivo CSV
        df = pd.read_csv('ventas.csv')
        
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

# Cargar los datos
datos = cargar_datos()

if datos is not None:
    print("\nPrimeras 5 filas:")
    print(datos.head())

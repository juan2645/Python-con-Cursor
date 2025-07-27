import re

def contar_palabras(texto):
    """
    Cuenta las palabras en un texto dado.
    
    Args:
        texto (str): El texto del cual contar las palabras
        
    Returns:
        int: El número total de palabras en el texto
    """
    if not texto or not texto.strip():
        return 0
    
    # Usar regex para encontrar todas las palabras
    palabras = re.findall(r'\w+', texto.lower())
    return len(palabras)

def contar_lineas(texto):
    """
    Cuenta las líneas en un texto dado.
    
    Args:
        texto (str): El texto del cual contar las líneas
        
    Returns:
        int: El número total de líneas en el texto
    """
    if not texto:
        return 0
    
    lineas = texto.split('\n')
    return len(lineas)

# Código principal para procesar archivos
if __name__ == "__main__":
    archivo = input("Introduce la ruta del archivo de texto: ")
    try:
        with open(archivo, "r", encoding='utf-8') as f:
            contenido = f.read()
            
            num_lineas = contar_lineas(contenido)
            num_palabras = contar_palabras(contenido)
            
            print(f"El archivo tiene {num_lineas} líneas.")
            print(f"Total palabras: {num_palabras}")
            
    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print(f"Error: {e}")







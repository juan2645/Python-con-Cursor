def generar_cuadrados(n):
    """
    Genera una lista con los cuadrados de los primeros n números naturales.
    
    Args:
        n (int): Número de elementos a generar
        
    Returns:
        list: Lista con los cuadrados de los números del 1 al n
    """
    return [i**2 for i in range(1, n + 1)]

def generar_cuadrados_tradicional(n):
    """
    Versión tradicional usando un bucle for.
    """
    cuadrados = []
    for i in range(1, n + 1):
        cuadrados.append(i**2)
    return cuadrados

def generar_cuadrados_map(n):
    """
    Versión usando map().
    """
    return list(map(lambda x: x**2, range(1, n + 1)))

def cuadrados(n):
    """
    Genera una lista con los cuadrados de los primeros n números naturales.
    
    Args:
        n (int): Número de elementos a generar
        
    Returns:
        list: Lista con los cuadrados de los números del 1 al n
    """
    return [i**2 for i in range(1, n + 1)]

# Ejemplo de uso
if __name__ == "__main__":
    # Pedir al usuario el valor de n
    try:
        n = int(input("Ingrese el número de elementos (n): "))
        if n <= 0:
            print("Por favor ingrese un número positivo.")
        else:
            # Generar la lista usando el método principal
            lista_cuadrados = generar_cuadrados(n)
            print(f"Lista con los cuadrados de los primeros {n} números naturales:")
            print(lista_cuadrados)
            
            # Mostrar también los otros métodos
            print(f"\nMétodo tradicional: {generar_cuadrados_tradicional(n)}")
            print(f"Método con map: {generar_cuadrados_map(n)}")
            
            # Mostrar cada número y su cuadrado
            print(f"\nDesglose:")
            for i, cuadrado in enumerate(lista_cuadrados, 1):
                print(f"{i}² = {cuadrado}")
                
    except ValueError:
        print("Por favor ingrese un número válido.")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")

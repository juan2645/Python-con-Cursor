# Programa para determinar si un número es primo
# Un número primo es aquel que solo es divisible por 1 y por sí mismo

def es_primo_basico(n):
    """
    Función básica para determinar si un número es primo
    """
    # Los números menores a 2 no son primos
    if n < 2:
        return False
    
    # Verificar divisibilidad desde 2 hasta n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

def es_primo_optimizado(n):
    """
    Función optimizada para determinar si un número es primo
    Solo verifica hasta la raíz cuadrada del número
    """
    # Los números menores a 2 no son primos
    if n < 2:
        return False
    
    # 2 es el único número primo par
    if n == 2:
        return True
    
    # Los números pares mayores a 2 no son primos
    if n % 2 == 0:
        return False
    
    # Verificar divisibilidad por números impares hasta la raíz cuadrada
    import math
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def mostrar_primos_hasta(limite):
    """
    Muestra todos los números primos hasta un límite dado
    """
    primos = []
    for i in range(2, limite + 1):
        if es_primo_optimizado(i):
            primos.append(i)
    return primos

# Función principal para interactuar con el usuario
def main():
    print("=== DETERMINADOR DE NÚMEROS PRIMOS ===")
    print()
    
    while True:
        try:
            # Solicitar número al usuario
            numero = input("Ingrese un número para verificar si es primo (o 'q' para salir): ")
            
            if numero.lower() == 'q':
                print("¡Hasta luego!")
                break
            
            numero = int(numero)
            
            # Verificar si es primo usando ambas funciones
            es_primo_basico_resultado = es_primo_basico(numero)
            es_primo_optimizado_resultado = es_primo_optimizado(numero)
            
            print(f"\nResultado para el número {numero}:")
            print(f"Función básica: {'Es primo' if es_primo_basico_resultado else 'No es primo'}")
            print(f"Función optimizada: {'Es primo' if es_primo_optimizado_resultado else 'No es primo'}")
            
            # Mostrar algunos ejemplos
            if numero > 0:
                print(f"\nNúmeros primos hasta {min(numero, 50)}:")
                primos_hasta_n = mostrar_primos_hasta(min(numero, 50))
                print(primos_hasta_n)
            
            print("\n" + "="*50)
            
        except ValueError:
            print("Error: Por favor ingrese un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break

# Ejecutar el programa si se ejecuta directamente
if __name__ == "__main__":
    main()

# Ejemplos de uso:
print("\n=== EJEMPLOS DE USO ===")
ejemplos = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print("Números primos del 1 al 100:")
for num in ejemplos:
    print(f"{num} es primo: {es_primo_optimizado(num)}")

print("\nNúmeros no primos del 1 al 20:")
for num in range(1, 21):
    if not es_primo_optimizado(num):
        print(f"{num} no es primo")

# Información adicional sobre números primos
print("\n=== INFORMACIÓN ADICIONAL ===")
print("• El 1 NO es considerado un número primo")
print("• El 2 es el único número primo par")
print("• Todos los demás números primos son impares")
print("• Los números primos son infinitos (demostrado por Euclides)")
print("• Los números primos son fundamentales en criptografía") 
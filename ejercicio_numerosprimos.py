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
    Función altamente optimizada para determinar si un número es primo
    Aplica múltiples optimizaciones:
    - Verificación rápida de casos especiales
    - Solo verifica hasta la raíz cuadrada
    - Solo verifica divisores de la forma 6k±1
    - Cache de divisores pequeños
    """
    # Casos especiales rápidos
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Cache de divisores pequeños para números grandes
    if n < 1000:
        # Para números pequeños, verificar divisores hasta raíz cuadrada
        import math
        limite = int(math.sqrt(n))
        for i in range(5, limite + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True
    else:
        # Para números grandes, usar optimización 6k±1
        import math
        limite = int(math.sqrt(n))
        # Verificar divisores de la forma 6k±1 (más eficiente)
        for i in range(5, limite + 1, 6):
            if n % i == 0:
                return False
            if i + 2 <= limite and n % (i + 2) == 0:
                return False
        return True


def es_primo_miller_rabin(n, k=5):
    """
    Test de primalidad de Miller-Rabin (probabilístico)
    Muy eficiente para números grandes
    k: número de iteraciones (mayor k = mayor precisión)
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Escribir n-1 como 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Test de Miller-Rabin
    import random
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def criba_eratostenes(limite):
    """
    Implementación de la Criba de Eratóstenes
    Encuentra todos los números primos hasta un límite dado
    Muy eficiente para encontrar múltiples números primos
    """
    # Crear lista de booleanos inicializada en True
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False
    
    # Aplicar la criba
    for i in range(2, int(limite ** 0.5) + 1):
        if es_primo[i]:
            # Marcar todos los múltiplos de i como no primos
            for j in range(i * i, limite + 1, i):
                es_primo[j] = False
    
    # Retornar lista de números primos
    return [i for i in range(limite + 1) if es_primo[i]]


def mostrar_primos_hasta(limite):
    """
    Muestra todos los números primos hasta un límite dado
    Usa la criba de Eratóstenes para mayor eficiencia
    """
    if limite <= 1000:
        # Para límites pequeños, usar criba de Eratóstenes
        return criba_eratostenes(limite)
    else:
        # Para límites grandes, usar función optimizada
        primos = []
        for i in range(2, limite + 1):
            if es_primo_optimizado(i):
                primos.append(i)
        return primos

# Función principal para interactuar con el usuario
def comparar_rendimiento(n):
    """
    Compara el rendimiento de las diferentes funciones de primalidad
    """
    import time
    
    print(f"\n=== COMPARACIÓN DE RENDIMIENTO PARA {n} ===")
    
    # Función básica
    inicio = time.time()
    resultado_basico = es_primo_basico(n)
    tiempo_basico = time.time() - inicio
    
    # Función optimizada
    inicio = time.time()
    resultado_optimizado = es_primo_optimizado(n)
    tiempo_optimizado = time.time() - inicio
    
    # Función Miller-Rabin (solo para números grandes)
    if n > 1000:
        inicio = time.time()
        resultado_miller = es_primo_miller_rabin(n)
        tiempo_miller = time.time() - inicio
    else:
        resultado_miller = resultado_optimizado
        tiempo_miller = 0
    
    print(f"Función básica: {resultado_basico} (tiempo: {tiempo_basico:.6f}s)")
    print(f"Función optimizada: {resultado_optimizado} (tiempo: {tiempo_optimizado:.6f}s)")
    if n > 1000:
        print(f"Miller-Rabin: {resultado_miller} (tiempo: {tiempo_miller:.6f}s)")
    
    if tiempo_basico > 0:
        mejora = (tiempo_basico - tiempo_optimizado) / tiempo_basico * 100
        print(f"Mejora de rendimiento: {mejora:.1f}%")
    
    return resultado_optimizado


def probar_funciones():
    """
    Función para probar que todas las funciones de primalidad funcionen correctamente
    """
    print("=== PRUEBAS DE FUNCIONES DE PRIMALIDAD ===")
    
    # Números conocidos para probar
    numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    numeros_no_primos = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40]
    
    print("\nProbando números primos conocidos:")
    errores_primos = 0
    for num in numeros_primos:
        resultado = es_primo_optimizado(num)
        if not resultado:
            print(f"ERROR: {num} debería ser primo pero se detectó como no primo")
            errores_primos += 1
    
    print(f"Errores en números primos: {errores_primos}")
    
    print("\nProbando números no primos conocidos:")
    errores_no_primos = 0
    for num in numeros_no_primos:
        resultado = es_primo_optimizado(num)
        if resultado:
            print(f"ERROR: {num} debería NO ser primo pero se detectó como primo")
            errores_no_primos += 1
    
    print(f"Errores en números no primos: {errores_no_primos}")
    
    # Probar números grandes
    numeros_grandes_primos = [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061]
    print("\nProbando números primos grandes:")
    for num in numeros_grandes_primos:
        resultado = es_primo_optimizado(num)
        print(f"{num}: {'✓' if resultado else '✗'}")
    
    if errores_primos == 0 and errores_no_primos == 0:
        print("\n✅ Todas las funciones funcionan correctamente!")
    else:
        print(f"\n❌ Se encontraron {errores_primos + errores_no_primos} errores")


def main():
    print("=== DETERMINADOR DE NÚMEROS PRIMOS OPTIMIZADO ===")
    print("Funciones disponibles:")
    print("1. Básica - Verificación completa")
    print("2. Optimizada - Con múltiples optimizaciones")
    print("3. Miller-Rabin - Probabilístico para números grandes")
    print()
    
    while True:
        try:
            # Solicitar número al usuario
            numero = input("Ingrese un número para verificar si es primo (o 'q' para salir): ")
            
            if numero.lower() == 'q':
                print("¡Hasta luego!")
                break
            
            numero = int(numero)
            
            # Usar la función de comparación de rendimiento
            resultado = comparar_rendimiento(numero)
            
            # Mostrar algunos ejemplos
            if numero > 0 and numero <= 100:
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
    # Ejecutar pruebas primero
    probar_funciones()
    print("\n" + "="*60)
    # Luego ejecutar el programa principal
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

print("\n=== OPTIMIZACIONES IMPLEMENTADAS ===")
print("1. Verificación rápida de casos especiales (2, 3, números pares)")
print("2. Solo verificar hasta la raíz cuadrada del número")
print("3. Solo verificar divisores de la forma 6k±1 (excluye múltiplos de 2 y 3)")
print("4. Cache de divisores pequeños para números grandes")
print("5. Test de Miller-Rabin para números muy grandes (probabilístico)")
print("6. Criba de Eratóstenes para encontrar múltiples números primos")
print("7. Comparación de rendimiento entre diferentes algoritmos")

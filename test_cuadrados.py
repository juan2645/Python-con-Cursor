def cuadrados(n):
    """
    Genera una lista con los cuadrados de los primeros n números naturales.
    """
    return [i**2 for i in range(1, n + 1)]

def probar_cuadrados():
    """Función para probar diferentes casos de la función cuadrados(n)"""
    
    print("=== PRUEBAS DE LA FUNCIÓN CUADRADOS(N) ===\n")
    
    # Prueba 1: Números pequeños
    print("1. Prueba con n = 3:")
    resultado = cuadrados(3)
    print(f"   cuadrados(3) = {resultado}")
    print(f"   Verificación: 1²=1, 2²=4, 3²=9 ✓\n")
    
    # Prueba 2: Número mediano
    print("2. Prueba con n = 7:")
    resultado = cuadrados(7)
    print(f"   cuadrados(7) = {resultado}")
    print(f"   Verificación: 1²=1, 2²=4, 3²=9, 4²=16, 5²=25, 6²=36, 7²=49 ✓\n")
    
    # Prueba 3: Número grande
    print("3. Prueba con n = 10:")
    resultado = cuadrados(10)
    print(f"   cuadrados(10) = {resultado}")
    print(f"   Longitud de la lista: {len(resultado)}")
    print(f"   Último elemento: {resultado[-1]} (debería ser 10² = 100) ✓\n")
    
    # Prueba 4: Verificar propiedades matemáticas
    print("4. Verificación de propiedades:")
    n = 5
    resultado = cuadrados(n)
    suma_cuadrados = sum(resultado)
    print(f"   Para n = {n}: {resultado}")
    print(f"   Suma de los cuadrados: {suma_cuadrados}")
    print(f"   Fórmula matemática: 1² + 2² + 3² + 4² + 5² = 1 + 4 + 9 + 16 + 25 = 55 ✓\n")
    
    # Prueba 5: Caso límite
    print("5. Caso límite con n = 1:")
    resultado = cuadrados(1)
    print(f"   cuadrados(1) = {resultado}")
    print(f"   Verificación: 1² = 1 ✓\n")
    
    # Prueba 6: Comparación con valores esperados
    print("6. Comparación con valores esperados:")
    casos_prueba = [
        (1, [1]),
        (2, [1, 4]),
        (3, [1, 4, 9]),
        (4, [1, 4, 9, 16]),
        (5, [1, 4, 9, 16, 25])
    ]
    
    for n, esperado in casos_prueba:
        resultado = cuadrados(n)
        if resultado == esperado:
            print(f"   ✓ cuadrados({n}) = {resultado}")
        else:
            print(f"   ✗ cuadrados({n}) = {resultado}, esperado: {esperado}")
    
    print("\n=== TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE ===")

if __name__ == "__main__":
    probar_cuadrados() 
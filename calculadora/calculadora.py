def calculadora():
    """
    Calculadora simple que permite realizar operaciones básicas:
    suma, resta, multiplicación y división.
    El programa se ejecuta hasta que el usuario escriba "salir".
    """
    
    print("=== CALCULADORA SIMPLE ===")
    print("Operaciones disponibles: suma, resta, multiplicación, división")
    print("Escribe 'salir' para terminar el programa")
    print("-" * 40)
    
    while True:
        # Solicitar operación al usuario
        operacion = input("\nIngresa la operación (suma/resta/multiplicación/división/salir): ").lower().strip()
        
        # Verificar si el usuario quiere salir
        if operacion == "salir":
            print("¡Gracias por usar la calculadora!")
            break
        
        # Validar que la operación sea válida
        operaciones_validas = ["suma", "resta", "multiplicación", "división"]
        if operacion not in operaciones_validas:
            print("❌ Operación no válida. Por favor, ingresa una operación válida.")
            continue
        
        # Solicitar los dos números
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("❌ Error: Por favor, ingresa números válidos.")
            continue
        
        # Realizar la operación según la selección del usuario
        resultado = None
        
        if operacion == "suma":
            resultado = num1 + num2
            simbolo = "+"
        elif operacion == "resta":
            resultado = num1 - num2
            simbolo = "-"
        elif operacion == "multiplicación":
            resultado = num1 * num2
            simbolo = "*"
        elif operacion == "división":
            if num2 == 0:
                print("❌ Error: No se puede dividir por cero.")
                continue
            resultado = num1 / num2
            simbolo = "/"
        
        # Mostrar el resultado
        print(f"\n✅ Resultado: {num1} {simbolo} {num2} = {resultado}")
        print("-" * 40)

# Ejecutar la calculadora si el archivo se ejecuta directamente
if __name__ == "__main__":
    calculadora()

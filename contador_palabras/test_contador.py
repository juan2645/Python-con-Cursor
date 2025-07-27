import unittest
from contador import contar_palabras

def test_contar_palabras():
    """Test simple para la función contar_palabras"""
    
    # Test 1: Texto vacío
    assert contar_palabras("") == 0, "Texto vacío debe retornar 0"
    
    # Test 2: Texto simple
    assert contar_palabras("hola mundo") == 2, "Debe contar 2 palabras"
    
    # Test 3: Texto con puntuación
    assert contar_palabras("¡Hola, mundo!") == 2, "Debe ignorar puntuación"
    
    # Test 4: Texto con números
    assert contar_palabras("Python 3.9") == 2, "Debe contar números como palabras"
    
    # Test 5: Texto con espacios extra
    assert contar_palabras("  hola  mundo  ") == 2, "Debe ignorar espacios extra"
    
    print("✅ Todos los tests pasaron correctamente!")

if __name__ == "__main__":
    test_contar_palabras() 
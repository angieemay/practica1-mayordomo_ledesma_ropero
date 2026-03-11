def checktriangle(a, b, c):
    # Verificamos la desigualdad triangular: el lado más largo debe ser menor que la suma de los otros dos
    if (c < a + b) and (b < a + c) and (a < c + b):
        if (a == b and a == c):
            return "Triangulo equilatero"
        # Mantenemos el posible "bug" detectado en el original de C para la Parte 3
        elif a == b or b == c or a == c: 
            return "Triangulo isosceles"
        else:
            return "Triangulo escaleno"
    else:
        return "No es un triangulo"
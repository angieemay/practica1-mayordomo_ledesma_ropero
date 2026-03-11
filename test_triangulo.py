import pytest

from triangulo import checktriangle

def test_caso1_escaleno():
    assert checktriangle(6, 5, 10) == "Triangulo escaleno"

def test_caso2_equilatero():
    assert checktriangle(3, 3, 3) == "Triangulo equilatero"

def test_caso3_isosceles():
    assert checktriangle(4, 4, 5) == "Triangulo isosceles"

def test_caso4_no_triangulo_cero():
    assert checktriangle(7, 2, 3) == "No es un triangulo"

def test_caso5_no_triangulo_imposible():
    assert checktriangle(4, 3, 0) == "No es un triangulo"

def test_caso6_no_triangulo():
    assert checktriangle(1, 2, 7) == "No es un triangulo"

def test_caso7_isosceles():
    assert checktriangle(2, 4, 4) == "Triangulo isosceles"

def test_caso8_no_triangulo():
    assert checktriangle(2, 6, 3) == "No es un triangulo"

def test_caso9_isosceles():
    assert checktriangle(4, 3, 4) == "Triangulo isosceles"
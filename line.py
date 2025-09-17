def line():
import math
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    x1 = float(input("Ingrese el coeficiente X1: "))
    x2 = float(input("Ingrese el coeficiente X2: "))

    y1 = A * x1 + B
    y2 = A * x2 + B
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"El coeficiente A de su ecuación de la recta es: {A}")
    print(f"El coeficiente B de su ecuación de la recta es: {B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {x2}")

    print("\nPara la siguiente ecuación:")
    print(f"\tY = {A}X + {B}")

    print("\nDados los siguientes puntos:")
    print(f"\tP1 ({x1}, {y1})")
    print(f"\tP2 ({x2}, {y2})")
    print(f"\nLa distancia entre ellos es: {distancia}")
    
line()

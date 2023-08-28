import random

""" 
Genera 30 curvas de bezier aleatorias para testear
"""


def generate_point():
    """Genera un punto aleatorio (x,y) con valores entre -100 y 100."""
    x = random.uniform(-100, 100)
    y = random.uniform(-100, 100)
    return x, y

def generate_bezier_curve(id):
    """Genera una curva de Bézier cuadrática con tres puntos A, B y C y un valor t."""
    A = generate_point()
    B = generate_point()
    C = generate_point()
    t = random.uniform(0, 1)
    
    return f"{id}, {A[0]:.2f}, {A[1]:.2f}, {B[0]:.2f}, {B[1]:.2f}, {C[0]:.2f}, {C[1]:.2f}, {t:.2f}"

# Generar 30 curvas de Bézier y guardarlas en un archivo.
with open("bezier_curves.txt", "w") as f:
    for i in range(30):
        curve = generate_bezier_curve(i + 1) # Ids desde 1 hasta 30
        f.write(curve + '\n')

print("Archivo 'bezier_curves.txt' creado con 30 curvas de Bézier.")

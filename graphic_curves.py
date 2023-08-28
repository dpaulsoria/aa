import pandas as pd
import matplotlib.pyplot as plt
from metrics import composite_score, bezier_quadratic, hausdorff_distance, std_distance, area_between_curves, composite_score

"""
Grafica las curvas del bezier_curves.csv para visualizarlas
"""


def bezier_curve(t, A, B, C):
    """Calcula un punto en la curva de Bézier cuadrática basado en t y puntos de control A, B y C."""
    return ((1 - t)**2 * A) + (2 * (1 - t) * t * B) + (t**2 * C)

def plot_curves_from_csv(filename):
    """Lee el archivo .csv y grafica las curvas de Bézier cuadráticas."""
    df = pd.read_csv(filename)
    
    for index, row in df.iterrows():
        A = (row['Ax'], row['Ay'])
        B = (row['Bx'], row['By'])
        C = (row['Cx'], row['Cy'])
        t_val = row['t']
        
        # Valores de t para la curva
        ts = [i/100 for i in range(101)]
        
        # Calcular puntos de la curva
        x_vals = [bezier_curve(t, A[0], B[0], C[0]) for t in ts]
        y_vals = [bezier_curve(t, A[1], B[1], C[1]) for t in ts]
        
        plt.plot(x_vals, y_vals, label=f"ID: {int(row['id'])} (t={t_val:.2f})")
    
    plt.title("Curvas de Bézier cuadráticas")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.grid(True)
    plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)
    plt.tight_layout()
    plt.show()

# Usar la función para graficar las curvas desde un archivo "bezier_curves.csv"
plot_curves_from_csv("bezier_curves.csv")
# df = pd.read_csv("bezier_curves.csv")
# print(df.columns)
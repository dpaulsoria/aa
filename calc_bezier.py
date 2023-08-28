import pandas as pd
import numpy as np

from metrics import generate_curve_points, hausdorff_distance, std_distance, composite_score, area_between_curves

""" 
Calcula el valor de similitud entre la curva i y la curva i+1 hasta terminar el archivo bezier_curves.csv
"""

def process_csv(file_path):
    # Leemos el archivo .csv
    df = pd.read_csv(file_path)
    
    # Aseguramos que haya al menos 2 curvas
    if len(df) < 2:
        print("Se requieren al menos 2 curvas para calcular similitudes.")
        return
    
    # Procesamos cada par de curvas consecutivas
    for i in range(len(df) - 1):
        curve1_data = df.iloc[i]
        curve2_data = df.iloc[i+1]
        
        # Extraemos los puntos de las curvas
        P0_curve1 = (curve1_data['Ax'], curve1_data['Ay'])
        P1_curve1 = (curve1_data['Bx'], curve1_data['By'])
        P2_curve1 = (curve1_data['Cx'], curve1_data['Cy'])
        
        P0_curve2 = (curve2_data['Ax'], curve2_data['Ay'])
        P1_curve2 = (curve2_data['Bx'], curve2_data['By'])
        P2_curve2 = (curve2_data['Cx'], curve2_data['Cy'])

        # Generamos puntos a lo largo de las curvas
        curve1_points = generate_curve_points(P0_curve1, P1_curve1, P2_curve1)
        curve2_points = generate_curve_points(P0_curve2, P1_curve2, P2_curve2)
        
        # Calculamos métricas de similitud
        hd = hausdorff_distance(curve1_points, curve2_points)
        std = std_distance(curve1_points, curve2_points)
        area = area_between_curves(curve1_points, curve2_points)
        comp_score = composite_score(curve1_points, curve2_points)
        
        # Imprimimos los resultados
        print(f"Comparando Curva {curve1_data['id']} con Curva {curve2_data['id']}:")
        print(f"  Distancia de Hausdorff: {hd}")
        print(f"  Desviación estándar de la distancia: {std}")
        print(f"  Área entre las curvas: {area}")
        print(f"  Puntaje compuesto de similitud: {comp_score}")
        print("\n")

if __name__ == "__main__":
    file_path = "bezier_curves.csv"  # Cambia esto a la ubicación real del archivo .csv
    process_csv(file_path)

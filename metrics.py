import numpy as np
from scipy.spatial import distance

""" 
Metricas para calcular la similitud entre 2 curvas. 0 muy similares y 1 muy diferentes.
"""

def distance(point1, point2):
    """Calcula la distancia euclidiana entre dos puntos."""
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def hausdorff_distance(curve1, curve2):
    """Calcula la distancia de Hausdorff entre dos conjuntos de puntos."""
    return max([min([distance(p1, p2) for p2 in curve2]) for p1 in curve1])

def std_distance(curve1, curve2):
    """Calcula la desviación estándar de las distancias entre puntos de las curvas."""
    distances = [min([distance(p1, p2) for p2 in curve2]) for p1 in curve1]
    return np.std(distances)

def area_between_curves(curve1, curve2):
    """Calcula el área entre las dos curvas."""
    areas = [0.5 * distance(p1, p2) for p1, p2 in zip(curve1, curve2)]
    return sum(areas)

def composite_score(curve1, curve2):
    hd = hausdorff_distance(curve1, curve2)
    std = std_distance(curve1, curve2)
    area = area_between_curves(curve1, curve2)
    
    # Normalización (los valores máximos deberán ajustarse según tu contexto)
    max_distance = np.sqrt(2) * 200  # Diagonal de un cuadrado de 200x200
    hd_norm = hd / max_distance
    std_norm = std / max_distance
    area_norm = area / (200 * 100)  # Área de un rectángulo de 200x100
    
    return (hd_norm + std_norm + area_norm) / 3


def bezier_quadratic(P0, P1, P2, t):
    """Devuelve el punto de una curva de Bézier cuadrática en t."""
    x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t ** 2 * P2[0]
    y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t ** 2 * P2[1]
    return (x, y)

def generate_curve_points(P0, P1, P2, num_points=100):
    """Genera puntos a lo largo de una curva de Bézier cuadrática."""
    return [bezier_quadratic(P0, P1, P2, t) for t in np.linspace(0, 1, num_points)]

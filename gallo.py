import numpy as np

def dynamic_time_warping(curve1, curve2):
    n = len(curve1)
    m = len(curve2)
    
    dp = np.zeros((n + 1, m + 1))
    
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] + np.linalg.norm(curve1[i - 1] - curve2[0])
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] + np.linalg.norm(curve1[0] - curve2[j - 1])
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = np.linalg.norm(curve1[i - 1] - curve2[j - 1])
            dp[i][j] = cost + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    return dp[n][m]

def compare_curves_to_reference(reference_curve, curve, threshold=250):
    dtw_distance = dynamic_time_warping(reference_curve, curve)
    return dtw_distance <= threshold

def classify_curves_with_reference(reference_curve, curves, threshold=250):
    similar_curves = []
    different_curves = []
    
    for curve in curves:
        if compare_curves_to_reference(reference_curve, curve[1], threshold):
            similar_curves.append(curve[0])
        else:
            different_curves.append(curve[0])
    
    return similar_curves, different_curves

# Read curves from the input file
input_file = "bezier_curves.txt"
curves = []

with open(input_file, "r") as f:
    lines = f.readlines()
    for line in lines:
        values = line.strip().split(", ")
        curve_id = int(values[0])
        curve_points = np.array([float(val) for val in values[1:]])
        curves.append((curve_id, curve_points))

modelo = "-56.81, -57.25, -93.24, -70.27, -95.42, 1.61"
reference_curve = np.array([float(val.strip()) for val in modelo.split(",")])

similar_curves, different_curves = classify_curves_with_reference(reference_curve, curves)

with open("output.txt", "w") as f:
    f.write("Similar Curves: {}\n".format(similar_curves))
    f.write("Different Curves: {}\n".format(different_curves))
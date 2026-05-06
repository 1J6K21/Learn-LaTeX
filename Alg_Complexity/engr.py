import numpy as np

A = np.array([[2.5,-3,4,-1],[0,6,-4.5,8],[-2,0,0,5],[3,-4.7,1,0]])
print("A")
print(A)

A_inv = np.linalg.inv(A)
print("Inverse")
print(A_inv)

print("I")
print(A@A_inv) #I

B = np.array([15,-24,7,5])

X = A_inv@B
print(f"X\n{X}")

print(np.linalg.det(A))

A = np.array([[1,1],[0.037,0.074]])
B = np.array([323.2,14.478])
print(np.linalg.solve(A,B))

A = np.array([[1,1,1],[0.17,0.25,0.23],[0,1,0]])
A_inv = np.linalg.inv(A)
B = np.array([387,85.25,129])
print(A_inv.dot(B))

# Variables: x = [C, D, G, W]
# C: Clean gravel output (kg/min)
# D: Dirt in feed (kg/min)
# G: Clean gravel in feed (kg/min)
# W: Water in feed (kg/min)
# A = np.array([
#     [0, 1, 1, 1],          # Total Mass Balance
#     [0, 0.87, -0.13, 0],   # Dry Composition Ratio
#     [1, 4.3478, 0, 0],     # Dirt/Waste Output Balance
#     [-1, -0.0870, 1, 0]    # Gravel Balance
# ])

# A = np.array([
#     [0, 1, 1, 1],          # Total Mass Balance
#     [0, 0.87, -0.13, 0],   # Dry Composition Ratio
#     [-1, -0.087, 1, 0],    # Dirt/Waste Output Balance
#     [1,4.348,0,0],    # Gravel Balance
# ])

A = np.array([
    [0, 1, 1, 1],          # Total Mass Balance
    [0, 0.87, -0.13, 0],   # Dry Composition Ratio
    [0, 4.261, 1, 0],    # Dirt/Waste Output Balance
    [1,4.348,0,0],    # Gravel Balance
])

B = np.array([8, 0, 8, 8])

sol = np.linalg.solve(A, B)
print(f"solution: {sol}")
print(f"Clean product: {sol[0]/8}")
print(f"Dirt: {sol[1]/8}")
print(f"Clean in: {sol[2]/8}")
print(f"water: {sol[3]/8}")
print(f"clean out: {0.02*(sol[1]/8)/0.23 + sol[0]/8}")

# A = np.array([[1,-1],[0.0035,0]])
# B = np.array([0.288,0.288])
# print(np.linalg.solve(A, B))
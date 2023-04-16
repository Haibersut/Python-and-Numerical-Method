import numpy as np

A = np.array([
    [-2, 1, 0, 0],
    [1, -2, 1, 0],
    [0, 1, -2, 1],
    [0, 0, 1, -2]
])

A_inv = np.linalg.inv(A)

row_sum_norm_A = np.max(np.sum(np.abs(A), axis=1))
row_sum_norm_A_inv = np.max(np.sum(np.abs(A_inv), axis=1))

condition_number = row_sum_norm_A * row_sum_norm_A_inv

print("Row sum norm of A:", row_sum_norm_A)
print("Row sum norm of A^(-1):", row_sum_norm_A_inv)
print("Condition number:", condition_number)

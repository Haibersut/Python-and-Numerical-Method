import sympy as sp

A = sp.Matrix([
    [-2, 1, 0, 0],
    [1, -2, 1, 0],
    [0, 1, -2, 1],
    [0, 0, 1, -2]
])

A_inv = A.inv()

row_abs_sums_A = [sum(abs(row[i]) for i in range(A.cols)) for row in A.tolist()]
row_abs_sums_A_inv = [sum(abs(row[i]) for i in range(A_inv.cols)) for row in A_inv.tolist()]

row_sum_norm_A = max(row_abs_sums_A)
row_sum_norm_A_inv = max(row_abs_sums_A_inv)

condition_number = row_sum_norm_A * row_sum_norm_A_inv

print("Row sum norm of A:", row_sum_norm_A)
print("Row sum norm of A^(-1):", row_sum_norm_A_inv)
print("Condition number:", condition_number)
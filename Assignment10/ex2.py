import numpy as np


def matrix_stats(matrix: np.ndarray) -> dict:
    if matrix.ndim != 2:
        raise ValueError
    total_sum = matrix.sum()
    (row, column) = matrix.shape

    row_sum = np.empty(row, dtype=matrix.dtype)
    for i in range(row):
        row_sum[i] = matrix[i].sum()

    column_sum = np.empty(column, dtype=matrix.dtype)
    for i in range(column):
        column_sum[i] = matrix[:, i].sum()

    return dict(total_sum=total_sum, row_sums=row_sum, column_sums=column_sum)


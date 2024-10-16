import numpy as np

def max_pool_dp(matrix, k):
    """Perform max pooling using a dynamic programming approach."""
    m = matrix.shape[0]
    if k <= 0 or m == 0:
        return np.zeros((m, m))  # Return zero matrix if k is non-positive or matrix is empty
    
    # Step 1: Calculate row-wise max with a sliding window
    row_max = np.zeros((m+1, m - k + 2))
    for i in range(m):
        for j in range(m - k + 2):
            row_max[i, j] = np.max(matrix[i, j:j + k])
    
    # Step 2: Calculate column-wise max from row_max
    output_size = m
    output = np.zeros((output_size, output_size))
    for j in range(output_size):
        for i in range(output_size):
            output[i, j] = np.max(row_max[i:i + k, j])
    
    return output

# Example Usage
matrix = np.array([[1, 2, 3,4],
                   [5, 6, 7,8],
                   [9, 10, 11,12],
                   [13, 14, 15,16]])
k = 2
output = max_pool_dp(matrix, k)
print("Dynamic Programming Max Pooling Output:\n", output)

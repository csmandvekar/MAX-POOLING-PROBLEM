import numpy as np

# Function for max pooling with a moving window
def max_pool_basic(matrix, k):
    m = matrix.shape[0]
    output = np.zeros((m, m))
    
    for i in range(m):
        for j in range(m):
            # Define window boundaries
            row_start = max(i - k // 2, 0)
            row_end = min(i + k // 2 + 1, m)
            col_start = max(j - k // 2, 0)
            col_end = min(j + k // 2 + 1, m)
            
            # Extract window and find maximum
            window = matrix[row_start:row_end, col_start:col_end]
            output[i, j] = np.max(window)
    
    return output

# Example Usage
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
k = 2
output = max_pool_basic(matrix, k)
print("Basic Max Pooling Output:\n", output)

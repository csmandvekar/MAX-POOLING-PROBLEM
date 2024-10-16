# Max Pooling Optimization

## Overview

This project demonstrates two different implementations of the Max Pooling operation on a matrix:
1. **Basic Max Pooling Implementation**: A straightforward approach with a time complexity of **O(m² * k²)**.
2. **Optimized Max Pooling Using Dynamic Programming (DP)**: An improved version that reduces the time complexity to **O(m²)** by utilizing precomputed results for efficiency.

The purpose of this project is to compare both approaches in terms of performance and demonstrate how the DP approach enhances the computation.

## Files

- **max_pool_basic.py**: Contains the basic max pooling implementation with time complexity **O(m² * k²)**.
- **dp.py**: Contains the optimized dynamic programming-based max pooling implementation with time complexity **O(m²)**.

## How to Run

1. **Requirements**:
   - Python 3.x
   - NumPy library (install using `pip install numpy`)

2. **Steps to Run**:
   - Clone the repository or download the two Python files (`max_pool_basic.py` and `dp.py`).
   - Navigate to the directory where the files are located.
   - Run the basic max pooling implementation with the following command:
     ```bash
     python max_pool_basic.py
     ```
   - Run the optimized DP max pooling implementation with the following command:
     ```bash
     python dp.py
     ```

### Example Usage

By default, both implementations run on a sample 3x3 matrix with a window size of 2. To modify the input matrix or window size, simply change the values in the respective Python files:

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
k = 2  # Window size
```

### Custom Inputs

You can modify the `matrix` and `k` values directly in the code. Both files contain these variables, and you can input your own matrix and window size to test different scenarios.

## Validating Output and Runtime

Both implementations print the resulting max pooling matrix to the console. In addition to the output, you can also check the runtime performance by wrapping the function calls with timing code as shown:

```python
import time

start_time = time.time()
output = max_pool(matrix, k)
print("Execution Time: ", time.time() - start_time)
```

### Findings

- **Basic Max Pooling**: This approach computes the maximum value within each window individually, leading to a time complexity of **O(m² * k²)** where `m` is the dimension of the matrix and `k` is the size of the pooling window. It is simple but inefficient for larger matrices.
  
- **Dynamic Programming Approach**: The DP implementation reduces the redundant computation of overlapping windows by storing intermediate results and reusing them. This reduces the time complexity to **O(m²)**, making it significantly faster for larger matrices.

### Performance Comparison

You can observe a noticeable difference in performance, especially when running on larger matrices with bigger window sizes. The optimized DP version consistently outperforms the basic implementation due to its more efficient approach to handling overlapping windows.

---

### Conclusion

This project showcases the importance of optimizing algorithms for performance-sensitive tasks such as max pooling in machine learning and image processing. By comparing a naive approach with a dynamic programming solution, we highlight the significant improvements that can be achieved through algorithmic optimizations.

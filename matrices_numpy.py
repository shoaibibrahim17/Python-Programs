import numpy as np

def matrix_operations(A, B):
    # Check if matrices are compatible for addition
    if A.shape[1] == B.shape[0]:
        # Matrix Addition (if shapes match)
        try:
            matrix_sum = A + B
            print("Matrix Sum (A + B):\n", matrix_sum)
        except ValueError as e:
            print("Matrix addition not possible due to incompatible shapes:", e)
    
    # Check if matrices are compatible for multiplication
    if A.shape[1] == B.shape[0]:
        # Matrix Multiplication
        matrix_product = np.dot(A, B)
        print("Matrix Product (A * B):\n", matrix_product)
    else:
        print("Matrix multiplication not possible due to incompatible shapes.")

# Example usage
A = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3 matrix
B = np.array([[7, 8], [9, 10], [11, 12]])  # 3x2 matrix

matrix_operations(A, B)

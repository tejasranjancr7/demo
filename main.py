import numpy as np

def test_numpy():
    print("NumPy Test Started...\n")
    
    # Create arrays
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    
    print("Array a:", a)
    print("Array b:", b)
    
    # Basic operations
    print("\nAddition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    
    # Matrix operations
    mat1 = np.array([[1, 2], [3, 4]])
    mat2 = np.array([[5, 6], [7, 8]])
    
    print("\nMatrix 1:\n", mat1)
    print("Matrix 2:\n", mat2)
    
    print("\nMatrix Multiplication:\n", np.dot(mat1, mat2))
    
    # Statistics
    print("\nMean of a:", np.mean(a))
    print("Sum of a:", np.sum(a))
    print("Max of a:", np.max(a))
    print("Min of a:", np.min(a))
    
    print("\nNumPy Test Completed Successfully!")

if __name__ == "__main__":
    test_numpy()
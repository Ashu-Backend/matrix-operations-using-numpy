import numpy as np

def input_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter matrix row by row (space-separated values):")

    matrix = []
    for i in range(rows):
        while True:
            try:
                print(f"Enter {i+1} row")
                row = list(map(int, input().split()))

                if len(row) == cols:
                    break
                else:
                    print("Wrong Input, enter again.")
            except:
                print("Only numbers allowed.")
                continue
                
        matrix.append(row)
    
    return np.array(matrix)

matrices = []
n = int(input("How Many Matrix you want to make -> "))
for i in range(n):
    print(f"\nEnter Matrix {i+1}")
    mat = input_matrix()
    matrices.append(mat)
    
def print_matrix(mat, name="Matrix"):
    print(f"\n{name}:")
    for row in mat:
        print("  ", " ".join(f"{val:5}" for val in row))

def show_all_matrices():
    for idx, mat in enumerate(matrices):
        print_matrix(mat, f"Matrix {idx+1}")

def show_operations():
    print("\n========== MATRIX TOOL ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("0. Exit")
    print("================================")

def add_matrix(A, B):
    if A.shape == B.shape:
        result = np.add(A, B)
        return result
        
    else:
        print("Matrix shapes do not match for addition.")
        return None

def subtract_matrix(A, B):
    if A.shape == B.shape:
        result = np.subtract(A, B)
        return result
    else:
        print("Matrix shapes do not match for subtraction.")
        return None

def multiply_matrix(A, B):
    if A.shape[1] == B.shape[0]:
        result = np.dot(A, B)
        return result
    else:
        print("Matrix shapes not compatible for multiplication.")
        return None

def transpose_matrix(A):
    return A.T

def determinant_matrix(A):
    if A.shape[0] == A.shape[1]:
        result = np.linalg.det(A)
        return result
    else:
        print("Determinant only possible for square matrix.")
        return None
   
while True:
    show_operations()
    try:
        
        choice = int(input("Enter your choice or press 0 for exit: "))
        
        if choice == 1:
            show_all_matrices()

            i = int(input("First matrix index: "))
            j = int(input("Second matrix index: "))
                
            if i < 1 or i > len(matrices) or j < 1 or j > len(matrices):
                print("Invalid index")
                continue
            
        
            A = matrices[i-1]
            B = matrices[j-1]
            
            result = add_matrix(A, B)
            if result is not None:
                print_matrix(result, "Result")
        
        elif choice == 2:
            show_all_matrices()

            i = int(input("First matrix index: "))
            j = int(input("Second matrix index: "))
                
            if i < 1 or i > len(matrices) or j < 1 or j > len(matrices):
                print("Invalid index")
                continue
                
        
            A = matrices[i-1]
            B = matrices[j-1]
            result = subtract_matrix(A, B)
            
            if result is not None:
                print_matrix(result, "Result")
        
        elif choice == 3:
            show_all_matrices()

            i = int(input("First matrix index: "))
            j = int(input("Second matrix index: "))
                
            if i < 1 or i > len(matrices) or j < 1 or j > len(matrices):
                print("Invalid index")
                continue
                
        
            A = matrices[i-1]
            B = matrices[j-1]
            
            result = multiply_matrix(A, B)
            if result is not None:
                print_matrix(result, "Result")
        
        elif choice == 4:
            show_all_matrices()
                
            i = int(input("Which matrix index: "))
            
            if i < 1 or i > len(matrices):
                print("Invalid index")
                continue

            A = matrices[i-1]

            result = transpose_matrix(A)
            print_matrix(result, "Result")
            
        
        elif choice == 5:
            show_all_matrices()
                
            i = int(input("Which matrix index: "))
            
            if i < 1 or i > len(matrices):
                print("Invalid index")
                continue
            
            A = matrices[i-1]
            
            result = determinant_matrix(A)
            if result is not None:
                print(f"\n✅ Determinant: {round(result, 2)}")
        
        elif choice == 0:
            break
    except:
        print("Invalid input, enter number")
        continue
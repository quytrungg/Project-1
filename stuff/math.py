import copy
import numpy as np

def createMatrix(A : list, n : int):
    if n <= 0:
        print("Không thể tạo ma trận")
        return
    for i in range(0, n): 
        A.append([])
        for j in range(0, n): 
            A[i].append(float(input("Nhập phần tử thứ a[%d][%d]: " % (i, j))))
    return A

def printMatrix(A : list): 
    for i in A:
        print(i)
    print('\n')

def isMatrixZero(A : list, row, col):
    for i in range(row, len(A)):
        if A[i][col] != 0:
            return False
    return True

def idenMatrix(F : list, n : int):
    for i in range(0, n):
        F.append([])
        for j in range(0, n):
            if i == j:
                F[i].append(1.0)
            else: 
                F[i].append(0.0)
    return F

def truncate(n, decimals = 0):
    multiplier = 10 ** decimals 
    truncate = (n*multiplier)/multiplier
    return int(truncate)

def checkZeroRow(A : list, n, row):
    j = 0
    for i in A[row]:
        if j == n:
            break
        if i != 0:
            return False
        j = j + 1
    return True

def swapRow(A : list, i : int, j : int): 
    A[i], A[j] = A[j], A[i] 

def rowPLusRow(A : list, i : int, j : int, alpha : float): 
    for k in range(0, len(A[i])):
        value = A[i][k] + alpha * A[j][k]
        if value == -0.0:
            value = 0.0 
        A[i][k] = truncate(value, 4)

def multiRow(A : list, i : int, alpha : float): 
    for j in range(0, len(A[i])):
        value = alpha * A[i][j]
        if value == -0.0:
            value = 0.0    
        A[i][j] = truncate(value, 4)

def inverseMatrix(A : list, n : int):
    GJ = A.copy()
    I = idenMatrix([], n)

    concat = 0
    for rowG in GJ: 
        for k in range(0, len(I[concat])): 
            rowG.append(I[concat][k])
        concat += 1

    nrow = n 
    ncol = 2 * n 
    row = 0 

    while row < nrow:
        col = row
        while col < ncol and isMatrixZero(GJ, row, col):
            col = col + 1
        if col == ncol: 
            break 
        for pivot in range(row, nrow):
            if GJ[pivot][col] != 0:
                break 
        swapRow(GJ, row, pivot)
        multiRow(GJ, row, 1 / GJ[row][col])
        a = 1 / GJ[row][col]
        for rvs in range(0, row):
            rowPLusRow(GJ, rvs, row, -GJ[rvs][col])
        for k in range(row + 1, n):
            rowPLusRow(GJ, k, row, -GJ[k][col])
            if checkZeroRow(GJ, n, k) == True:
                return ["Không khả nghịch"]
        
        row = row + 1
                
    for p in GJ:
        for i in range(0, n):
            del p[0]

    return GJ

def matrixFormat(A : list):
    print("Ma trận: ", printMatrix(A))
    print('Có nghịch đảo: ', printMatrix(inverseMatrix(A, len(A))))

def main():
    M = [[[1, 2, 1], [3, 7, 3], [2, 3, 4]], 
        [[1, -1, 2], [1, 1, -2], [1, 1, 4]],
        [[1, 2, 3], [2, 5, 3], [1, 0, 8]],
        [[-1, 3, -4], [2, 4, 1], [-4, 2, -9]],
        [[1, 2, 3], [-2, -5, 3], [2, 3, 15]]]

    for i in range (0, 5):
        matrixFormat(M[i])
    
main()
import copy
import numpy as np

A = list() 
# đọc file
read = [line.rstrip() for line in open ('Test.txt')]

for row in read:
    values = row.split(' ')
    A.append([float(value) for value in values])

def is_Stair(maze):
    for i in range(len(maze)):
        for j in range(i):
            if(maze[i][j]!=0):
                return False
        return True     

def is_Zero(x):
    if(x==0):return True
    return False

def get_Identity_Matrix (maze):
    R = list(list())
    for i in range (len(maze)):
        a = list()
        R.append(a)
        for j in range (len(maze[0])):
            if(j == i): R[i].append(1.0)
            else: R[i].append(0.0)
    return R

def set_Identity_Matrix(val):
    identity = val

def swap_Row(maze,i,j):
    for k in range(len(maze[0])):
        temp = maze[i][k]
        maze[i][k] = maze[j][k]
        maze[j][k] = temp
    return maze

def make_Scalar(maze,i,x):
    for k in range(len(maze[0])):
        maze[i][k] = maze[i][k] * x
    return maze

def get_Sum(maze,i,j,x):
    for k in range(len(maze[0])):
        maze[i][k] = maze[i][k] + x * maze[j][k]
    return maze

def transform_Row(maze,temp,pivot,val):
    for j in range (len(maze[0])):
        maze[temp][j] += val * maze[pivot][j]
    return maze

def Gauss_Elimination(maze,identity):
    if(len(identity)!=0): check = True
    else: check = False
    R=copy.deepcopy(maze)
    if(check): 
        I = copy.deepcopy(identity)

    m=len(R)
    n=len(R[0])
    isRow = 0
    isCol = 0

    while(isRow<m):
        while(isCol<n) and (all(is_Zero(R[i][isCol]) for i in range(isRow,m))):
            isCol=isCol+1
        if isCol==n: 
            break
            
        pivot = isRow + [not is_Zero(R[i][isCol]) for i in range(isRow,m)].index(True)

        R = swap_Row(R,isRow,pivot)
        if (check): 
            I = swap_Row(I,isRow,pivot)
        val = 1/R[isRow][isCol]
        R = make_Scalar(R,isRow,val)
        if (check): 
            I = make_Scalar(I,isRow,val)
        for k in range(isRow+1,m):
            if (R[k][isCol] != 0):
                val = -(R[k][isCol])
                R = get_Sum(R,k,isRow,val)
                if (check): I = get_Sum(I,k,isRow, val)
        isRow=isRow+1
    
    return {"Matrix": R, "Identity": I}

def is_Inverse_Matrix(maze):
    for i in range(len(maze)):
        for j in range(len(maze)):
            if(maze[i][j]!=1 and j==i):return False
            elif(maze[i][j]!=0 and j!=i):return False
    return True

def inverse(maze,identity):
    check = False
    if(len(maze[0])!=len(maze)):
        print("Deo phai ma tran vuong")
        return

    if(len(identity)!=0): 
        check = True
        I = copy.deepcopy(identity)

    R=copy.deepcopy(maze)
    
    E = Gauss_Elimination(maze, identity)
    I = E["Identity"]
    R = E["Matrix"]

    # for row in I: print(row)
    # print()
    # for row in R: print(row)
    m=len(R)
    n=len(R[0])
    for i in range(m-1):
        for j in range(i+1,m):
            if(R[i][j]!=0):
                val = -(R[i][j]/R[j][j])
                R = transform_Row(R,i,j,val)
                if(check==True): I=transform_Row(I,i,j,val)

    if(not is_Inverse_Matrix(R)):
        print("Ma trận không khả nghịch")
        I.clear()
        R.clear()
    return {"Matrix": R, "Identity": I}

def Display():
    # print(A)
    identity = get_Identity_Matrix(A)
    # print(I)
    AI = inverse(A,identity)
    #print(AI)
    for row in AI["Matrix"]:
        print(row)
    print()
    for row in AI["Identity"]:
        print(row)

Display()
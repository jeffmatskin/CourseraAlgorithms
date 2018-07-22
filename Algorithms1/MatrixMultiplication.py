import numpy as np

def matrixMultiply(X,Y):
    
    nx = min(np.shape(X))
    ny = min(np.shape(Y))
    print(nx,ny)
    if nx == 0 or ny == 0:
        return 0
    if nx == 1 and ny == 1:
        return X[0][0] * Y[0][0]
    else:
        dimx = nx//2
        dimy = ny//2
        A = X[:dimx,:dimx]
        B = X[:dimx,dimx:]
        C = X[dimx:,:dimx]
        D = X[dimx:,dimx:]

        E = Y[:dimy,:dimy]
        F = Y[:dimy,dimy:]
        G = Y[dimy:,:dimy]
        H = Y[dimy:,dimy:]
        
        P1 = matrixMultiply(A,F-H)
        P2 = matrixMultiply(A+B,H)
        P3 = matrixMultiply(C+D,E)
        P4 = matrixMultiply(D,G-E)
        P5 = matrixMultiply(A+D,E+H)
        P6 = matrixMultiply(B-D,G+H)
        P7 = matrixMultiply(A-C,E+F)    

        return np.array([[P5+P4-P2+P6,P1+P2],[P3+P4,P1+P5-P3-P7]])



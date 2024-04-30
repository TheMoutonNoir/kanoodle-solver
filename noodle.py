from enum import Enum
import numpy as np

class ShapeData:
    def __init__(self,space,weight,name):
        self.space = space
        self.weight = weight
        self.name = name

class Noodle(Enum):
    A = ShapeData(np.array([[1,0],[1,0],[1,1]]), 4, 'A')
    B = ShapeData(np.array([[1,0],[1,1],[1,1]]), 5, 'B')
    C = ShapeData(np.array([[1,0],[1,0],[1,0],[1,1]]), 5, 'C')
    D = ShapeData(np.array([[1,0],[1,1],[1,0],[1,0]]), 5, 'D')
    E = ShapeData(np.array([[0,1],[1,1],[1,0],[1,0]]), 5, 'E')
    F = ShapeData(np.array([[1,0],[1,1]]), 3, 'F')
    G = ShapeData(np.array([[1,0,0],[1,0,0],[1,1,1]]), 5, 'G')
    H = ShapeData(np.array([[1,0,0],[1,1,0],[0,1,1,]]), 5, 'H')
    I = ShapeData(np.array([[1,1],[1,0],[1,1]]), 5, 'I')
    J = ShapeData(np.array([[1],[1],[1],[1]]), 4, 'J')
    K = ShapeData(np.array([[1,1],[1,1]]), 4, 'K')
    L = ShapeData(np.array([[0,1,0],[1,1,1],[0,1,0]]), 5, 'L')
    

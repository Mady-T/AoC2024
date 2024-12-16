import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
CCWMATRIX = np.array([[0, 1], [-1, 0]])
direction = np.array([1,0])
print(direction @ CCWMATRIX)
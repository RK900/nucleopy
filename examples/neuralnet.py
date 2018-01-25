from nucleopy.molecules.dna import DNA
from nucleopy.models.cnn import CNN

X = [[1,2,3,4,5],[3,4,5,6,7]]
y = [[1,0,0,0],[0,1,0,0]]
test_x = [[4,5,6,7,8]]
test_y = [0,1,0,0]
cnn = CNN(X, y, test_x, test_y, 1, 5, 4, 5, 2, 5, activation='sigmoid')

cnn.train()

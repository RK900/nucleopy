from nucleopy.models.cnn import CNN

X = [[1,2,3,4,5],[3,4,5,6,7]]
y = [[1,0,0,0],[0,1,0,0]]
test_x = [[4,5,6,7,8]]
test_y = [0,1,0,0]
cnn = CNN(X, y, test_x, test_y, numfeatures=1, featuresize=5, numclasses=4,convolutions= 5,fullyconnected= 2,epochs= 5, activation='sigmoid')

cnn.train()

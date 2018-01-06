"""
Creates a convolutional neural network model
in TensorFlow
"""
import tensorflow as tf
import math

class CNN:
    def __init__(self,numfeatures, featuresize, labelsize,convolutions, fullyconnected,
                 epochs, activation, learningrate=0.001, optimizer="adam", dropout=0.1, batchsize=100):
        """
        Sets up the parameters for the CNN

        :param featuresize: 2D size of the features
        :param labelsize: Number of labels/classes
        :param convolutions: Number of convolutional layers
        :param fullyconnected: Number of fully connected layers
        :param epochs: Number of epochs
        :param activation: Activation function
        :param learningrate: Learning rate (default is 0.001)
        :param optimizer: Optimizer (default is Adam)
        :param dropout: Dropout rate (default is 0.1)
        :param batchsize: Size of batches to be processed (default is 100)
        """

        self.labels = labelsize
        self.numfeatures = numfeatures
        self.featuresize = featuresize
        self.conv = convolutions
        self.fc = fullyconnected
        self.epochs = epochs
        self.activation = activation
        self.lr = learningrate
        self.optimizer = optimizer
        self.dropout = dropout
        self.batch = batchsize

        self.features = self.numfeatures * self.featuresize
        self.keep_prob = 1 - self.dropout

        self.x_placeholder = tf.placeholder('float', [None, self.features], name='x_placeholder')
        self.y_placeholder = tf.placeholder('float', name='y_placeholder')
        self.keep_prob_placeholder = tf.placeholder('float', name='keep_prob_placeholder')

    def __conv2d(self,x, W):
        return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

    def __maxpool2d(self,x):
        return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")

    def build(self,x):
        weights_keys = []
        weights_values = []

        for i in range(len(self.conv)):
            power = math.pow(2,i)
            weights_keys.append("w_conv%i" % i)
            weights_values.append(tf.get_variable("w_conv%i" % i,
                                    [self.features, self.features, power, power * 2],
                                    initializer=tf.random_normal_initializer()))

        for i in range(len(self.fc)):
            weights_keys.append("w_fc%i" % i)
            weights_values.append(
                tf.get_variable("w_fc%i" % i,
                                    [math.pow(2,self.conv + i), math.pow(2,self.conv + i) * 2],
                                    initializer=tf.random_normal_initializer()))

        biases_keys = []
        biases_values = []

        for i in range(len(self.conv)):
            power = math.pow(2, i+1)
            weights_keys.append("b_conv%i" % i)
            weights_values.append(tf.get_variable("b_conv%i" % i,
                                                  [power],
                                                  initializer=tf.random_normal_initializer()))

        for i in range(len(self.fc)):
            weights_keys.append("b_fc%i" % i)
            weights_values.append(
                tf.get_variable("b_fc%i" % i,
                                    [math.pow(2,self.conv + i) * 2],
                                    initializer=tf.random_normal_initializer()))

        weights = zip(weights_keys, weights_values)
        biases = zip(biases_keys, biases_values)
        weights['out'] = tf.get_variable('w_out', [self.conv + self.fc - 1, self.labels],
                                         initializer=tf.random_normal_initializer())
        biases['out'] = tf.get_variable('b_out', [self.labels],
                                        initializer=tf.random_normal_initializer())

        reshaped = tf.reshape(x, shape=[-1,self.featuresize,1])
        if self.activation == 'relu':
            conv0 = tf.nn.relu(self.__conv2d(x, weights['w_conv0']) + biases['b_conv0'])

        elif self.activation == 'sigmoid':
            conv0 = tf.nn.sigmoid(self.__conv2d(x, weights['w_conv0']) + biases['b_conv0'])
        conv0 = self.__maxpool2d(conv0)

        matrix = [conv0]

        for i in range(1, len(self.conv)):
            if self.activation == 'relu':
                c = tf.nn.relu(self.__conv2d(matrix[i-1], weights['w_conv%i' %i]) + biases['b_conv%i' %i])
                c = self.__maxpool2d(c)
                matrix.append(c)

            elif self.activation == 'sigmoid':
                c = tf.nn.sigmoid(self.__conv2d(matrix[i - 1], weights['w_conv%i' % i]) + biases['b_conv%i' % i])
                c = self.__maxpool2d(c)
                matrix.append(c)

        fc0 = tf.reshape(matrix[-1], [-1, math.pow(2, self.conv)])
        if self.activation == 'relu':
            fc0 = tf.nn.relu(tf.add(tf.matmul(fc0,weights['w_fc0']),biases['b_fc0']))

        elif self.activation == 'sigmoid':
            fc0 = tf.nn.sigmoid(tf.add(tf.matmul(fc0,weights['w_fc0']),biases['b_fc0']))

        matrix.append(fc0)

        for i in range(1, len(self.fc)):
            if self.activation == 'relu':
                f = tf.nn.relu(tf.add(tf.matmul(matrix[i-1],weights['w_fc%i'%i]),biases['b_fc%i'%i]))
                matrix.append(f)

            elif self.activation == 'sigmoid':
                f = tf.nn.sigmoid(tf.add(tf.matmul(matrix[i - 1], weights['w_fc%i' % i]), biases['b_fc%i' % i]))
                matrix.append(f)

        last = tf.nn.dropout(matrix[-1], self.keep_prob)
        output = tf.add(tf.matmul(last, weights['out']), biases['out'], name='final')

        return output


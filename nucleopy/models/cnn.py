"""
Creates a convolutional neural network model
in TensorFlow
"""
import tensorflow as tf
import math

class CNN:
    def __init__(self,labelsize,featuresize,convolutions,fullyconnected,
                 epochs,activation,learningrate,optimizer,dropout,batchsize):
        self.labels = labelsize
        self.features = featuresize
        self.conv = convolutions
        self.fc = fullyconnected
        self.epochs = epochs
        self.activation = activation
        self.lr = learningrate
        self.optimizer = optimizer
        self.dropout = dropout
        self.batch = batchsize

    def __conv2d(self,x, W):
        """
        2D convolutions helper function
        :param x: Inputs
        :param W: Weights
        :return: Tensorflow convolution
        """
        return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

    def __maxpool2d(self,x):
        """
        2D pooling helper function
        :param x: Inputs
        :return: Tensorflow pooling
        """
        return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")

    def build(self):
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

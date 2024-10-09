import numpy as np
import matplotlib.pyplot as plt
import random


def get_column(data, index):
    return [row[index] for row in data]


def prepare_data(file_name_dataset):
    data = np.genfromtxt(file_name_dataset, delimiter=',',
                         skip_header=1).tolist()
    data_new = [get_column(data, k) for k in range(4)]
    X = [[1, x1, x2, x3]
         for x1, x2, x3 in zip(data_new[0], data_new[1], data_new[2])]
    y = data_new[3]
    return X, y


def initialize_params():
    bias = 0
    w = [random.gauss(mu=0.0, sigma=0.01) for _ in range(3)]
    return [bias, w[0], w[1], w[2]]


def predict(x_features, weights):
    y = sum([(x_feature*weight)
            for x_feature, weight in zip(x_features, weights)])
    return y


def compute_loss(y_hat, y):
    return (y_hat - y) ** 2


def compute_gradient_w(x_features, y_hat, y):
    y = [2*x*(y_hat - y) for x in x_features]
    return y


def update_weight(weights, dl_weights, lr):
    new_weights = [(weight - lr*dl_weight)
                   for weight, dl_weight in zip(weights, dl_weights)]
    return new_weights


def implement_linear_regression(x_feature, y_ouput, epoch_max=50, lr=1e-5):
    losses = []
    weights = initialize_params()
    n = len(y_ouput)
    for epoch in range(epoch_max):
        print("epoch:", epoch)
        for i in range(n):
            features_i = x_feature[i]
            y = y_ouput[i]
            y_hat = predict(features_i, weights)
            loss = compute_loss(y_hat, y)
            dl_dweights = compute_gradient_w(features_i, y_hat, y)
            weights = update_weight(weights, dl_dweights, lr)
            losses.append(loss)
    return weights, losses


if __name__ == '__main__':
    X, y = prepare_data('advertising.csv')
    W, L = implement_linear_regression(X, y)
    print('question 12: loss_9999 is', L[9999])

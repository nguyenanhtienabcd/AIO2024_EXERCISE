import numpy as np
import pandas as pd
import math


def create_data_iris(path):
    data_fr = pd.read_csv(path, header=None)
    header = ['Sepal length', 'Sepal width',
              'Petal length', 'Petal width', 'Species']
    data_fr.columns = header
    train_data = data_fr.to_numpy()
    return train_data


def compute_prior_probability(train_data):
    last_col = len(train_data[1, :])-1
    y_unique = np.unique(train_data[:, last_col])  # last column in table
    count = [np.count_nonzero(train_data[:, last_col] == y) for y in y_unique]
    prior_probability = count/np.sum(count)
    return y_unique, prior_probability


def gaussian_function(x, mean, sqrt_var):
    gaus = []
    for i in range(len(mean)):
        p1 = 1/(sqrt_var[i]*np.sqrt(2*np.pi))
        p2 = pow((x[i]-mean[i])/sqrt_var[i], 2)
        p3 = np.exp(-p2/2)
        gaus.append(p1*p3)
    return np.array(gaus)


def compute_conditional_probability(x, train_data):
    last_col = len(train_data[1, :])-1
    y_unique = np.unique(train_data[:, last_col])
    conditional_probability = []
    for i in range(len(y_unique)):
        # lấy index y_unique[i] cột cuối cùng
        index = np.nonzero(
            train_data[:, train_data.shape[1]-1] == y_unique[i])[0]
        table_i = train_data[index, :train_data.shape[1]-1]
        mean_i = np.mean(table_i, axis=0)
        var_i = np.var(table_i, axis=0)
        sqrt_var_i = []
        for data in var_i:
            sqrt_var_i.append(math.sqrt(data))
        sqrt_var_i = np.array(sqrt_var_i)

        # tính sx của từng hàng
        p_i = gaussian_function(x, mean_i, sqrt_var_i)

        # sx có điều kiện của tưng thành phần
        conditional_probability.append(np.prod(p_i))

    return np.array(conditional_probability)


# tạo một hàm train dữ liệu dựa vào các hàm đã tạo trước đấy
def train_gaussian_naive(x, train_data):
    y_unique, prior_probability = compute_prior_probability(train_data)
    conditional_probability = compute_conditional_probability(x, train_data)
    return y_unique, prior_probability, conditional_probability

# tạo một hàm đưa ra dự đoán


def predict_data_iris(y_unique, prior_probability, conditional_probability):
    p = prior_probability*conditional_probability
    predict_list = (p/np.sum(p))
    index_predict = np.nonzero(predict_list == np.max(predict_list))[0]
    predict = y_unique[index_predict]
    return predict


if __name__ == "__main__":
    train_data = create_data_iris('iris.data.csv')
    given_x = [6.3, 3.3, 6.0, 2.5]
    given_y = [5.0, 2.0, 3.5, 1.0]
    given_z = [4.9, 3.1, 1.5, 0.1]

    y_unique_x, prior_probability_x, conditional_probability_x = train_gaussian_naive(
        given_x, train_data)
    predict_x = predict_data_iris(
        y_unique_x, prior_probability_x, conditional_probability_x)

    y_unique_y, prior_probability_y, conditional_probability_y = train_gaussian_naive(
        given_y, train_data)
    predict_y = predict_data_iris(
        y_unique_y, prior_probability_y, conditional_probability_y)

    y_unique_z, prior_probability_z, conditional_probability_z = train_gaussian_naive(
        given_z, train_data)
    predict_z = predict_data_iris(
        y_unique_z, prior_probability_z, conditional_probability_z)

    print(predict_x)
    print(predict_y)
    print(predict_z)

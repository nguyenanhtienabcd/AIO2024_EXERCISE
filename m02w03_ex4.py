import numpy as np

# tạo một hàm sinh dữ liệu


def create_train_data():
    data = [
        ['Sunny', 'Hot', 'High', 'Weak', 'no'],
        ['Sunny', 'Hot', 'High', 'Strong', 'no'],
        ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
        ['Rain', 'Mild', 'High', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
        ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
        ['Overcast', 'Mild', 'High', 'Weak', 'no'],
        ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Mild', 'Normal', 'Weak', 'yes']
    ]
    return np.array(data)

# Hàm tính sắc xuất tiền định


def compute_prior_probability(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))
    count_no = np.count_nonzero(train_data[:, 4] == y_unique[0])
    count_yes = np.count_nonzero(train_data[:, 4] == y_unique[1])
    prior_probability[0] = count_no/(count_no + count_yes)
    prior_probability[1] = count_yes/(count_no + count_yes)
    return prior_probability

# Hàm tính sắc xuất có điều kiện


def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    x_name_list = []
    # list chưa SX tương ứng x_name_list , với điều kiện no
    conditional_probability_no = []
    # list chưa SX tương ứng x_name_list , với điều kiện yes
    conditional_probability_yes = []
    # lấy dữ liệu lần lượt tất cả các cột, trừ cột cuối cùng (cột xem là result)
    for i in range(0, train_data.shape[1]-1):
        x_unique = np.unique(train_data[:, i])
        x_name_list.append(x_unique)

        conditional_probability_no.append([0]*len(x_unique))
        conditional_probability_yes.append([0]*len(x_unique))

        for j in range(0, len(x_unique)):
            # tính toán conditional_probability cho 'no'
            # lấy index no cột cuối cùng
            index_no = np.nonzero(
                train_data[:, train_data.shape[1]-1] == y_unique[0])[0]
            count_j = np.count_nonzero(
                train_data[:, i][index_no] == x_unique[j])
            conditional_probability_no[i][j] = count_j/len(index_no)

            # tính toán conditional_probability cho 'yes'
            # lấy index yes cột cuối cùng
            index_yes = np.nonzero(
                train_data[:, train_data.shape[1]-1] == y_unique[1])[0]
            count_j = np.count_nonzero(
                train_data[:, i][index_yes] == x_unique[j])
            conditional_probability_yes[i][j] = count_j/len(index_yes)

    conditional_probability = [
        conditional_probability_no, conditional_probability_yes]
    return conditional_probability, x_name_list


# tạo một hàm đưa ra đúng vị trí của dữ liệu mong muốn
def get_index_from_value(value, x_name_list):
    for i in range(len(x_name_list)):
        for j in range(len(x_name_list[i])):
            if x_name_list[i][j] == value:
                return i, j


# ##########################
# Train Naive Bayes Model
# ##########################
def train_naive_bayes(train_data):
    prior_probability = compute_prior_probability(train_data)
    conditional_probability, x_name_list = compute_conditional_probability(
        train_data)
    return prior_probability, conditional_probability, x_name_list


# ###################
# Prediction
# ###################
def prediction_play_tennis(given_x, x_name_list, prior_probability, conditional_probability):

    x1 = get_index_from_value(given_x[0], x_name_list)
    x2 = get_index_from_value(given_x[1], x_name_list)
    x3 = get_index_from_value(given_x[2], x_name_list)
    x4 = get_index_from_value(given_x[3], x_name_list)

    # gán biến Prediction ban đầu
    p0 = 0  # sx sẽ thực hiện no
    p1 = 0  # sx sẽ thực hiện yes

    # tính sx có điều kiện với 'no':  'p(no).p(x/no)'
    x1_no = conditional_probability[0][x1[0]][x1[1]]
    x2_no = conditional_probability[0][x2[0]][x2[1]]
    x3_no = conditional_probability[0][x3[0]][x3[1]]
    x4_no = conditional_probability[0][x4[0]][x4[1]]
    p_no = prior_probability[0] * x1_no * x2_no * x3_no * x4_no

    # tính sx có điều kiện với 'yes':  'p(yes).p(x/yes)'
    x1_yes = conditional_probability[1][x1[0]][x1[1]]
    x2_yes = conditional_probability[1][x2[0]][x2[1]]
    x3_yes = conditional_probability[1][x3[0]][x3[1]]
    x4_yes = conditional_probability[1][x4[0]][x4[1]]
    p_yes = prior_probability[1] * x1_yes * x2_yes * x3_yes * x4_yes

    # tính không gian mẫu
    p_total = p_no + p_yes

    # tính sx sẽ thực hiên (prediction)
    p0 = p_no/p_total
    p1 = p_yes/p_total

    y_predict = None

    if p0 > p1:
        y_predict = 'NO'
    if p0 < p1:
        y_predict = 'YES'

    return y_predict


if __name__ == "__main__":
    train_data = create_train_data()
    X = ['Sunny', 'Cool', 'High', 'Strong']
    prior_probability, conditional_probability, x_name_list = train_naive_bayes(
        train_data)
    y_predict = prediction_play_tennis(
        X, x_name_list, prior_probability, conditional_probability)
    print(y_predict)

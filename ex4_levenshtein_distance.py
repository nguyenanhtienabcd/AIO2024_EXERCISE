# tạo một hàm sinh ra ma trận nxm với các phần tử bên trong là số 0
def matrix_0_mn(source, target):
    n_source = len(source)  # n_source: là độ dài của chuỗi source
    m_target = len(target)  # m_target: là độ dài của chỗi target
    # tạo một list có rỗng ban đâu (list này để chứ các phần tử list_in)

    # cách 1: dùng list comprehension
    result = [[0] * (m_target + 1) for _ in range(n_source + 1)]

    # cách 2: dùng vòng lặp for và method extend()
    # list_out = []
    # for i in range(n_source + 1):
    #    list_out.extend([[0]*(m_target + 1)])
    # result = list_out
    return result


# tạo hàm tính khoảng cách levenshtein
def levenshtein_distance(source, target):
    dp = matrix_0_mn(source, target)
    n_source = len(source) + 1
    m_target = len(target) + 1

    # update lại hàng 0 và cột 0 của ma trận dp
    for i in range(n_source):
        dp[i][0] = i
    for j in range(m_target):
        dp[0][j] = j

    # tính toán khoảng cách levenshtein
    for i in range(1, n_source):
        for j in range(1, m_target):
            # so sánh ký tự thứ i-1 của source và ký tự thứ j-1 của target
            if source[i-1] == target[j-1]:
                cost = 0
            else:
                cost = 1
            d_del = dp[i-1][j] + 1  # delete
            d_ins = dp[i][j-1] + 1  # insert
            d_sub = dp[i-1][j-1] + cost  # subtituation
            # tìm giá trị nhỏ nhát của 3 công thứ trên
            dp[i][j] = min(d_del, d_ins, d_sub)
    result = dp[n_source-1][m_target-1]
    return result


if __name__ == '__main__':
    source = input('nhap source:')
    target = input('nhap target:')
    dist = levenshtein_distance(source, target)
    print('levenshtein_distance is:', dist)


# tạo hàm lấy giá trị lớn nhất trong một list
def getmax(list):
    max_list = 0
    size = len(list)
    for i in range(size):
        if list[i] > max_list:
            max_list = list[i]
    return max_list


# tạo hàm trả về mảng giá trị lớn nhất của từng list có K phần tử
def max_array(list, k):
    result = []
    size = len(list)
    if k > size:
        print('k must be less than the number of elements in the list')
        return
    for i in range(size-k+1):
        initial_list = list[i:i+k]
        result.append(getmax(initial_list))
    return result


if __name__ == '__main__':
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    print(max_array(num_list, k))

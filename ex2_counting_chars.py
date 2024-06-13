
# tạo hàm chuyển đổi chuỗi thành một unique list
def char_dictionary(string):
    dict_list = []   # tạo một list rỗng ban đầu
    for char in string:
        if char == " ":  # không tính ký tự space
            continue
        if char not in dict_list:
            # add lần lượt từng phần tử vào trong list "dict"
            dict_list.append(char)
    return dict_list

# tạo hàm đếm số lần xuất hiện của ký tự trong chuỗi


def counting_char(string):
    dict_list = char_dictionary(string)
    output = {}  # tạo một biến kiểu dictionary để lưu dữ liệu
    for char in dict_list:
        # đếm xem ký tự đó xuất hiện bao nhiêu lần trong chuỗi
        count_c = string.count(char)
        output[char] = count_c
    return output


if __name__ == '__main__':
    string = input("input string:")
    print(counting_char(string))

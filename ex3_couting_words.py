### DÙNG CÁC CÂU LỆNH THỰC HIỆN TRÊN COLAB ###

# BLOCK1: download dữ liệu từ goodgle drive
'!gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'


# BLOCK2: đọc dữ liệu từ file
r_file = open('/content/P1_data.txt', 'r')
data = r_file.read()
data = data.lower()
r_file.close()


# BLOCK3: chuyển đổi string thành một list các word
word_list = data.split()
print(word_list)
print(len(word_list))


# BLOCK4: tạo hàm chuyển đổi chuỗi thành một unique word list
def word_dictionary(string):
    dict_list = []   # tạo một list rỗng ban đầu
    for word in string:
        if word not in dict_list:
            # add lần lượt từng phần tử vào trong list "dict"
            dict_list.append(word)
    return dict_list


# BLOCK5: tạo hàm để đếm các từ trong một file
def counting_word(string):
    word_list = word_dictionary(string)
    output = {}  # tạo một biến kiểu dictionary để lưu dữ liệu
    for word in word_list:
        count_w = string.count(word)
    output[word] = count_w
    return output

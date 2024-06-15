### ----- these codes were written in colab ----- ###

# CODE OF QUESTION 1: refer to file "ex1_slicing_list.py"
# CODE OF QUESTION 2: refer to file "ex2_counting_chars.py"
# CODE OF QUESTION 3: refer to file "ex3_couting_words.py"
# CODE OF QUESTION 4: refer to file "ex4_levenshtein_distance.py"
# CODE OF QUESTION 5:
# Block 1: create a check the number function
def check_the_number(n):
    list_of_numbers = []
    result = ""
    for i in range(1, 4+1):
        list_of_numbers.append(i)
    if n in list_of_numbers:
        result = "True"
    else:
        result = "False"
    return result


# Block 2: check function
n = 7
assert check_the_number(n) == "False"
n = 2
results = check_the_number(n)
print(results)


# CODE OF QUESTION 6
# Block 1: create a check the number function
def my_function(data, max, min):
    result = []
    for i in data:
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


# Block 2: check function
my_list = [5, 2, 5, 0, 1]
max = 1
min = 0
assert my_function(max=max, min=min, data=my_list) == [1, 1, 1, 0, 1]
my_list = [10, 2, 5, 0, 1]
max = 2
min = 1
print(my_function(max=max, min=min, data=my_list))


# CODE OF QUESTION 7
# Block 1: create a check the number function
def my_function(x, y):
    x.extend(y)
    return x


# Block 2: check function
list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]
assert my_function(list_num1, my_function(list_num2, list_num3)) == [
    'a', 2, 5, 1, 1, 0, 0]

list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]
print(my_function(list_num1, my_function(list_num2, list_num3)))


# CODE OF QUESTION 8
# Block 1: create a check the number function
def my_function(n):
    min_n = 0
    for i in n:
        if i < min_n:
            min_n = i
    return min_n


# Block 2: check function
my_list = [1, 22, 93, -100]
assert my_function(my_list) == -100
my_list = [1, 2, 3, -1]
print(my_function(my_list))


# CODE OF QUESTION 9
# Block 1: create a check the number function
def my_function(n):
    max_n = 0
    for i in n:
        if i > max_n:
            max_n = i
    return max_n


# Block 2: check function
my_list = [1001, 9, 100, 0]
assert my_function(my_list) == 1001
my_list = [1, 9, 9, 1]
print(my_function(my_list))


# CODE OF QUESTION 10
# Block 1: create a check the number function
def my_function(integers, number=1):
    result = []
    for i in integers:
        if i == number:
            result = True
        else:
            result = False
    return result


# Block 2: check function
my_list = [1, 3, 9, 4]
assert my_function(my_list, -1) == False
my_list = [1, 2, 3, 4]
print(my_function(my_list, 2))


# CODE OF QUESTION 11
# Block 1: create a check the number function
def my_functoin(list_nums=[0, 1, 2]):
    var = 0
    length = len(list_nums)
    for i in list_nums:
        var += i
        result = var/length
    return result


# Block 2: check function
assert my_functoin([4, 6, 8]) == 6
print(my_functoin())


# CODE OF QUESTION 12
# Block 1: create a check the number function
def my_function(data):
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)
    return var


# Block 2: check function
assert my_function([3, 9, 4, 5]) == [3, 9]
print(my_function([1, 2, 3, 4, 5, 6]))


# CODE OF QUESTION 13
# Block 1: create a check the number function
def my_function(y):
    var = 1
    while (y > 1):
        var *= y
        y -= 1
    return var


# Block 2: check function
assert my_function(8) == 40320
print(my_function(4))


# CODE OF QUESTION 14
# Block 1: create a check the number function
def my_function(n):
    var = list(n)
    var.reverse()
    my_string = ''.join(var)
    return my_string


# Block 2: check function
x = 'i can do it'
assert my_function(x) == 'ti od nac i'
x = 'apricot'
print(my_function(x))


# CODE OF QUESTION 15
# Block 1: create a check the number function
def function_helper(x):
    if x > 0:
        x = 't'
    else:
        x = 'n'
    return x


def my_function(list):
    data = [function_helper(x) for x in list]
    return data


# Block 2: check function
data = [10, 0, -10, -1]
assert my_function(data) == ['T', 'N', 'N', 'N']
data = [2, 3, 5, -1]
print(my_function(data))

# CODE OF QUESTION 16
# Block 1: create a check the number function


def function_helper(x, data):
    for i in data:
        if x == i:
            return 0
    return 1


def my_function(data):
    res = []
    for i in data:
        if function_helper(i, data) == 1:
            res.append(i)
    return res


# Block 2: check function
lst = [10, 10, 9, 7, 7]
assert my_function(lst) == [10, 9, 7]
lst = [1, 2, 3, 4, 5]
print(my_function(lst))

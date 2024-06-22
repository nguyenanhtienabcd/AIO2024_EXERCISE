# Stack (ngăn xếp) là một cấu trúc dữ liệu hoạt động theo nguyên tắc LIFO (Last In, First Out)
# nghĩa là phần tử được thêm vào cuối cùng sẽ được lấy ra đầu tiên

# trong bài này sẽ dùng tới list để mô phỏng như một stack (list = stack)

class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def get_stack(self):      # tạo một phương thức lấy giá trị của biến private ra
        return self.__stack

    def is_empty(self):
        if len(self.__stack) == 0:
            return True
        else:
            return False

    def is_full(self):
        # kiểm tra độ dài của list với capacity - kiểm tra chiều dài của stack với capacity
        if len(self.__stack) == self.__capacity:
            return True
        elif len(self.__stack) < self.__capacity:
            return False
        elif len(self.__stack) > self.__capacity:
            print('the size of Stack is being overloaded !!!!!!')
            return False

    def pop(self):
        # lấy chiều dài của list - lấy chiều dài của stack
        len_list = len(self.__stack)
        if len_list > 0:
            value = self.__stack[len_list-1]
            self.__stack.pop()           # xóa phần tử cuối cùng của list
            print(value)
            return value                # trả về giá trị là 1 khi chương trình chạy đúng
        if len_list == 0:
            print('Stack is empty, no value is poped')
            return -1                   # trả về giá trị là -1 khi chương trình chạy báo empty

    def push(self, value):
        len_list = len(self.__stack)
        if len_list < self.__capacity:    # kiểm tra độ dài của list với capacity - kiểm tra chiều dài của stack
            self.__stack.append(value)
            return 1                    # trả về giá trị là 1 khi chương trình chạy đúng
        if len_list >= self.__capacity:
            print('can not push a new value into the Stack, FULL!!!')
            return -1                   # trả về giá trị là -1 khi chương trình báo đã full

    def top(self):
        len_list = len(self.__stack)
        if len_list > 0:
            value = self.__stack[len_list-1]
            print(value)
            return 1

        if len_list == 0:
            print('Stack is empty, no top value to show ')


if __name__ == '__main__':
    stack_a = MyStack(7)
    stack_a.push(25)
    stack_a.push(34)
    stack_a.push(43)
    stack_a.push(97)
    stack_a.push(121)
    stack_a.push(122)
    print(stack_a.get_stack())
    stack_a.pop()
    print(stack_a.get_stack())
    print(stack_a.is_empty())
    print(stack_a.is_full())
    stack_a.pop()
    print(stack_a.get_stack())

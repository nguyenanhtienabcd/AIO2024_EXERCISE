# Queue (hàng đợi) là một cấu trúc dữ liệu hoạt động theo nguyên tắc FIFO (First In, First Out)
# nghĩa là phần tử được thêm vào đầu tiên sẽ được lấy ra đầu tiên

# trong bài này sẽ dùng tới list để mô phỏng như một Queue (list = Queue)

class MyQueue:
    def __init__(self, capacity):
        # tạo thuộc tính private và không thể truy cập từ bên ngoài lớp  self.__abc = abc
        self.__capacity = capacity
        self.__queue = []

    def get_queue(self):    # tạo một phương thức lấy giá trị của biến private ra
        return self.__queue

    def is_empty(self):
        if len(self.__queue) == 0:
            return True
        else:
            return False

    def is_full(self):
        # kiểm tra độ dài của list với capacity - kiểm tra chiều dài của Queue với capacity
        if len(self.__queue) == self.__capacity:
            return True
        elif len(self.__queue) < self.__capacity:
            return False
        elif len(self.__queue) > self.__capacity:
            print('the size of Queue is being overloaded !!!!!')
            return False

    def dequeue(self):
        # lấy chiều dài của list - lấy chiều dài của Queue
        len_list = len(self.__queue)
        if len_list > 0:
            value = self.__queue[0]
            self.__queue.pop(0)           # xóa phần tử đầu tiên của list
            print(value)                 # in ra phần tử đầu tiên của list
            return value
        if len_list == 0:
            print('Queue is empty, no value is dequeued')
            return -1                   # trả về giá trị là -1 khi chương trình chạy báo empty

    def enqueue(self, value):
        len_list = len(self.__queue)
        if len_list < self.__capacity:    # kiểm tra độ dài của list với capacity - kiểm tra chiều dài của Queue
            self.__queue.append(value)
            return 1                    # trả về giá trị là 1 khi chương trình chạy đúng
        if len_list >= self.__capacity:
            print(
                'can not enqueue a new value into the Queue, because the Queue was already full')
            return -1                   # trả về giá trị là -1 khi chương trình báo đã full

    def front(self):
        len_list = len(self.__queue)
        if len_list > 0:
            value = self.__queue[0]
            print(value)
            return 1

        if len_list == 0:
            print('Queue is empty, no top value to show ')


if __name__ == '__main__':
    stack_a = MyQueue(7)
    stack_a.enqueue(25)
    stack_a.enqueue(34)
    stack_a.enqueue(43)
    stack_a.enqueue(97)
    stack_a.enqueue(121)
    stack_a.enqueue(122)
    print(stack_a.get_queue())
    stack_a.dequeue()
    print(stack_a.get_queue())
    print(stack_a.is_empty())
    print(stack_a.is_full())
    stack_a.dequeue()
    print(stack_a.get_queue())

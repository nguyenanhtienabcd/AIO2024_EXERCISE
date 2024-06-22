# tạo một lớp people ban đầu để có thể dùng lại ở các lớp con Student, Teacher, Dortor
# dùng kiểu protected cho các thuộc tính của lớp cha

class People:
    def __init__(self, name, yob):
        # dùng kiểu protected cho các thuộc tính của lớp cha
        self._name = name
        self._yob = yob

    def describe(self):
        # trả về một chuỗi để có thể in ở các lớp con
        return f'name: {self._name}, year of birth: {self._yob}'


class Student(People):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)     # kế thừa các thuộc tính của lớp cha
        # dùng kiểu private cho các thuộc tính của lớp con, do lớp con ko có lớp nào khác kế thừa
        self.__grade = grade

    def describe(self):
        # lớp con in giá trị kết quả ra
        print(f'Student - {super().describe()}, grade: {self.__grade}')


class Teacher(People):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)  # kế thừa các thuộc tính của lớp cha
        # dùng kiểu private cho các thuộc tính của lớp con, do lớp con ko có lớp nào khác kế thừa
        self.__subject = subject

    def describe(self):
        # lớp con in giá trị kết quả ra
        print(f'Teacher - {super().describe()}, subject: {self.__subject}')


class Doctor(People):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)  # kế thừa các thuộc tính của lớp cha
        # dùng kiểu private cho các thuộc tính của lớp con, do lớp con ko có lớp nào khác kế thừa
        self.__specialist = specialist

    def describe(self):
        # lớp con in giá trị kết quả ra
        print(f'Doctor - {super().describe()
                          }, specialist: {self.__specialist}')

# tạo ra một lớp Ward


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__people = []

    def add_people(self, person):
        self.__people.append(person)

    def describe(self):
        print(f'Ward: {self.__name}')
        for person in self.__people:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.__people:
            if isinstance(person, Doctor) == True:
                count = count + 1
        return count

    def age_sort(self):
        self.__people.sort(key=lambda x: x._yob, reverse=True)
        return self.__people

    def teacher_average_age(self, this_year=2024):
        age_teacher = []
        for person in self.__people:
            # kiểm tra từng người xem có thuộc class Teacher không?
            if isinstance(person, Teacher) == True:
                # tính tuổi và lưu vào trong list
                age_teacher.append(this_year - person._yob)
        # làm tròn đến số thứ 2 sau dấu phẩy
        result = round(sum(age_teacher)/len(age_teacher), 2)
        return result


if __name__ == '__main__':
    ward = Ward('downtown')
    ward.add_people(Student('Hoàng', 2003, 9))
    ward.add_people(Teacher("Thắm", 1987, 'math'))
    ward.add_people(Teacher("Quang", 1996, 'math'))
    ward.add_people(Teacher("Đoàn", 1997, 'math'))
    ward.add_people(Student("Quân", 1987, 'heart'))
    ward.add_people(Doctor("Thành", 1988, 'brain'))
    ward.add_people(Doctor("Tùng", 1982, 'teeth'))
    ward.add_people(Doctor("Toàn", 1976, 'heart'))
    ward.add_people(Doctor("Toàn", 1971, 'heart'))
    ward.describe()
    m = ward.count_doctor()
    print('số lượng bác sỹ ở ward là:', m)

    ward.age_sort()
    ward.describe()
    print('tuổi trung bình của giáo viên ở Ward là:', ward.teacher_average_age())

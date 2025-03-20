class SchoolSystem:
    def __init__(self):
        self.__list_students = {class_number: []
                                for class_number in range(1, 12)}

    def add_student_system(self, student_obj):
        print('Студент добавлен в систему ')
        self.__list_students[student_obj.get_class].append(student_obj)

    def student_search(self, name_student: str, last_name_student: str):
        for class_list in self.__list_students.values():
            for student in class_list:
                if student.get_name == name_student and student.get_last_name == last_name_student:
                    return student
        raise ValueError(
            'Проверьте корректность введеных данных. Студент не найдет')

    def remove_student_from_system(self, student_obj):
        class_list = self.__list_students.get(student_obj.get_class)
        class_list.remove(student_obj)
        print('Студент удален из системы')

    @property
    def list_students(self):
        return self.__list_students


class Student:
    def __init__(self, name, last_name, age, class_number, school):
        if age not in range(7, 20) or not isinstance(age, int):
            raise ValueError(
                'Возраст учащегося не должен быть меньше 7 и не больше 19 лет')
        if class_number < 1 or class_number > 11 or not isinstance(class_number, int):
            raise ValueError(
                'Ученик не может попасть в класс младше 1 или старше 11')

        self.__name = self.validate_name_or_last_name(name)
        self.__last_name = self.validate_name_or_last_name(last_name)
        self.__age = age
        self.__class_number = class_number

        assert all([isinstance(data, str)
                   for data in (self.__name, self.__last_name)])
        assert all([isinstance(data, int)
                   for data in (self.__class_number, self.__age)])

    def __str__(self):
        return f'''Имя: {self.__name} 
                Фамилия: {self.__last_name}
                Возраст: {self.__age} 
                В каком классе обучается: {self.__class_number}'''

    def __repr__(self):
        return f'''{self.__name} {self.__last_name}'''

    @property
    def get_class(self):
        return self.__class_number

    @property
    def get_name(self):
        return self.__name

    @property
    def get_last_name(self):
        return self.__last_name

    @staticmethod
    def validate_name_or_last_name(name_or_last_name):
        if not isinstance(name_or_last_name, str):
            raise TypeError('Имя пользователя или фамилия должна быть строкой')
        len_name_or_last_name = len(name_or_last_name)
        if len_name_or_last_name < 2 or len_name_or_last_name > 100:
            raise ValueError(
                'Длина имени пользователя или фамилия не может быть равна 1 символу или больше 100')
        if len(name_or_last_name.split()) > 1:
            raise ValueError(
                'В поле имени или фамилии должны храниться только эти данные')
        return name_or_last_name.capitalize()


school = SchoolSystem()

first_student = Student('Alex', 'Ivanov', 15, 9, school)
second_student = Student('Igor', 'Antonov', 8, 2, school)
third_student = Student('Vlad', 'Petrov', 16, 10, school)

school.add_student_system(first_student)
school.add_student_system(second_student)
school.add_student_system(third_student)

print(school.list_students)

print(school.student_search('Alex', 'Ivanov'))
print(school.student_search('Vlad', 'Petrov'))

school.remove_student_from_system(first_student)
print(school.list_students)

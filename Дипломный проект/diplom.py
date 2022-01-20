import os

import jsonpickle

class FileProvider:

    

    def get(self, path):

        file = open(path, "r")

        data = file.read()

        file.close()

        return data

    

    def create(self , path):

        file = open(path , "x")

    

    def append(self, path, data):

        file = open(path, "a")

        data = file.write(data)

        file.close()

    

    def writelines(self, path, data):

        file = open(path, "w")

        data = file.writelines(data)

        file.close

    

    def write_from_scratch(self,path,data):

        file = open(path, "w")

        data = file.write(data)

        file.close

        

    def clear(self, path):

        file = open(path, "w")

        data = file.write("")

        file.close()    

        

    def exists(self, path):

        return os.path.exists(path)

class StudentsStorage(FileProvider):

    def __init__(self , students = None):

        if students == None:

            self.file_name = []

            json_data = jsonpickle.encode(self.file_name)

            super().create('./students.json')

            super().writelines(json_data)

        else:

            self.file_name = students

        

    def get_all(self):

        if not  super().exists(self.file_name):

            students = []

            self.safe_students(students)

            

        data = super().get(self.file_name)

        students = jsonpickle.decode(data)

        return students

    

    def safe_students(self, students):

        json_data = jsonpickle.encode(students)

        super().writelines(self.file_name, json_data)

            

    def add(self, student):

        students = self.get_all()

        students.append(student)

        self.safe_students(students)

        

    def remove(self, index):

        students = self.get_all()

        students.pop(index)

        self.safe_students(students)

    

class Student:

    def __init__(self, first_name_student, last_name_student, age_student,

                 number_class):

        self.first_name_student = first_name_student

        self.last_name_student = last_name_student

        self.age_student = age_student

        self.number_class = number_class   

class School:

    def __init__(self , name , adress) :

        self.name = name

        self.adress = adress

    

class SchoolHandler:

    def setup_initial_school_data(self):

        self.school = 'school.json'

        self.file_provider.create(self.school)

        school_initial_data = School('None' , 'None')

        json_data = jsonpickle.encode(school_initial_data)

        self.file_provider.writelines(self.school , json_data)

    def __init__(self , school = None , students = None) :

        self.file_provider = FileProvider()

        if school == None:

            self.setup_initial_school_data()

        else:

            self.school = school

        

        try:

            self.school_data = jsonpickle.decode(self.file_provider.get(self.school))

        except FileNotFoundError:

            self.setup_initial_school_data()

            self.school_data = jsonpickle.decode(self.file_provider.get(self.school))

        # self.school = school

        self.student_handler = StudentHandler(students)

        # self.file_provider = FileProvider()

   

    def change_name(self):

        new_name = input('Введите новое название : ')

        # school_data = jsonpickle.decode(self.file_provider.get(self.school))

        self.school_data.name = new_name

        school_data_json = jsonpickle.encode(self.school_data)

        self.file_provider.clear(self.school)

        self.file_provider.write_from_scratch(self.school,school_data_json)

    def change_adress(self):

        new_adress = input('Введите новый адресс : ')

        # school_data = jsonpickle.decode(self.file_provider.get(self.school))

        self.school_data.adress = new_adress

        school_data_json = jsonpickle.encode(self.school_data)

        self.file_provider.clear(self.school)

        self.file_provider.write_from_scratch(self.school,school_data_json)

    def print_name(self):

        # school_data = jsonpickle.decode(self.file_provider.get(self.school))

        if self.school_data.name == 'None':

            print('\nДанных о названии нету \n')

        else:

            print(f'{self.school_data.name}')

    def print_adress(self):

        

        # school_data = jsonpickle.decode(self.file_provider.get(self.school))

        if self.school_data.adress == 'None':

            print('\nДанных об адресе нету\n')

        else:

            print(f'{self.school_data.adress}')

    def school_handler_main(self):

        while True:

            print('Меню Школы')

            print('Показать название школы (1)')

            print('Показать показать адрес школы (2)')

            print('Изменить адрес (3)')

            print('Изменить название (4)')

            print('Отобразить меню учеников (5)')

            print('Закончить (Любой другой символ)')

            user_input = input()

            

            

            if user_input == "1":

                self.print_name() 

            elif user_input == "2":

                self.print_adress()    

            elif user_input == "3":

                self.change_adress()    

            elif user_input == "4":

                self.change_name()    

            elif user_input == "5":

                self.student_handler.student_handler_main()    

            else:

                break

        

class StudentHandler:

    def __init__(self , students):

        # self.file_provider = FileProvider()

        self.studentsStorage = StudentsStorage(students)

    

    def add_new_student(self):

        

        print("Введите Имя, Фамилию, Возраст, Номер класса")

        first_name_student = validate_word(input("введите имя ученика: ") , 2 , 20)

        last_name_student = validate_word(input("введите фамилию ученика: ") , 2 , 20)

        age_student = validate_integer(input("введите возраст ученика: ") , 6 , 20)   

        number_class = validate_integer(input("введите класс ученика: ") , 1 , 12)

        new_student = Student(first_name_student, last_name_student, age_student,

                    number_class)

        self.studentsStorage.add(new_student)

    def print_students(self):

        students = self.studentsStorage.get_all()

        if students.__len__() < 1:

            print('\nСписок учеников пуст\n')

            return

        first_name_student = "Имя"

        last_name_student = "Фамилия"

        age_student = "Возраст"

        number_class = "Номер класса"

        

        

        print(f'{first_name_student:15}{last_name_student:15}{age_student:15}{number_class:15}')

        

        for i in range(len(students)):

            print(f'{i + 1}.{students[i].first_name_student:15}{students[i].last_name_student:15}{students[i].age_student:15}{students[i].number_class:15}')

        

    def remove_student(self):

        students = self.studentsStorage.get_all()

        while True:

            self.print_students()

            print("Выберите номер ученика которого надо удалить.")

            user_answer = int(input())

            

            if user_answer < 1 or user_answer > len(students):

                continue

                

            self.studentsStorage.remove(user_answer - 1)

            

            print(f"{user_answer} успешно удален")

            break

    def student_handler_main(self):

        while True:

        

            print('Меню студентов')

            print('Показать список (1)')

            print('Добавить (2)')

            print('Удалить (3)')

            print('Закончить (Любой другой символ)')

            user_input = input()

            

            

            if user_input == "1":

                self.print_students() 

            elif user_input == "2":

                self.add_new_student()    

            elif user_input == "3":

                self.remove_student()    

            else:

                break

def validate_word(value , min_length , max_length):

    # value_arr = value.split()

    

    # проверка на символы

    # проверка на числа

    if not value.isalpha():

            value = input('\nПоле не может содержать символы и числа , введите еще раз : ')

            validate_word(value , min_length , max_length)

        

    if value.__len__() < min_length or value.__len__() > max_length:

            value = input(f'\nПоле не может быть длинее {max_length} и короче {min_length} символов, введите еще раз : ')

            validate_word(value , min_length , max_length)

    

    if not value.istitle():

        value = input('\nПоле должно начинаться с заглавной буквы и остальные буквы должны быть в нижнем регистре , введите еще раз : ')

        validate_word(value , min_length , max_length)

        

    return value

    

def validate_integer(value , min_d , max_d):

    while tryParse(value) == False:

      

        value = input('\nРазрешается только число : ')

        validate_integer(value , min_d , max_d)

    if int(value) < min_d or int(value) > max_d:

        value = input(f'\nРазрешается ввести не меньше {min_d} и не больше {max_d} : ')

        validate_integer(value , min_d , max_d)

    return value

def tryParse(value):

    try:

        return True , int(value)

    except ValueError:

        return False

jsonpickle.set_encoder_options("json", indent=4,

                               separators=(",", ": "),

                               ensure_ascii=False)

school_handler = SchoolHandler('school.json' , 'students.json')

if __name__ == '__main__':

    school_handler.school_handler_main()
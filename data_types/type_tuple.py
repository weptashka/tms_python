# кортежи (tuples)

# операции с кортежами
# tuple() делает кортеж из итерируемых объектов и может принимать только 1 аргумент
a = tuple("1")
print(a)
print(type(a))

# для того чтобы передать множество аргументов - разделить их запятой и поместить в круглые скобки
b = (1, 2, 3, 4)
print(b)
print(type(b))

# a, b = b, a


# объявление кортежей
# пустой кортеж
tuple_01 = tuple()

# пустой кортеж 2
tuple_02 = tuple()

# не кортеж, а строка, так как без запятой
tuple_11 = ('s')

# а это уже кортеж
tuple_12 = ('s',)

# и это тоже
tuple_13 = 's',

# можно создать кортеж из итерируемого объекта
tuple_2 = tuple("Hello, world!")

#  в большинстве случаев кортеж создаётся с использованием круглых скобок
tuple_31 = ("3", "akjfv", 4, 5, 6)

# можно и без скобок, но лучше таким не увлекаться
tuple_32 = "3", "akjfv", 4, 5, 6

print(type(tuple_01))
print(type(tuple_02))

print(type(tuple_11))
print(type(tuple_12))
print(type(tuple_13))

print(type(tuple_2))
print(tuple_2)

print(type(tuple_31))
print(type(tuple_32))

# pазмер меньше, чем у list
a = (1, 2, 3, 4, 5, 6)
b = [1, 2, 3, 4, 5, 6]

print(a.__sizeof__())
print(b.__sizeof__())

# кортежи как ключи словарей, так как неизменяемый тип
d = {(1, 2, 3): 4444}
print(d)

# d = {[1, 2, 3]: 4444}
# print(d)

# {(1, 2, 3): 4444}
# Traceback (most recent call last):
#   File "C:\PycharmProjects\tms_home_tasks\type_tuple.py", line 16, in <module>
#     d = {[1, 2, 3]: 4444}
#         ^^^^^^^^^^^^^^^^^
# TypeError: unhashable type: 'list'


# разложим кортеж на отдельные переменные:
name, age, company, position = ("Tom", 37, "Google", "software developer")
print(name)  # Tom
print(age)  # 37
print(position)  # software developer
print(company)  # Google

# доступ к элементам кортежа:
# как и везде - как к элементам "массива"

tom = ("Tom", 37, "Google", "software developer")
print(tom)
print(tom[0])  # Tom
print(tom[1])  # 37
print(tom[-1])  # software developer


# кортеж - несколько подряд неизменяемых значений, и этим можно пользоваться:
# когда функция возвращает несколько значений, по сути она возвращает кортеж


def get_person():
    name = "Polly"
    age = 22
    job = "Python developer"
    return name, age, job


print(type(get_person))  # <class 'function'>
person = get_person()
print(type(a))  # <class 'tuple'>


# передача в функцию кортежа, как нескольких значений:

def type_person_info(name, age, job, city):
    print(f"name: {name}, age: {age}, job: {job}, city: {city}")


type_person_info(*person, "Minsk")

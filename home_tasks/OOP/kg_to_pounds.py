# 3. Необходимо создать класс KgToPounds, в который принимает количество
# килограмм, а с помощью метода to_pounds() они переводятся в фунты.
# Необходимо закрыть доступ к переменной kg.
# Также, реализовать методы:
# - set_kg() - для задания нового значения килограммов (записывать только
# числовые значения),
# - get_kg() - для вывода текущего значения кг.
# Во второй версии необходимо использовать декоратор property для создания
# setter и getter взамен set_kg и get_kg.

# ------- Геттеры и Сеттеры ----------
# class KgToPounds:
#     def __init__(self, kg: float):
#         self.__kg = kg
#         self.__pounds = 0
#
#     def to_pounds(self):
#         self.__pounds = self.__kg * 2.20462
#
#     def get_kg(self):
#         return self.__kg
#
#     def set_kg(self, kg: float):
#         self.__kg = kg
#
#     def get_pounds(self):
#         return self.__pounds
#
# measure_1 = KgToPounds(5)
# measure_1.to_pounds()
# print(measure_1.get_pounds())
#
# measure_1.set_kg(10)
# measure_1.to_pounds()
# print(measure_1.get_pounds())
#

# ----- property -------

class KgToPounds:
    def __init__(self, kg: float):
        self.__kg = kg
        self.__pounds = 0

    def to_pounds(self):
        self.__pounds = self.__kg * 2.20462

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, kg: float):
        self.__kg = kg

    @property
    def pounds(self):
        return self.__pounds


measure_1 = KgToPounds(5)
measure_1.to_pounds()
print("kg: ", measure_1.kg)
print("pounds: ", measure_1.pounds)

measure_1.kg = 10
measure_1.to_pounds()
print("kg: ", measure_1.kg)
print("pounds: ", measure_1.pounds)




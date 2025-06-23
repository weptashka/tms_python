# 1) Создайте класс Soda (для определения типа газированной воды), принимающий
# 1 аргумент при инициализации (отвечающий за добавку к выбираемому
# лимонаду). В этом классе реализуйте метод show_my_drink(), выводящий на
# печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе
# отобразится следующая фраза: «Обычная газировка».

class Soda:

    def __init__(self, soda_addition=None):
        self.soda_addition = soda_addition

    def show_my_drink(self):
        if self.soda_addition is not None:
            print("ГАЗИРОВКА и " + self.soda_addition)
        else:
            print("Обычная газировка")


soda_1 = Soda("Лимон")
soda_2 = Soda("Ежевика")
soda_3 = Soda()

soda_1.show_my_drink()
soda_2.show_my_drink()
soda_3.show_my_drink()
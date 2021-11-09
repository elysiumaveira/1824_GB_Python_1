"""
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


from random import randint


class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed = randint(10, 100)
        print(f'Машина идет со скоростью {self.speed} км/ч')

    def stop(self):
        self.speed = 0

    def turn(self):
        if self.speed > 30:
            print(f'Поворот не возможен на скорости {self.speed}! Сбавьте скорость!')
        else:
            print(f'Машина повернула на скорости {self.speed} км/ч.')

    def show_speed(self):
        if self.speed == 0:
            print('Машина никуда не едет.')
        else:
            print(f'Скорость автомобиля {self.speed} км/ч.')


class TownCar(Car):
    def show_speed(self):
        if 0 < self.speed <= 60:
            print(f'Скорость автомобиля {self.speed} км/ч.')
        elif self.speed > 60:
            print(f'Сбавьте скорость. Скорость {self.speed} км/ч')
        else:
            print('Машина стоит')


class WorkCar(Car):
    def show_speed(self):
        if 0 < self.speed <= 30:
            print(f'Скорость {self.speed} км/ч.')
        elif self.speed > 30:
            print(f'Сбавьте скорость. Скорость {self.speed} км/ч ')
        else:
            print('Автомобиль стоит')


class SportCar(Car):
    color: str = 'черная'
    name: str = 'Lamborghini'
    is_police = False


class PoliceCar(Car):
    color: str = 'белая'
    name: str = 'УАЗ'
    is_police:bool = True

    def show_speed(self):
        print('Мы с мигалками! Скорость не важна!')


def check_class(class_name):
    class_name.go()
    class_name.show_speed()
    class_name.turn()
    class_name.stop()
    print('\n')


car = Car('зеленый', 'копейка', False)
check_class(car)

town_car = TownCar('красный', 'Ford', False)
check_class(town_car)

work_car = WorkCar('белый', 'Газель', False)
check_class(work_car)

sport_car = SportCar('красный', 'Ferrari', False)
check_class(sport_car)

police_car = PoliceCar('бело-синяя', 'УАЗ', True)
check_class(police_car)

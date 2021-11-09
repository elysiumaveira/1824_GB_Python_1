"""
Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) —
на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
"""


from time import sleep


class TrafficLight:
    __color = ''
    __colors = ['red', 'yellow', 'green']

    def change_color(self, i):
        self.__color = i
        print(self.__color)

    def running(self):
        for clr in self.__colors:
            if clr == 'red':
                self.change_color(clr)
                sleep(7)
            elif clr == 'yellow':
                self.change_color(clr)
                sleep(2)
            else:
                self.change_color(clr)
                sleep(8)


traffic_light = TrafficLight()

traffic_light.running()

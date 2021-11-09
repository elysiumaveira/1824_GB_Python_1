class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки...')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f'Это {self.title} \n')


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f'Это {self.title} \n')


class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f'Это {self.title} \n')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()

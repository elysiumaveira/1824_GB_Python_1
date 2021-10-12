"""
(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с
числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
"Один"
# >>> num_translate_adv("two")
"два"
"""

def num_translate_adv(number) -> str:

    big_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    examination = False

    for letter in number:
        if letter in big_letters:
            number = number.lower()
            examination = True

    numbers_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    for key, value in numbers_dict.items():
        if key == number:
            if examination:
                return value.capitalize()
            else:
                return value


digit = input('Введите число: ')

print(num_translate_adv(digit))

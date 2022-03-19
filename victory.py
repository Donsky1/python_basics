'''
Задание 7.
(МОДУЛЬ 4) В проекте создать новый модуль victory.py. Задание
Написать или улучшить программу Викторина из предыдущего дз (Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю для тренировки пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
Пример использования sample:
import random
numbers = [1, 2, 3, 4, 5]

# 2 - количество случайных элементов
result = random.sample(numbers, 2)

print(result) # [5, 1]

После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'

Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде: третье января 2009 года, склонением можно пренебречь

В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
'''
import random

d_ls = ('первое', 'второе', 'третье', 'четвёртое', 'пятое',
        'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое',
        'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое',
        'шестьнадцатое', 'семьнадцатое', 'восемьнадцатое', 'девятнадцатое', 'двадцатое',
        'двадцать первое', 'двадцать второе', 'двадцать третье', 'двадцать четвертое',
        'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать девятое',
        'тридцатое', 'тридцать первое')

m_ls = ('января', 'февраля', 'марта', 'апреля',
        'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря')

members_dict = {'Dasha': '22.01.1990',
                'Pasha': '10.03.1987',
                'Masha': '03.01.1988',
                'Sasha': '01.01.1990',
                'Natasha': '15.05.1988',
                'Denis': '11.08.1984',
                'Nikolai': '13.10.1999',
                'Irina': '04.04.2004',
                'Ekaterina': '16.06.2001',
                'Sergey': '21.01.2001'}

while True:
    winners_list = random.sample(list(members_dict), 5)
    true_count = 0
    for people in winners_list:
        data_text = ''
        data_propis = members_dict[people].split('.')
        data_text = d_ls[int(data_propis[0]) - 1] + ' ' + m_ls[int(data_propis[1]) - 1] + ' ' + data_propis[2] + ' года'
        data = input('Угадайте дату рождения первого победителя: ')
        if data != members_dict[people]:
            print(f'Вы ввели неверную дату {data}, а верная следующая {members_dict[people]}: '
                  f'{data_text}')
        else:
            print(f'Вы ввели верную дату {data})')
            true_count += 1

    print('-' * 30)
    print(f'Кол-во верных ответов: {true_count}, {round(true_count / 5 * 100, 2)}%')

    # предложение сыграть снова
    if input('Для продолжения нажмите любую клавишу (для выхода q) ').lower() == 'q':
        break

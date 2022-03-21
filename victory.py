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

members_dict = {'Алекса́ндр Серге́евич Пу́шкин': '26.05.1799',
                'Лев Никола́евич Толсто́й': '09.09.1828',
                'Ива́н Серге́евич Турге́нев': '09.11.1818',
                'Фёдор Ива́нович Тю́тчев': '05.12.1803',
                'Никола́й Васи́льевич Го́голь': '01.04.1809',
                'Фёдор Миха́йлович Достое́вский': '11.11.1821',
                'Анто́н Па́влович Че́хов': '29.01.1860',
                'Александр Николаевич Островский': '12.04.1823',
                'Иван Александрович Гончаров': '18.06.1812',
                'Алекса́ндр Серге́евич Грибое́дов': '15.01.1795'}

count = 1
while True:
    winners_list = random.sample(list(members_dict), 5)
    true_count = 0
    for people in winners_list:
        data_text = ''
        data_propis = members_dict[people].split('.')
        data_text = d_ls[int(data_propis[0]) - 1] + ' ' + m_ls[int(data_propis[1]) - 1] + ' ' + data_propis[2] + ' года'
        data = input(f'Угадайте дату рождения {count} победителя {people}: ')
        if data != members_dict[people]:
            print(f'Вы ввели неверную дату {data}, а верная следующая {members_dict[people]}: '
                  f'{data_text}')
        else:
            print(f'Вы ввели верную дату {data}')
            true_count += 1

    print('-' * 30)
    print(f'Кол-во неверных ответов {5 - true_count}, верных ответов: {true_count}, {round(true_count / 5 * 100, 2)}%')
    count += 1

    # предложение сыграть снова
    if input('Для продолжения нажмите любую клавишу (для выхода q) ').lower() == 'q':
        break

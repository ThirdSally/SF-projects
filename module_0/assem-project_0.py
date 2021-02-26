#!/usr/bin/env python
# coding: utf-8

# ## Задача: компьютер загадывает целое число от 1 до 100, нужно написать программу, которая угадывает его (за как можно меньшее число попыток)
# 
# ### Решение:

# In[ ]:


import numpy as np
def game_core_v3(number):
    '''Сначала устанавливаем число в середине заданного диапазона от 1 до 100, затем меняем его 
    в зависимости от того, в какой части диапазона находится загаданное число.
       Функция принимает загаданное число и возвращает число попыток'''
    start_range = 1 #начальное число заданного диапазона
    end_range = 100 #конечное число заданного диапазона
    predict = (start_range + end_range)//2 #обозначаем середину диапазона для его последующего сокращения
    attempt = 1 #счетчик попыток
    
    while number != predict:
        attempt += 1
        predict = (start_range + end_range)//2
        if number > predict: #проверяем, в какой части диапазона находится загаданное число
            start_range = predict #передвигаем начало диапазона в обозначенную в цикле середину
            predict = start_range + 1
        else:
            end_range = predict #передвигаем конец диапазона в обозначенную в цикле середину
            predict = end_range
            
    return attempt


def score_game(game_core_v3):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core_v3(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
    return(score)


score_game(game_core_v3)


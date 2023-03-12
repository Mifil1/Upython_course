##############################
# Блок підключення бібліотек #
##############################
# -*- coding: utf-8 -*-
import sys
import random


###########################
# Блок реалізації функцій #
###########################
def fizzbuzz(fizz=0, buzz=0, count=0):
    result = ""
    if (count):
        if (fizz < 0):
            fizz * -1
        if (buzz < 0):
            buzz * -1
        for i in range(1, count + 1):
            if (not i % fizz):
                result += "F"
            if (not i % buzz):
                result += "B"
            if i % fizz and i % buzz:
                result += str(i)
            result += " "
    return result

def fill_file_for_fizz_buzz(start_min=1, stop_max=9, count_iteration=1,
                            count_complect=1, name_file="text.txt"):
    critical_max_count_operation = 101
    if count_complect and count_iteration < critical_max_count_operation:
        if stop_max > 9:
            stop_max = 9
        if start_min < 1:
            start_min = 1
        file = open(name_file, 'w')
        for i in range(count_complect):
            file.write(f"{random.randrange(start_min, stop_max)} {random.randrange(start_min, stop_max)}"
                       f" {count_iteration}\n")
        file.close()
        return name_file
    return ""

def print_file(file_name):
    file = open(file_name, 'r')
    for i in file:
        print(i)
    file.close()

def print_fb(file_name):
    file = open(file_name, "r")
    if file:
        for i in file:
            print(fizzbuzz(int(str(i).split()[0]), int(str(i).split()[1]), int(str(i).split()[2])))

def output_file_fb(file_name, file_name2):
    file_input = open(file_name, "r")
    file_output = open(file_name2, "w")
    if file_input:
        for i in file_input:
            file_output.write(fizzbuzz(int(str(i).split()[0]), int(str(i).split()[1]), int(str(i).split()[2])) + "\n")
    file_output.close()
    file_input.close()

#Тут должно біть что-то красивое и универсальное, но я пока передумал. Пусть будет так хоть и сложно для понимания
def output_fizz_buzz(file_name, func = print_fb):
    func(file_name)

#################################
# Основний цикл роботи програми #
#################################
while True:
    print("""Введи номер задания. От 1 до 3.
    Введи 0 чтобы выйти. """)
    your_choice = int(input())
    print(f"Вы ввели: {str(your_choice)}")
    if(your_choice):
        print(f"Завдання №{your_choice}")
    match (your_choice):
        case 1:
            print("Написати fizzbuzz для 20 комплектів по три числа, які записані в файл."
                  "Читайте із файлу перший рядок з трьома числами, беріть із нього числа, "
                  "рахуйте для них fizzbuzz, виводите, продовжуйте з наступним рядком"
                  " і так до кінця файла.")
            #
            min_fb = 1
            max_fb = 10
            count_fb = 50
            count_comp = 20
            name = fill_file_for_fizz_buzz(min_fb, max_fb, count_fb, count_comp)
            print("20 комплектів чисел:")
            print_file(name)
            print("20 комплектів fizzbuzz:")
            output_fizz_buzz(name, print_fb)
        case 2:
            print("Записати перше завдання в файл")
            min_fb = 1
            max_fb = 10
            count_fb = 50
            count_comp = 20
            name = fill_file_for_fizz_buzz(min_fb, max_fb, count_fb, count_comp)
            name1 = name + "1"
            print("20 комплектів чисел:")
            print_file(name)
            print("20 комплектів fizzbuzz:")
            output_fizz_buzz(name, print_fb)
            print("20 комплектів fizzbuzz із файлу:")
            output_file_fb(name, name1)
            print_file(name1)

        case 0:
            break
        case _:
            print("Ваш выбор не входит в диапазон")
    print("\n")
    if (not your_choice):
        break
print("\nПрограмма закончила работу. Пока!\n")
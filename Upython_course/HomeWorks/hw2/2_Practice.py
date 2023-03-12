# -*- coding: utf-8 -*-
import sys

while True:
    print("""Введи номер задания. От 1 до 3.
    Введи 0 чтобы выйти. """)
    your_choice = int(input())
    print("Вы ввели: " + str(your_choice) + "\n")
    match(your_choice):
        case 1:
            print("Завдання №" + str(your_choice))
            print("Перевірити, чи є введене число парним")
            print("Введіть, будь ласка, число")
            choice = int(input())
            if(not choice%2):
                print("Введене число є парним")
            else:
                print("Введене число не є парним\n")
        case 2:
            print("Завдання №" + str(your_choice))
            print("Перевірити, чи є число не парним, ділиться чи на три і на п'ять одночасно, але так, щоб не ділитися на 10")
            print("Введіть, будь ласка, число")
            choice = int(input())
            if (choice % 2 and not choice % 3 and not choice % 5 and choice % 10):
                print("Введене число є не парним, ділиться чи на три і на п'ять одночасно, але так, щоб не ділитися на 10")
            else:
                print("Введене число не є не парним, не ділиться чи на три та на п'ять одночасно, або ділитися на 10\n")
        case 3:
            print("Завдання №" + str(your_choice))
            print("Ввести число, вивести усі його дільники")
            print("Введіть, будь ласка, число")
            choice = int(input())
            print("Дільниками вашого числа є")
            for i in range(1,11):
                if (not choice % i):
                    print(i)
        case 4:
            print("Завдання №" + str(your_choice))
            print("ЗАВДАННЯ ПОКИ ЩО НЕ ПРАЦЮЄ")
            print("Ввести число, вивести його розряди та їх множники.")
            print("Введіть, будь ласка, число")
            choice = int(input())
            if (not choice % 2):
                print("")
        case 0:
            break
        case _:
            print("Ваш выбор не входит в диапазон")
    print("\n")
    if(not your_choice):
        break
print("\nПрограмма закончила работу. Пока!\n")
# -*- coding: utf-8 -*-
import operator
import time

while True:
    print("""Введіть номер завдання. Від 1 до 3.
    Введіть 0 щоб вийти. """)
    your_choice = int(input())
    print("Ви ввели" + str(your_choice) + "\n")
    match(your_choice):
        case 1:
            print("Завдання №" + str(your_choice))
            print("Вивести всі приклади посимвольно:")
            print("\n1.Табличка логічних операторів")
            print("\t0 to 0\t0 to 1\t1 to 0\t1 to 1\t")
            print("and\t\t" + str((0 and 0)) + "\t\t" + str((0 and 1)) + "\t\t" + str((1 and 0)) +  "\t\t" + str((1 and 1)))
            print("or\t\t" + str((0 or 0)) + "\t\t" + str((0 or 1)) + "\t\t" + str((1 or 0)) + "\t\t" + str((1 or 1)))
            print("xor\t\t" + str((0 ^ 0)) + "\t\t" + str((0 ^ 1)) + "\t\t" + str((1 ^ 0)) + "\t\t" + str((1 ^ 1)))
            print("\n2.Умовний оператор if")
            print("""\t\t\tprint("Give it to me!")
            number = int(input())
            if (number >= 100):
            \tprint("Thanks, man!")
            elif ((number > 10) and (number < 100)):
            \tprint("OK :(")
            else:
            \tprint("WHAAAAT????")
            if (number > 1000):
            \tprint("!!!!WOOOOWWWW!!!")""")
            print("Give it to me!")
            number = int(input())
            if (number >= 100):
                print("Thanks, man!")
            elif ((number > 10) and (number < 100)):
                print("OK :(")
            else:
                print("WHAAAAT????")
            if (number > 1000):
                print("!!!!WOOOOWWWW!!!")
            print("\n3.Оператори порівняння")
            print("""
            x = 5
            y = 10
            z = 15
            print((x < y) and (y <= z))
            print(x < y <= z)""")
            x = 5
            y = 10
            z = 15
            print(">>>" +str((x < y) and (y <= z)))
            print(">>>" +str(x < y <= z))
            print("\n4.заміна тернарному оператору")
            print("""\t\t\ttest = True
            result = 'Test is True' if test else 'Test is False'""")
            test = True
            result = 'Test is True' if test else 'Test is False'
            print(">>>result = " + str(result))
            print("""\n\t\t\ttest = True
            print ('ttt' if test else 'fff')""")
            test = True
            print('>>>ttt' if test else 'fff')
            print("\n5.Ще одна альтернатива тернарному оператору")
            print("""\t\t\ttest = True
            result = test and 'Test is True' or 'Test is False'""")
            test = True
            result = test and 'Test is True' or 'Test is False'
            print(">>>result = " + str(result))

        case 2:
            print("Завдання №" + str(your_choice))
            print("Придумати власні приклади на альтернативні варіанти використання if та булевої алгебри")
            print("Завдання Кав'ярня")
            print("Вітаю Вас у нашій кав'ярні. Ми можемо Вам запропонувати каву на вибір:")
            print("""
            1.Амерікано
            2.Амерікано з молоком
            3.Еспресо
            4.Латте
            5.Капучіно
            """)
            asort_list = {1 : "Амерікано", 2 : "Амерікано з молоком", 3 : "Еспресо", 4 : "Латте", 5 : "Капучіно"}
            print("Зробіть Ваш вибір")
            choice_coffe = int(input())
            if(len(asort_list) >= choice_coffe > 0 ):
                print("Ви обрали: " + str(asort_list[choice_coffe]))
            else:
                print("Не вірний вибір. Нажаль ми не знаємо що таке цикли, тож спробуй з початку!")
                break
            print("Яка кількість цукру потрібна?")
            choice_sugar = int(input())
            if(choice_sugar and choice_sugar < 10):
                print("Ви обрали " + str(choice_sugar) + " цукру")
            elif choice_sugar > 10:
                print("Вибачте але у нас нема додаткового стаканчика під цукор. Ми покладемо всього 10 ложок")
                choice_sugar = 10
            else:
                print("Ви побажали каву без цукру")
                choice_sugar = 0
            for i in range(0, 5):
                print(str(i/5*100) + "%")
                time.sleep(1)
            print("Ваша кава готова!")
            if(choice_sugar):
                print("Ви обрали " +str(asort_list[choice_coffe]) + " з цукром, в кількості " + str(choice_sugar) + " ложок")
            else:
                print("Ви обрали " + str(asort_list[choice_coffe]) + " без цукру.")
            print("Дякуємо, що звернулися до нашої кав'ярні. Допобачення, чекаємо на вас ще!")

        case 3:
            print("Завдання №" + str(your_choice))
            print("Задача fizz-buzz")
            print("Введіть число fizz")
            fizz = int(input())
            print("Введіть число bazz")
            bazz = int(input())
            print("Введіть кількість:")
            count = int(input())
            if(count):
                if(fizz < 0):
                    fizz * -1
                if(bazz < 0):
                    bazz * -1
                for i in range(1, count + 1):
                    if(not i%fizz):
                        print("F")
                    if (not i % bazz):
                        print("B")
                    if i%fizz and i % bazz:
                        print(i)
                    print("\n")
            else:
                print("Кількість = 0")
        case 0:
            break
        case _:
            print("Ваш выбор не входит в диапазон")
    print("\n")
    if(not your_choice):
        break
print("\nПрограмма закончила работу. Пока!\n")
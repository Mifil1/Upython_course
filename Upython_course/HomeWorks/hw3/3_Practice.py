# -*- coding: utf-8 -*-
import sys
from builtins import dict


def print_dict(dictionary = {}):
    for key, val in dictionary.items():  # проход по парам
        print(f"{key}: \t{val}")

max_ten_bill = 16880
def filling_dict(balance = 0):

    sum_bill_list = {1: 10, 2: 30, 5: 80, 10: 180, 20: 380, 50: 880, 100: 1880, 500: 6880, 1000: max_ten_bill}
    just_enough = False
    x = 1
    result_bill_list = {}
    start_operation = 0
    for key, val in sum_bill_list.items():
        if (not just_enough):
            if current_balance >= val:
                result_bill_list.update({key: 10})
            if current_balance == val:
                break
            # Эта сложная констукция создана для того чтобы цикл повторился ещё один раз
            # после того как было выполнено основное условие заполнения
            if current_balance < val:
                if x:
                    result_bill_list.update({key: 10})
                    x -= 1
                    start_operation = val - balance
                else:
                    just_enough = True
            continue
    #
    for key, val in reversed(result_bill_list.items()):
        if start_operation / key >= 1:
            result_bill_list[key] = val - int((start_operation / key))
            start_operation = start_operation % key
        else: continue
    return result_bill_list

while True:
    print("""Введи номер задания. От 1 до 3.
    Введи 0 чтобы выйти. """)
    your_choice = int(input())
    print("Вы ввели: " + str(your_choice) + "\n")
    match(your_choice):
        case 1:
            print("Завдання №" + str(your_choice))
            print("Кожен пише суму списку за допомогою for та while")
            my_list = (1, 10, 100, 1000, 10000)
            print("У нас есть список: " + str(my_list))
            my_sum = 0
            for i in my_list:
                my_sum += i;
            print("Сумма нашего списка с помощью ")
            print("for = " + str(my_sum))
            my_sum = i = 0
            while(i < len(my_list)):
                my_sum += my_list[i]
                i += 1
            print("while = " + str(my_sum))

        case 2:
            print("Завдання №" + str(your_choice))
            print("Написати програму, яка виводить сама себе")
            f = open(sys.argv[0], 'r')
            print("""Файл нашої програми має адресу
            """ + str(sys.argv[0]))
            print("\t\t\t\tКод нашої програми \n\n\n")
            for f_line in f:
                print(f_line)
            print("\n\n\t\t\t\tКод нашої програми зверху \n\n\n")
            f.close()

        case 3:
            print("Завдання №" + str(your_choice))
            print("Написати програму, яка виводить саму себе задом наперед")
            f = open(sys.argv[0], 'r')
            print("""Файл нашої програми має адресу
                        """ + str(sys.argv[0]))
            print("\t\t\t\tКод нашої програми \n\n\n")
            for f_line in f:
                print(f_line[::-1])
            print("\n\n\t\t\t\tКод нашої програми зверху \n\n\n")
            f.close()
            # print("\t\t\tКод нашої програми \n\n\n")
            # while (line_counter < 0):
            #
            #     line_counter -= 1
            # f.close()

        case 4:
            print("Завдання №" + str(your_choice))
            print("Банкомат видає суму максимально можливими купюрами")
            current_list = [1000,500,200,100,50,20,10,5,2,1]
            print("Пожалуйста введите сумму:")
            value = int(input())
            if value:
                print("Результат:")
                temp = value
                for i in current_list:
                    if temp >= i:
                        print(f"{i}: {int(temp/i)}")
                        temp = temp%i
        case 5:
            print("Завдання №" + str(your_choice))
            print("Банкомат видає суму дрібними, але не більше 10 штук кожної дрібної купюри")
            current_list = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
            print("Введіть сумму:")
            current_balance = int(input())
            bill_dict = {}
            if current_balance:
                print(f"Сумма = {current_balance}")
                if(current_balance > max_ten_bill):
                    print("Нажаль ми не можемо вам видати цю суму, оскільки стоїть обмеження у кількості\n"
                          "не більше 10-ти купюр одного номіналу")
                    break
                bill_dict = filling_dict(current_balance)
            else:
                print("Вы ввели 0")
                break

            print_dict(bill_dict)
            #Визначення контрольної суми
            sumer = 0
            for key, val in bill_dict.items():
                sumer = sumer + key * val
            print(f"Контрольна сума = {sumer}")
        case 0:
            break
        case _:
            print("Ваш выбор не входит в диапазон")
    print("\n")
    if(not your_choice):
        break
print("\nПрограмма закончила работу. Пока!\n")
#--------------------------------------------------------------------------------------#
##############################
# Блок підключення бібліотек #
##############################
# -*- coding: utf-8 -*-
import sys
import random
##############################
#        Кінець блоку        #
#    підключення бібліотек   #
##############################
#______________________________________________________________________________________#


#--------------------------------------------------------------------------------------#
###########################
# Блок реалізації функцій #
###########################
def create_briliant(num = 1):
    space = int(num/2)
    iterator = 0
    reverse = False
    if num%2:
        for line in range(num):
            ans = ""
            for elem in range(num):
                #Прохід в одну сторону
                if elem == 0 and not reverse:
                    iterator = 1
                elif elem and not reverse:
                    iterator += 2
                # Прохід циклу назад
                if elem == 0 and reverse:
                    break
                elif elem and reverse:
                    iterator -= 2
                ans = " "*space + "*"*iterator
                print(ans)
                if iterator == num:
                    reverse = True
                if space and not reverse:
                    space -= 1
                if space and reverse:
                    space += 1
                if not space and reverse:
                    space = 1

def file_sum(name_file = ""):
    if name_file:
        file = open(name_file, "r")
        for line in file:
            count = 0
            sum = 0
            dif = 0
            part_of_dif = 0
            result = False
            suming = True
            for elem in line:
                if str.isdigit(elem):
                    if suming:
                        count += 1
                        sum += int(elem)
                    if not dif and not suming:
                        dif = int(elem)
                        continue
                    if not part_of_dif and not suming:
                        part_of_dif = int(elem)
                        suming = True
                elif elem == ";":
                    suming = False
                else:
                    continue
            if sum//count == dif and sum%count == part_of_dif:
                result = True
            else:
                result = False
            print(f"{line} {result}")


def courier(apartment_number, floor_in_house, apartments_per_floor):
    total_apartments = floor_in_house * apartments_per_floor
    podezd = (apartment_number - 1) // total_apartments + 1
    floor_in_house = ((apartment_number - 1) % total_apartments) // apartments_per_floor + 1
    return "\nВам нужно зайти в {} подъезд, и подняться на {} этаж.".format(podezd, floor_in_house)

# def create_file_test(file_name = "",number = 1):
#     if file_name:
#         file = open(file_name, "w")
#         for i in range(number):
#             for line in range(random.randrange(2,5)):
#                 ans = ""
#                 for elem in range(random.randrange(1,9)):
#
#     else:
#         print("Введіть назву файлу")
#         return False

###########################
#       Кінець блоку      #
#    реалізації функцій   #
###########################
#______________________________________________________________________________________#


#--------------------------------------------------------------------------------------#
#################################
# Основний цикл роботи програми #
#################################
while True:
    print("Введи номер завдання. От 1 до 3. Введи 0 чтобы выйти. ")
    your_choice = int(input())
    print(f"Вы ввели: {str(your_choice)}")
    if(your_choice):
        print(f"Завдання №{your_choice}")
    match (your_choice):
        case 1:
            print("Завдання бриліант")
            imp = int(input("Введите целое,непарное число: "))
            create_briliant(imp)
        case 2:
            print("Завдання Файл-тест.")
            name_f = "sum.txt"
            file_sum(name_f)
        case 3:
            print("Завдання Кур'єр")
            a = int(input('Введите номер квартиры: '))
            b = int(input('Введите этажность дома: '))
            c = int(input('Введите колличество кв. на этаж: '))
            print(courier(a, b, c))

        case 0:
            break
        case _:
            print("Ваш выбор не входит в диапазон")
    print("\n")
    if (not your_choice):
        break
print("\nПрограма закінчила роботу. До зустрічі!\n")

#################################
#         Кінець роботи         #
#    основного циклу програми   #
#################################
#______________________________________________________________________________________#
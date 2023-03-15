#--------------------------------------------------------------------------------------#
##############################
# Блок підключення бібліотек #
##############################
# -*- coding: utf-8 -*-
import sys

##############################
#        Кінець блоку        #
#    підключення бібліотек   #
##############################
#______________________________________________________________________________________#


#--------------------------------------------------------------------------------------#
###########################
# Блок реалізації функцій #
###########################
#1
def upka(string):
    if isinstance(string, str):
        return str.upper(string)
    return ""
def lowka(string):
    if isinstance(string, str):
        return str.lower(string)
    return ""
#2
def sqrt(x):
    return x**2
def issmpl(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True
#3
def delete_service_symbol_in_str(string):
    if len(string) > 1000000000:
        return ""
    if isinstance(string, str):
        if string:
            temp_string = ""
            for i in string:
                if str.isalnum(i) or str.isspace(i):
                    temp_string += i
            return temp_string
        else:
            return ""
    else:
        return ""

def filter_string_after_count(stringa):
    return str.lower(delete_service_symbol_in_str(stringa)).split()

def counter_word(string_in_func):
    word_list = filter_string_after_count(string_in_func)
    words_dict = {}
    i_count = 1
    for i in word_list:
        if not words_dict.get(i):
            words_dict.update({i:1})
        for j_count, j in enumerate(word_list[i_count::]):
            if i == j:
                words_dict[i] += 1
                word_list.remove(j)
                #print(f"i_count: {i_count}, i: {i}, j: {j}, j_count: {j_count}")
        i_count += 1
    return words_dict

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
            print("Написати 2 функції. Перша функція прийматиме рядок та приводитиме\n"
                  "його до нижнього регістру. Друга функція прийматиме рядок та\n"
                  "приводитиме його до верхнього регістру. \n"
                  "Головна програма має застосовувати обидві функції до списку\n"
                  "рядків за допомогою map, для кожного з рядків, та друкувати результат.\n")
            link = "C:\\Users\\Mifil\\PycharmProjects\\pythonProject1\\its_text"
            f = open(link, 'r')
            print("В нас є радок:")
            listik = f.read(100).split()
            print(listik)
            print("Використовуємо map() зі збільшенням до нього:")
            listik = list(map(upka,listik))
            print(listik)
            print("Використовуємо map() зі зменшенням до нього:")
            listik = list(map(lowka, listik))
            print(listik)
            f.close()
        case 2:
            print("Написати функцію, яка буде підносити число у квадрат. Написати другу,\n"
                  "яка буде перевіряти, чи є число простим. Потрібно видрукувати в головній\n"
                  " програмі квадрати усіх простих чисел зі списку від 0 до 50 за допомогою map\n")
            print("Список простих чисел")
            smpl_list = [x for x in range(1, 51) if issmpl(x)]
            print(smpl_list)
            print("Всі квадрати простих чисел:")
            smpl_list = list(map(sqrt, smpl_list))
            print(smpl_list)

        case 3:
            print("Візьміть файл, в якому є багато англійських слів у рядках.\n"
                  "Порахуйте частоту зустрічі кожного слова та видрукуйте відсортовано.\n")
            link = "C:\\Users\\Mifil\\PycharmProjects\\pythonProject1\\its_text"
            f = open(link, 'r')
            text_list = f.read()
            print("Наш текст:")
            print(text_list)
            print("\nКількість слів у тексті:")
            print(counter_word(text_list))
            f.close()
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
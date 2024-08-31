# ### 1 Question
# Кадом методҳои модули datetime ва randome - ро медонед. Бо мисолҳо фаҳмонед.


# today() 
# fromtimestamp()
# today() 
# fromisoformat() 
# now()
# utcnow() 
# fromtimestamp() 
# strptime() 
# isoformat() 
# timedelta()  

# Random

# random()
# choice()
# choices()
# randint()
# randrange()
# sample()
 
#____________________________________________________________________________________________

# ### 2 Question
# Кадом методхо ва функсияхоро барои кор бо файл медонед.

# read
# readline 
# readlines
# write 
# writeline
# writelines
# (r)
# (a)
# (w)
# (b)
# open
# close

#_______________________________________________________________________________________________

# ### 3 Question
# Github чист? Командахои GitHub-ро фахмонед.

# GitHub — web servisi buzurgest ki baroi joygirkunii IT- proektho va razrabotkai on az tarafi yak kas you yak team kumak merasonad . 

# git init
# git add .
# git commit -m ""
# git branch "name of the branch"
# (link of the repository)
# git push origin "name of the resporatory"






# _______________________________________________________________________________________________


# # ### 1 Question
# Write a Python program to insert an element at a specified position into a given list.
# Напишите программу Python для вставки элемента в указанную позицию в заданный список.
# Барономае нависед дар Python, барои дохил кардани 
# [1, 1, 2, 3, 4, 4, 5, 1]
# # input
#     Enter an element: Sorbon
#     Index: 3
# # output
#     [1, 1, 2, "Sorbon", 3, 4, 4, 5, 1]


# def insert_element(lst, element, index):
#     lst.insert(index, element)
#     return lst

# my_list = [1, 1, 2, 3, 4, 4, 5, 1]

# element = input("Enter your element ----> ")
# index = int(input("Show the INdex ---> "))

# updated_list = insert_element(my_list, element, index)

# print(updated_list)


#______________________________________________________________________________________________


# ### 2 Question
# Write program to print 2 days before, today, 2 days after / Напишите программу для печати позавчера, сегодня, послезавтра. / Барномаи нависед, то пареррӯз, имрӯз, фардои дигарро чоп кунад 


# from datetime import datetime, timedelta

# today = datetime.now()
# two_days_before = today - timedelta(days=2)
# two_days_after = today + timedelta(days=2)

# print("Two days before today ---> ", two_days_before.strftime("%Y-%m-%d"))
# print("Today --->", today.strftime("%Y-%m-%d"))
# print("Two days after today ---> ", two_days_after.strftime("%Y-%m-%d"))

# ____________________________________________________________________________________________________


# ### 3 Question
# Write a program to subtract five days from the current date / Напишите программу, которая вычитает пять дней из текущей даты.

# Input: 17.02.2024           Output: 12.02.2024

# from datetime import datetime, timedelta

# current_date = datetime.strptime("17.02.2024", "%d.%m.%Y")
# new_date = current_date - timedelta(days=5)
# output = new_date.strftime("%d.%m.%Y")
# print(output)


#___________________________________________________________________________________________________________


# ### 4 Question
# Create a function that takes a string and returns the sum of vowels, where some vowels are considered numbers (Exactly use dictionary.). Создайте функцию, которая принимает строку и возвращает сумму гласных, где некоторые гласные считаются числами (Обязательно используйте словари).(A=4, E=3, I=1, O=0, U=0) 

# Input                                           Output
# sum_of_vowels("Do I get the correct output?")   10

# def vowels(s):
#     vowel_values = {
#         'A': 4, 
#         'E': 3, 
#         'I': 1, 
#         'O': 0, 
#         'U': 0}
#     total = 0
#     for char in s.upper():
#         if char in vowel_values:
#             total += vowel_values[char]
#     return total

# result = vowels("Do I get the correct output?")
# print(result)

# ___________________________________________________________________________________________________________

# ### 5 Task
# Create a python program to read line number N from the following file.
# Создайте программу Python для чтения строки номер N из следующего файла.
# my_file.txt -> Hello world
#                TEST
#                Tajikistan
#                An apple
# # input
#     3
# # otput
#     Tajikistan



# def read_line_n(filename, n):
#     with open(filename, 'r') as file:
#         lines = file.readlines()
#         if 1 <= n <= len(lines):
#             return lines[n-1].strip()
#         else:
#             return "Line number out of range"

# filename = 'my_file.txt'
# n = 3
# print(read_line_n(filename, n))




# ______________________________________________________________________________________________-

# ### 6 Question
# Write a program that replaces the content of all odd lines in a given file with a word that we input.
# Напишите программу, которая в заданном файле заменяет содержимое всех нечётных строк на слово, которое мы вводим.
# Барномае нависед, ки дар файли додашуда маълумоти хама сатрхои токро ба калимае, ки мо дохил мекунем, иваз кунад. 





#________________________________________________________________________________________________


# ### 7 Question
# Create a python program to generate a random password of the specified length.
# Создайте программу Python для создания случайного пароля указанной длины.
# # input
#     Enter the desired password length: 12
# # output
#     Generated password: Xy#7pLm$9oR5

# import random

# characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*[]()1234567890"

# length = 12

# password = ""
# for i in range(length):
#     password += random.choice(characters)

# print("Random password ---> ", password)


#_______________________________________________________________________________________________


# ### 8 Question
# Write a Python script to print a dictionary where the keys are numbers between 1 and N (both included) and the values are the square of the keys.
# Напишите сценарий Python для печати словаря, в котором ключами являются числа от 1 до N (оба включены), а значениями являются квадраты ключей.
# # input
#     15
# # output
#     {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


# N = 15
# result = {i: i**2 for i in range(1, N + 1)}
# print(result)


#____________________________________________________________________________________________________________________

# ### 9 Question
# Create a function that returns the number of times a character appears in each word in a sentence. Treat upper and lower case characters of the same letter as being identical. Создайте функцию, которая возвращает количество раз, когда символ встречается в каждом слове предложения. Считать символы верхнего и нижнего регистра одной и той же буквы идентичными.

# Input       
# char_appears("She sells sea shells by the seashore.", "s")

# Output
# [1, 2, 1, 2, 0, 0, 2]

# def char_appears(sentence, char):
#     words = sentence.split()
#     char = char.lower()
#     return [word.lower().count(char) for word in words]

# result = char_appears("She sells sea shells by the seashore.", "s")
# print(result)



# _______________________________________________________________________________________________________________

# ### 10 Task
# Given a list of elements of any data types. Create a Python program to separate elements by their types and save them into a new dictionary.
# The keys of a dictionary must be of a data type, and its element must be data belonging to that type.
# Дан список элементов любых типов данных. Создайте программу Python для разделения элементов по их типам и сохранения их в новый словарь.
# Ключи словаря должны иметь тип данных, а его элементом должны быть данные, принадлежащие этому типу.
# # input
#     1 hello True 12 Muhammad
# # output
#     {"int": [1,12], "str": ["hello", "Muhammad"], "bool": [True]}


# def bora(elements):
#     separated_dict = {}
    
#     for element in elements:
#         try:
#             element_type = type(element).__name__
#             if element_type not in separated_dict:
#                 separated_dict[element_type] = []
#             separated_dict[element_type].append(element)
#         except Exception as e:
#             print(f"Error processing element {element}: {e}")
    
#     return separated_dict

# input_elements = [1, "hello", True, 12, "Muhammad"]
# output = bora(input_elements)
# print(output)

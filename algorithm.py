# Ex1
# text = input("enter your text:")
# for char in text :
#     print(char)

# Ex2
# text = input("enter your text:")
# for i in range(len(text)):
#     print(i)
               
# Ex3
# text = input("enter text: ")
# result = "no"
# for cha in text:
#     if cha.isupper():
#         result = "yes"
# print(result)


# Ex4

# text = "3 4 5 6"
# sum = 0
# for char in text:
#     if char!=" ":
#         print(char)
#         sum += int(char)
# print(sum)


# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
# Q2 - Sum all number 
# Q3 - Sum only even number 
# Q4 - Reverse 
# text = "454639"
# count_odd = 0
# count_even = 0
# sum_num = 0
# sum_even = 0
# for char in text:
#     num = int(char)
#     if num % 2 == 0:
#         count_even += 1
#         sum_even += num
#     else:
#         count_even += 1
#     sum_num += num
# print(count_odd)
# print(count_even)
# print(sum_num)
# print(sum_even)
# print(text[::-1])

# Ex6
# num = int(input("enter your num:"))
# if num % 2 == 0 :
#     print("odd num")
# else:
#     print("even num")

# Ex7
# for i in range(10,20):
#     num = int(input("Enter num here:"))
#     if num >= 10 and num <= 20:
#         print("Continue")
#     else:
#         print("Out of range")

# Ex8 - String
# We have text = "9394884039"
# Q1 - How many number 8 in string
# Q2 - What is first index of letter 8

# text = "9394884039"
# count_8 = text.count("8")
# first_index_8 = text.find('8')
# print("count_8:",count_8)
# print("first_index_8:",first_index_8)

# Ex9 - String
# We have string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"
# Q2 - Multiple each letter by 2 result = "6 8 10 12"

# text = "3 4 5 6"
# result_no_spaces = text.replace(" ", "")
# print( result_no_spaces)
# numbers = text.split()
# doubled_numbers = [str(int(num) * 2) for num in numbers]
# result_doubled = " ".join(doubled_numbers)
# print( result_doubled)


#Ex10 - Number
#Enter 5 numbers and find maximum and minimum value
#Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0
# number = int(input("Enter number:"))
# number_max = number
# number_min = number
# for i in range(4):
#     number = int(input("Enter number:"))
#     if number > number_max:
#         number_max = number
#     if number < number_min:
#         number_min = number
# print("Max =", number_max, "Min =", number_min)








    











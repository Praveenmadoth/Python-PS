

# task 2-------------

# Q1: Take an input string "manoj". Replace the last character with the length of the string.
# # - Input: manoj
# # - Output: mano
# name=input("enter the name:")
# l=len (name)
# print(name[:l-1] + str (l))

# Q2: Given a string "manoj", find the first half length and second half length.
# - Input: manoj
# - Output:
# - First half length = 2
# - Second half length = 3
# name=input("enter the name:")
# first_half=len(name)//2
# second_half=len(name)-first_half
# print("1st half length is :",first_half)
# print("2st half length is :",second_half)

# Q3: From the string "manoj", print the first half characters and the second half characters.
# - Input: manoj
# - Output:
# - First half = ma
# - Second half = noj

# name=input("enter the name:")#1.praveen & 2.raju  manoj
# first_half=len(name)//2 #7//2=3...4//2=2
# second_half=len(name)-first_half #7-3=4...4-2=2
# print(name[ :(first_half)]) # pra..ra
# print( name[len(name)//2:]) # een...ju

# # 4.From the string "manoj", print the first half length and the second half characters.
# - Input: manoj
# - Output:
# - First half length = 2
# - Second half characters = noj
# name=input("enter the name:")
# print("First half length",len(name)//2)
# print(name[len(name)//2:])

# Q5: If the input is "manoj" and age is 20, print the sentence:
# - Input: "manoj", 20
# - Output: manoj is 20 years old

# name=input("enter the name:")
# age=str(input("enter age:"))
# print(name+" is "+age + " years old")

# Q6: Take the input "manoj". Print the first and last character together with the age.
# - Input: "manoj", 20
# - Output: mj20
# name=input("enter the name:")
# age=str(input("enter age:"))
# print(name[0]+name[-1]+str(age))

# Q7: From the input "manoj", print the name with the first half replaced by stars.
# - Input: manoj
# - Output: **noj
# name=input("enter the name:")
# l=len(name)
# first_half=len(name)//2
# print(first_half*"*"+name[len(name)//2:])

# 8. From the input "manoj", print the name with the second half replaced by stars.
# - Input: manoj
# - Output: ma***
# name=input("enter the name:")
# l=len(name)
# first_half=len(name)//2
# second_half=len(name)-first_half
# print(name[:first_half]+"*"*second_half)

# Q9: If the input is "manoj" and age is 20, print the sentence where the age is added to the string length.
# - Input: "manoj", 20
# - Output: manoj is 25 years old

# name=input("enter the name:")
# age=int(input("enter the age:"))
# length=len(name)
# age=age+length
# print(name + " is " + str(age) +" years old " )

# Q10: Reverse the string "manoj" and append the age at the end.
# - Input: "manoj", 20
# - Output: jonam20
# name=input("enter the name:")
# age=int(input("enter the age :"))
# rev=name[::-1]
# print(rev+ str(age))


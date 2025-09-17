# ....Task1
# 1.	Write a Python program to store "manoj" in one variable and "parlapalli" in another,
#  then print them together as "manoj parlapalli".
# name="manoj "
# s="parlapalli"
# print(name+" "+s)

# 2.	How would you slice characters from a string "manoj"
#  without using loops? Give 3 different slice examples.
# n="manoj"
# print(n[0:2])#ma
# print (n[1:3] )#an
# print( n[3:])#oj
 
# 3. to reverse the string "manoj
# n="manoj"
# rev=n[::-1]
# print(rev)

# 4.first and last character of the string "manoj". Expected output: mj
# n='manoj'
# print(n[0]+n[len(n)-1])

# 5.first two and last two characters of "manoj".
# n=str(input("enter the string name:"))
# print(n[0:2]+ n[-2:])

# 6."manoj" → "m***j".
# n=input("enter the string :")
# print(n[0] + "*" * (len(n)-2) + n[-1])

# 7.first two and last two characters and cover the remaining characters with *.
# Example: "manoj" → "ma*oj"

# n="praveen"
# print(n[0:2] + "*" * (len(n)-4) + n[-2:])

#8. first half of the string "parlapalli".
# n="parlapalli"
# h=(len(n)//2)
# print(n[:h])

# 9.last half of the string "parlapalli
# n="parlapalli"
# h=(len(n)//2)
# print(n[h:])

# 10.Example: name = "manoj", number = 3 → Output: "manoj manoj manoj".
# n="manoj "
# m=int(input("how many times to multiply :"))
# print(n*m)

# add of some of the  numbers
# n=int(input("enter the no of numbers :"))
# i=0
# sum=0
# while i in range(n):
#     m=int(input("enter values: "))
#     sum+=m
#     i+=1
# print(sum)   

# type conversion

# v=0.10
# v=bool(v)
# print(v)
# print(type(v))

# v=str (10)
# v=int(v)
# print(v)

# v=str (10.0)
# v= int(v)
# print(v)# error

#  input=praveen output=pr5
# name=input("enter the name:")
# n=name[:2]
# print(n+str((len(name)-2)))

#input name =praveen age=14 output= praveen age is 14
# name=input("enter the name:")
# age=str(input("enter age:"))
# print(name+" age is "+age)

# task 2-------------

# Q1: Take an input string "manoj". Replace the last character with the length of the string.
# # - Input: manoj
# # - Output: mano4
# name=input("enter the name:")
# l=len (name)
# # print(l)
# print(name[:(len(name)-1)] + str (l))

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
# l=len(name)
# first_half=len(name)//2
# second_half=len(name)-first_half
# print("first half length",first_half)
# print(name[second_half:])

# Q5: If the input is "manoj" and age is 20, print the sentence:
# - Input: "manoj", 20
# - Output: manoj is 20 years old

# name=input("enter the name:")
# age=str(input("enter age:"))
# print(name+" age is "+age)

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
# second_half=len(name)-first_half
# print(first_half*"*"+name[second_half:])

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

# From the string "manoj", print the first half characters and the second half characters.
# - Input: manoj
# - Output:
# - First half = ma
# - Second half = noj
# name=input("enter the name:")
# l=len(name)
# first_half=len(name)//2 
# second_half=len(name)-first_half 
# if l%2!=0:
#     print(name[ :(first_half)]) 
#     print( name[second_half-1:]) 
# else:
#     print(name[ :(first_half)]) 
#     print( name[second_half:]) 


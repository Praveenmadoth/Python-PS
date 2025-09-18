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
# n="manoj"
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
# 1.Question: Determine whether a number is even or odd. Explanation: A number is even
# if it is divisible by 2. Otherwise, it’s odd. - Input: Number = 6 - Output: Even number
# n=int(input("enter the number:"))
# if n%2==0:
#     print("even number")
# else:
#     print("odd number")

# 2.Check if a number is divisible by 5 but not by 10.Explanation: Use modulo (%) to check 
 #  if the number % 5 == 0 and number % 10 != 0. - Input: Number = 25 - Output: Satisfy
# n=int(input("enter the number:"))
# if n%5==0 and n%10!=0:
#     print("satisfy")
# else:
#     print("not satisfy")
# 
# 3.biggest number among two. Explanation: Use comparison operators (>)
#  to check which number is greater. - Input: A = 4, B = 7 - Output: Biggest is: 7
# a=int(input("enter a number:"))
# b=int(input("enter b number:"))
# if a>b:
#     print("Biggest is :",a)
# else:
#     print("Biggest is :",b)

#4. the smallest number among two. Explanation: Use comparison operators (<)
#  to find the smaller value. - Input: A = 4, B = 7 - Output: Smallest is: 4
# a=int(input("enter a number:"))
# b=int(input("enter b number:"))
# if a<b:
#     print("Smallest is :",a)
# else:
#     print("Smallest is :",b)

# 5.Check if a number is divisible by 2, 3, and 6. Explanation: If a number is 
# divisible by both 2 and 3, it is also divisible by 6. - Input: Number = 18 - Output: Satisfy
# a=int(input("enter a number:"))
# if a%2==0 and a%3==0:
#     print("Satisfy")
# else:
#     print("not satisfy")

# 6.person is eligible to vote (age >= 18). Explanation: A person is eligible
#  to vote if their age is 18 or above. - Input: Age = 19 - Output: Eligible to vote
# age=int(input("enter the age:"))
# if age>=18:
#     print("Eligible to vote")
# else:
#     print("Not eligible")

# 7.Student passes only if marks in all subjects are 35 or more.
#  - Input: Maths = 40, Physics = 36, Chemistry = 30 - Output: Fail
# m=int(input("enter maths marks:"))
# p=int(input("enter physics marks:"))
# c=int(input("enter chemistry marks:"))
# if m>=35 and p>=35 and c>=35:
#     print("Pass")
# else:
#     print("Fail")

# 8.check if any one subject has marks >= 35
#  - Input: Maths = 20, Physics = 38, Chemistry = 25 - Output: Pass
# m=int(input("enter maths marks:"))
# p=int(input("enter physics marks:"))
# c=int(input("enter chemistry marks:"))
# if m>=35 or p>=35 or c>=35:
#     print("Pass")

# 9.to verify two subjects
#  >= 35. - Input: Maths = 40, Physics = 20, Chemistry = 36 - Output: Pass
# m=int(input("enter maths marks:"))
# p=int(input("enter physics marks:"))
# c=int(input("enter chemistry marks:"))
# if (m>=35 and p>=35) or (p>=35 and c>=35) or (c>=35 and m>=35):
#     print("Pass")  
# else:
#       print("Fail")     

#10.biggest number among three. Explanation: Compare each pair of numbers
#  using if-else conditions. - Input: A = 7, B = 4, C = 9 - Output: Biggest is: 9 
# a=int(input("enter A value:"))
# b=int(input("enter B value:"))
# c=int(input("enter C value:"))
# if a>b and a>c:
#     print("Biggest is",a)
# elif b>a and b>c:
#     print("Biggest is",b)
# elif c>a and c>b:
#     print("Biggest is",c)

# 11.smallest number among three. Explanation: Use comparison logic to
#  determine the minimum value. - Input: A = 7, B = 4, C = 9 - Output: Smallest is: 4
# a=int(input("enter A value:"))
# b=int(input("enter B value:"))
# c=int(input("enter C value:"))
# if a<b and a<c:
#     print("Smallest is",a)
# elif b<a and b<c:
#     print("Smallest is",b)
# elif c<a and c<b:
#     print("Smallest is",c)

# 12.A number is a perfect square if the square of its square root equals
#  the number. - Input: Number = 49 - Output: Perfect square
# n=int(input("enter the value:"))
# a=int(n**0.5)
# print(a)
# res=a*a
# if n==res:
#     print("perfect sq")
# else:
#     print("not perfect sq")

# 13.Divide total people by 5 and round up using ceiling logic.
#  - Input: Members = 17 - Output: Cars needed = 4
# n=int(input("enter peoples number:"))
# cars=n//5
# if n%5==0:
#     print("cars needed",cars)
# else:
#     print("cars needed",cars+1)


#  14.to find the second largest value.
#  - Input: A = 10, B = 25, C = 18 - Output: Second biggest: 18
# a=int(input("enter A value:"))
# b=int(input("enter B value:"))
# c=int(input("enter C value:"))
# if a>b and a<c:
#     print("Second biggest is",a)
# elif b>a and b<c:
#      print("Second biggest is",b)  
# elif c>a and c<b:
#       print("Second biggest is",c)     

# 15: A year is a leap year if it is divisible by 4,
#  and (not divisible by 100 unless divisible by 400). - Input: Year = 2024 - Output: Leap year
# y=int(input("enter the year:"))
# if y%4==0 and y%100!=0:
#     print("Leap year")
# elif y%100==0 and y%400==0:
#     print("Leap year")
# else :
#     print("Not a leap year")    


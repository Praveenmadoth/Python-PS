# 1. Print Numbers from 1 to n
# n=int(input("enter the number:"))
# i=1
# while i<=n:
#     print(i)
#     i+=1

#  2. Print Numbers from m to n using loop
# m=int(input("enter the m value :"))
# n=int(input("enter the n value:"))
# while m<n:
#     print(m)
#     m+=1

#3. Print num from n to 1 in Reverse
# n=int(input("enter the number:"))
# i=1
# while i<=n:
#     print(n)
#     n-=1

# 4. Print Numbers from n to m in Reverse
# n=int(input("enter the n value:"))
# m=int(input("enter the m value :"))
# while n>=m:
#     print(n)
#     n-=1

# 5. Sum of n Natural Numbers
# n=int(input("enter the n value:"))
# i=0
# sum=0
# while i<=n:
#     sum=sum+i
#     i+=1
# print(sum)    

# 6.Factorial of a Number 
# n=int(input("enter the n value:"))
# f=1
# while n>=1:
#     f=f*n
#     n-=1
# print("factorial of the given number is :,",f)

#  7.sum of m to n
# n=int(input("enter the n value:"))
# m=int(input("enter the m value :"))
# sum=0
# while m>=n:
#     sum+=m
#     m-=1
# print("sum of the n and m is",sum) 

# 8.pruduct of n and m numbers
# n=int(input("enter the n value:"))
# m=int(input("enter the m value :"))
# mul=1
# while m>=n:
#     mul=mul*m
#     m-=1
# print("pruduct of the n and m is",mul) 

# 9.Print Factors of a Number
# n=int(input("enter the numbre:"))
# i=1
# print("the factorial of n is:")
# while i<n:
#     if n%i==0:
#         print(i,end=" ")
#     i+=1    
# print()

# 10. Count of Factors
# n=int(input("enter the numbre:"))
# i=1
# count=0
# print("the factorial of n is:")
# while i<=n:
#     if n%i==0:
#         print(i,end=" ")
#         count+=1
#         i+=1
#     else:
#         i+=1
# print()
# print(count)
# print("the count of n is",count)

# 11.Prime Number Check
# n=int(input("enter a number:"))
# if n<2:
#     print("not a prime ")
# i=2
# while i<n/2:
#     if n%i==0:
#         print("not Prime number")
#         break
#     i+=1
# else:
#     print("prime number")

# 12. Even Numbers from m to n
# n=int(input("enter the n value:"))#10
# m=int(input("enter the m value :"))#12
# while n<=m:
#     if n%2==0:
#         print(n,end=" ")
#         n+=1
#     n+=1
# print("are the even numbers")  
# 
# 13. Odd Numbers from m to n 
# n=int(input("enter the n value:"))#10
# m=int(input("enter the m value :"))#12
# while n<=m:
#     if n%2==1:
#         print(n,end=" ")
#         n+=1
#     n+=1
# print("are the odd numbers") 
# 
#14. Count of Even and Odd Numbers
# n=int(input("enter the n value:"))#10
# m=int(input("enter the m value :"))#12
# ecount=0
# ocount=0
# while n<=m:
#     if n%2==0:
#         n+=1
#         ecount+=1
#     else:

#         ocount+=1
#         n+=1
# print(ecount,"even count")
# print(ocount,"odd count")

# 15.Reverse a given string. Explanation:
#  Use slicing or loop. - Input: “hello” - Output: “olleh”
# name=input(" enter the name of string:")
# rev=name[::-1]
# print("reverse",rev)

# 16. Check for Palindrome String
# s = input("enter the string: ")
# rev = ""
# for i in s:          
#     rev = i + rev    # put current char in front
# if s==rev:
#     print("palindrome ")
# else:
#     print("not palindrome ")   

# #################
# 17. Sum of Digits
# Question: Calculate the sum of digits of a number. Explanation: 
# Use loop and % 10 to extract digits. - Input: 123 - Output: 6

# def sum_of_digits(n):
#     total_sum=0
#     while n>0:
#         r=n%10
#         total_sum+=r
#         n=n//10
#     return total_sum

# print(sum_of_digits(123))
# print(sum_of_digits(345))
# print(sum_of_digits(908))

# 18. Praduct of digits
# n=int (input("enter the number:"))
# def product_of_digits_(n):
#     # total_product= 1
#     pdt=1
#     while n>0:
#         r=n%10
#         pdt=pdt*r
#         n=n//10
#     return pdt   
# print(product_of_digits_(123))

# 19. Armstrong Number Check
# Question: Check if a number is an Armstrong number.
# #  Explanation: Sum of cube of digits equals the number. - Input: 153 - Output: Armstrong number
# def arm_strong_num(n):
#     x=len(str(n))
#     m=n
#     t_s=0
#     while n>0:
#         r=n%10
#         t_s+=r**x
#         n=n//10
#     if t_s==m:
#         return "armstrong number"
#     else:
#         return "armstrong number"
# print(arm_strong_num(153))

# 20.: Reverse the digits of a number.
#  Explanation: Use loop with % and // to reverse. - Input: 123 - Output: 321
# n=int(input("enter the value:"))
# rev=0
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# print(rev)    

# 21.Explanation: Compare number with its reverse. - Input: 121
#  - Output: Palindrome
# n=int(input("enter the value:"))
# m=n
# rev=0
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# if m==rev:
#     print("palindrome number")
# else:
#     print("not palindrome number")

# 22.: Count number of vowels in a string.
#  Explanation: Loop and check for a, e, i, o, u. - Input: “apple” - Output: 2
# str=input("enter the stringe:")
# v="aeiouAEIOU"
# oc=0
# i=len(str)-1
# while i>=0:
#     if str[i]  in v:
#         oc+=1
#         i-=1
#     else:
#       i-=1    
# print("vowels count is:",oc)
# # 23.count the consonents 
# str=input("enter the stringe:")
# v="aeiouAEIOU"
# cc=0
# i=len(str)-1
# while i>=0:
#     if str[i]not in v:
#         cc+=1
#         i-=1
#     else:    
#         i-=1    
# print("consonents count is:",cc)        

# 24.Count vowels and consonants in input string. Explanation: Maintain two counters. -
# Input: “apple” - Output: Vowels = 2, Consonants = 3
# str=input("enter the stringe:")
# v="aeiouAEIOU"
# oc=0
# cc=0
# i=len(str)-1
# while i>=0:
#     if str[i]  in v:
#         oc+=1
#         i-=1  
#     elif str[i] not  in v:
#         cc+=1     
#         i-=1
# print("vowel count is ",oc)
# print("consonents count is ",cc)



# 25. Explanation:
#  Sum of proper divisors equals the number. - Input: 28 - Output: Perfect number
# n=int(input("enter the number :"))
# mid=n//2
# # dp=0
# i=1
# s=0
# m=n
# while i<=mid:
#     if n%i==0:
#         s+=i
#         i+=1
#     else:
#         i+=1
# if s==m:
#     print("perfect number")
# else:
#     print("not perfect number")
    

# 26. Neon Number Check
# Question: Check if a number is a neon number.
# Explanation: Square the number, sum digits, match original. 
# - Input: 9 - Output: Neon number
# n=9
# res=n*n
# s=0
# while res>0:
#     r=res%10
#     s+=r
#     res//=10
# if s==n:
#     print(f"{n} is neon number")
# else:
#     print(f"{n} is not neon number")



# 27. Strong Number Check
# Question: Check if a number is a strong number.
# Explanation: Sum of factorial of digits equals the number. 
# - Input: 145 - Output: Strong number

# n=145
# m=n
# strong_sum=0
# while n>0:
#     r=n%10
#     fact=1
#     while r>0:
#         fact=fact*r
#         r-=1
#     strong_sum+=fact
#     n=n//10
# if strong_sum==m:
#     print(f"{m} is Strong number")
# else:
#      print(f"{m} is not Strong number")

# 28.: Check if a number is divisible by the sum of its digits. Explanation:
#  Calculate digit sum and check divisibility. - Input: 18 - Output: Harshad number

# n=18
# m=n
# sum1=0
# while n>0:
#     r=n%10
#     sum1+=r
#     n//=10
# if m%sum1==0:
#     print(f"{m} is harshad num")
# else:
#     print(f"{m} is not harshad num")


# 29. Fibonacci Series
# Question: Print the Fibonacci series up to n terms. 
# Explanation: Start with 0, 1 and continue with sum of last two. - 
# Input: n = 5 - Output: 0 1 1 2 3

# n=5
# a,b=0,1
# while n>0:
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
#     n-=1
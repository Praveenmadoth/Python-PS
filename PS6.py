# 1. Print All Prime Numbers from m to n
# Problem: Given a range from m to n, print all prime numbers in that range.
# m=int(input("enter the first no:"))
# n=int(input("enter the sec number:")) 
# for i in range (m,n+1):
#      count=0
#      for j in range (1,i+1):
#           if i%j==0:
#                count+=1
#      if count==2 :  
#           print(i,end=" ")

     
# 2. Count of All Prime Numbers from m to n
# Problem: Count how many prime numbers are there between m and n.

# m=int(input("enter the fist no:"))
# n=int(input("enter the sec number:")) 
# c=0
# for i in range (m,n+1):
#      count=0
#      for j in range (1,i+1):
#           if i%j==0:
#                count+=1
#      if count==2 :  
#           c+=1
#           print(i,end=" ")
#           print()
# print("the no of prime numbers bwt m,n are",c)  

# 3. Print All Armstrong Numbers in a Range
# Problem: Print all Armstrong numbers between m and n.
# n=int(input("enter the first no:"))
# m=int(input("enter the sec number:"))
# for i in range (n,m+1):
#     l=len(str(i))
#     sum1=0
#     tem=i
#     while i>0:
#         rev=i%10
#         sum1=sum1+(rev**l)
#         i=i//10
#     if sum1==tem:
#         print(tem,end=" ")
    # print()    

# 4.First Prime Number from m to n
# Problem: Find the first prime number in the given range.
# m=int(input("enter the first no:"))
# n=int(input("enter the sec number:")) 
# for i in range (m,n+1):
#      count=0
#      for j in range (1,i+1):
#           if i%j==0:
#                count+=1
#      if count==2 : 
#           print(i) 
#           break

# 
# 5. Last Prime Number from m to n
# m=int(input("enter the first no:"))
# n=int(input("enter the sec number:")) 
# for i in range (n,m-1,-1):
#      count=0
#      for j in range (1,i+1):
#           if i%j==0:
#                count+=1
#      if count==2 : 
#           print(i) 
#           break
# else:
#     print("not prime number in this range")

# 6. First Vowel in a Name
# name=input("enter the name:")
# vowel="aeiouAEIOU"
# l=len(name)-1
# for i in range(0,l):
#     if name[i]  in vowel:
#         print(name[i])
#         break

# 7. Last Vowel in a Name
# name=input("enter the name:")
# vowel="aeiouAEIOU"
# l=len(name)-1
# for i in range(l,0,-1):
#     if name[i]  in vowel:
#         print(name[i])
#         break

# 8. Print All Even Numbers Using Continue
# m=int(input("enter the first no:"))
# n=int(input("enter the sec number:"))
# print("even numbers from m to n is") 
# for i in range (m,n+1):
#     if i%2==1:
#         continue
#     print(i,end=" ")

# 9. Print All Odd Numbers Using Continue
# m=int(input("enter the first no:"))
# n=int(input("enter the sec number:"))
# print("even numbers from m to n is") 
# for i in range (m,n+1):
#     if i%2==0:
#         continue
#     print(i,end=" ")

# 10. Count of Prime and Composite Numbers from m to n
# m=int(input("enter the first no:"))
# n=int(input("enter the sec number:"))

# primec=0
# compositec=0
# for i in range (m,n+1):
#      count=0
#      for j in range (1,i+1):
#           if i%j==0:
#                count+=1
#      if count==2 :
       
#           primec+=1
#      else:
#           compositec+=1
# print(primec)   
# print(compositec)  




        








# write internal code of 
#        swapcase( ) ,
#        strip( ) ,
#       replace( )  built in functions
# 1.Swap case
# def swapp(name):
#     if len(name)==0:
#         return
#     res=""
#     for i in name:
#         if ord(i)>=65 and ord(i)<=97:
#             res+=chr(ord(i)+32)
#         elif ord(i)>=97 and ord(i)<=122:
#             res+=chr(ord(i)-32)
#         else:
#             res+=i
#     return res  

# name="PrAvEeN"   
# print(swapp(name))

# 2.strip( )
# in="  praveenn  "
# op=="praveen"
# name = input("enter str: ")
# while len(name) > 0 and name[0] == " ":
#     name = name[1:]
# while len(name) > 0 and name[-1] == " ":
#     name = name[:-1]
# print(name)
#  finding 1st max and second max

# 3.replace( )
# def my_replace(text, old, new):
#     result = ""
#     i = 0
#     while i < len(text):
#         if text[i:i+len(old)] == old:
#             result += new       
#             i += len(old)       
#         else:
#             result += text[i]   
#             i += 1
#     return result
# text = "I like java because java is easy"
# print(my_replace(text, "java", "python"))










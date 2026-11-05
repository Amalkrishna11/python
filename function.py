# functiom is a block of code use to perform specifc task

# def function_name(parameters):
#    # function body
#    return 'result'


# function_name(arguments)

# def greet():
#     print("Hello")
# greet()


# def greet(user):
#     print(f"Hello {user}")

# greet("alan")

# def greet(user):
    # return f"Hello {user}"

# result = greet("alan")
# print(result)


# def greet(msg,user ='guest'):# default parameter
#  return f"Hello,{user}!!{msg}..."
# result1 = greet('good morning', 'alan')
# result2 = greet('good evening')
# print(result1)
# print(result2)


# def add(a,*args):# *args is used to pass variable number of arguments to a function
#     sum = a
#     for n in args:
#         sum += n
#     print(f"sum IS :{sum}")

#  add("hello"45,56)
# add(10,20,30,40,50) #arbitrary number of arguments

# def greet(msg,user):
#     return f"Hello,{user}!!{msg}..."

# print(greet(user='jithu',msg='good morning')) #keyword arguments

# def greet(**kwargs):
#     print(kwargs)

# greet(name='jithu', msg='good morning') # arbitrary keyword arguments


# ---------->calculator using function<--------------

# def add(a,b):
#     return a+b  
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# while True:
#     choice = input('+ ---> add\n- ---> sub\n* ---> mul\n/ ---> div\n1 ---> quit\nEnter your choice:')
#     try:
#         n1 = int(input("Enter the first number:"))
#         n2 = int(input("Enter the second number:"))
#     except ValueError,:
#         print("integer are only allowed")
#         continue
#     match choice.strip():
#         case '+':
#             print(add(n1,n2))
#         case '-':
#             print(sub(n1,n2))
#         case '*':
#             print(mul(n1,n2))
#         case '/':
#             print(div(n1,n2))
#         case '1':
#             break
#         case _:
#             print("invalid entry")


# ------------->zerodivision<-----------------

# def add(a,b):
#     return a+b  
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     if b == 0:
#         return "Error: Division by zero is not allowed."
#     return a/b
# while True:
#     choice = input('+ ---> add\n- ---> sub\n* ---> mul\n/ ---> div\n1 ---> quit\nEnter your choice:')
#     try:
#         n1 = int(input("Enter the first number:"))
#         n2 = int(input("Enter the second number:"))
#     except ValueError,:
#         print("integer are only allowed")
#         continue
#     match choice.strip():
#         case '+':
#             print(add(n1,n2))
#         case '-':
#             print(sub(n1,n2))
#         case '*':
#             print(mul(n1,n2))
#         case '/':
#             print(div(n1,n2))
#         case '1':
#             break
#         case _:
#             print("invalid entry")


# --------->lambda function<----------------------

n= 5

# def square(x):
#     return x*x
# print(square(n))
# print(square(4))
# print(square(5))
# print(square(7))


# square = lambda x: x*x
# print(square(n))
# print(square(4))
# print(square(5))
# print(square(7))

# def type_of_number(n):
#     if n>0:
#         return "positive"

#     elif n<0:
#         return "negative"
#     else:
#         return "zero" 


# true expression if condition else false expression

# check_type = lambda n: "positive" if n>0 else "negative" if n<0 else "zero"
# print(check_type(8))
# print(check_type(-8))
# print(check_type(0))






        




   
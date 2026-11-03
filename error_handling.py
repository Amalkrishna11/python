# 1.NameError - variable not defined
# print(x)


# 2. Typeerror - invalid type used in the operation
# print(1+'1')
# 3. valueerror - wrong value is used in the operation
# print(int('helllo'))

# 4.indexerror - index is out of range
# li = [1,2]
# print(li[5])
  
# 5. Keyerror - key is not present in the dictionary
# d = {'a':1}
# print(d['b'])

# 6. Attributeerror - attribute is not present in the object
# print("hello".upper())

# 7. ZeroDivisionError - division by zero
# print(1/0)

# 8. FileNotFoundError - file is not present in the directory
# 9.moduleNotFoundError - module is not present in the directory

# exception handling
# syntax:
# try:
#     # code that may generate error
# except exceptionclass:
#     # code to handle the exception
# else:
#     # code to execute if no exception is raised       
# finally:
#     # code to execute in  any case

# try:
#     n= int(input("Enter a number: "))
#     print(56/n)
# except ValueError:
#     print("only integer value are allowed")
# except ZeroDivisionError:
#     print("division by zero is not allowed")
# except (valueError, ZeroDivisionError):
#     print("only integer value are allowed and division by zero is not allowed")

# except Exception as e:
#     print("error occured:")
# else:
#     print(reseult)
# finally:
#     print("exceptiom completed")
# print("after try except block")
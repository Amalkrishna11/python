'''
list is a collection of hetrogenous data.
-ordered
-indexed
-allow duplicates
-mutable

'''
numbers = [12,12,1,21,23,45,4,77,]
print(numbers)
print(type(numbers))
print(len(numbers))
print(numbers[6])
print(numbers[-1])
print(numbers[1:6])
print(numbers[-7:-2])
print(numbers[:-2])
print(numbers[4:])
print(numbers[::2])
print(numbers[::-2])
print(numbers[::-1])
print(numbers[0])
numbers[4]= 100
numbers.append(867)
numbers.append(8)
numbers.insert(1,23)
# numbers.extend("wayane")
numbers.extend([12,34,56])



print(numbers)
event_count = 0
for n in numbers:
    if  n%2 == 0:
        event_count +=1
print(event_count)



l2 = []
l3 = list("karthi")
print(numbers)
print(l3)
print(l3 in numbers)



print(numbers.count(77))
print(numbers.index(100))
print(22 in numbers)
print(22 not in numbers)


# l4 = numbers.copy()
# l4[1]= "jobin"
# print(l4)
# print(numbers)
# print(l4 in numbers)

# nunber.sort(reverse=true)
# numbers.reverse()
# print(numbers)
# l5 = [[12,12,12],[23,45,67],[67,76,65]]
# print(l5)
# print(l5[1][2])
# l6 = l5.copy() 
# l6[1][2]= 555
# l6 [2]=56

# print(l5)
# print(l6)

# for x in l5:
#     for n in x:
#         print(n)

# number = [78,96,77,36,10,2,75,34]

# square_nubers = []
# for n in number:
#     square_nubers.append(n*n)
# print(square_nubers)



# comp

# squared_numbers = [ n*n for n in number]
# print(squared_numbers)


# [expression for item in iterable if clause]

number = [78,96,77,36,10,2,75,34]

s = ["even" if n % 2 == 0 else "odd" for n in number]
print(s)



    






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
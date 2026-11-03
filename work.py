# -------------------------->pdf -1<---------------------------------------------------

# 1. Write a program to add two numbers entered by the user. 

# n = int(input("enter the 1st number"))
# m = int(input("enter the 2nd number"))
# print(n+m)

# Write a program to find the difference between two numbers.

# n = int(input("enter the 1st number"))
# m = int(input("enter the 2nd number")) 
# print(n-m)

#Write a program to multiply three numbers. 

# n = int(input("enter the 1st number"))
# m = int(input("enter the 2nd number"))
# o = int(input("enter the 3rd number"))
# print(n*m*o)

# # 4. Write a program to divide one number by another. 
# n = int(input("enter the 1st number"))
# m = int(input("enter the 2nd number"))
# print(n/m)

# 5. Write a program to calculate the square of a number.  
# n= int(input("enter a number"))
# print(n*n)

# 6. Write a program to calculate the cube of a number. 
# n= int(input("enter a number"))
# print(n*n*n)


# 7. Write a program to calculate the average of three numbers.
# n = int(input("enter the 1st number"))
# m = int(input("enter the 2nd number"))
# o = int(input("enter the 3rd number"))

# l = (n+m+o)
# result = (l/2)
# print(result)

#Write a program to calculate the total price of 5 notebooks if the price of one notebook is entered by the user. 
# n = int(input("enter the price of one note book"))
# price = n * 5
# print("price of 5 books:",price)


# 9. Write a program to find the quotient and remainder when one integer is divided by another. 

# a = int(input("enter the number"))
# b = int(input("enter the 2nd number"))

# quotient  = a//b
# remainder = a%b

# print("quotient :",quotient)
# print("remainder:",remainder)


# 10. A shop has 47 chocolates. If each box holds 6 chocolates, calculate: ● The number of completely filled boxes. ● The number of chocolates left over. 

# number_of_chocolates = 47
# chocolates_holds = 6
# filled = number_of_chocolates//chocolates_holds
# left = number_of_chocolates%chocolates_holds
# print("The number of completely filled boxes:",filled)
# print("he number of chocolates left over:",left)

# 11. Write a program to convert a given number of minutes into complete hours and remaining minutes. 

# minutes = int(input("Enter the number of minutes: "))

# hours = minutes // 60
# remaining_minutes = minutes % 60

# print("Complete hours =", hours)
# print("Remaining minutes =", remaining_minutes)

# 12. Write a program to convert 367 seconds into minutes and remaining seconds.

# seconds = 367

# minutes = seconds // 60
# remaining_seconds = seconds % 60

# print("Minutes =", minutes)
# print("Remaining seconds =", remaining_seconds)

# 13. A teacher wants to distribute 53 students into groups of 8. Calculate the number of complete groups and the students left over.


# students = 53
# group_size = 8
# complete_groups = students // group_size
# leftover_students = students % group_size
# print("Complete groups =", complete_groups)
# print("Students left over =", leftover_students)


# 14. Write a program to extract the last digit of a positive integer using the modulus operator. 

# num = int(input("Enter a positive integer: "))

# last_digit = num % 10

# print("Last digit =", last_digit)

# 15Write a program to remove the last digit of a positive integer using floor division.
# num = int(input("Enter a positive integer: "))

# result = num // 10

# print("Number after removing the last digit =", result)

# 16. Shopping bill: A customer buys 3 pens costing ₹15 each and 2 notebooks costing ₹40 each. Calculate the total bill
# pens = 3
# pen_price = 15

# notebooks = 2
# notebook_price = 40

# total_bill = (pens * pen_price) + (notebooks * notebook_price)

# print("Total bill = ₹", total_bill)

# 17. Salary calculation: An employee earns ₹800 per day. Calculate their salary for 26 working days. 

# salary = 800
# day = 26
# total = salary*day
# print("total salary",total)

# 18. Distance conversion: Convert a distance given in kilometers into meters and centimeters.

# kilometer = int(input("enter the distance in kilometers"))
# meter = kilometer*1000
# centimeter = kilometer*100000
# print("distance in meter",meter)
# print("distance in centimeter",centimeter)

# 19. Rectangle: Accept the length and width of a rectangle and calculate its area and perimeter. 


# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))

# area = length * width
# perimeter = 2 * (length + width)

# print("Area of rectangle =", area)
# print("Perimeter of rectangle =", perimeter)     


# 20. Simple interest: Accept the principal amount, annual interest rate, and time in years. Calculate the simple interest


# P = float(input("Enter the principal amount: "))
# R = float(input("Enter the annual interest rate: "))
# T = float(input("Enter the time in years: "))

# SI = (P * R * T) / 100

# print("Simple Interest =", SI)

# 21.Bill sharing: Accept a restaurant bill and the number of friends. Calculate how much each friend should pay if the bill is shared equally


# bill = float(input("Enter the restaurant bill: "))
# friends = int(input("Enter the number of friends: "))

# share = bill / friends

# print("Each friend should pay =", share)

# 22. Travel calculation: A car travels 180 km using 12 liters of fuel. Calculate its mileage in km per liter

# distance = 180
# fuel = 12

# mileage = distance / fuel

# print("Mileage:", mileage, "km/l")

# 23. Unit price: Accept the total price of a packet of rice and its weight in kilograms. Calculate the price per kilogram.

# total_price = float(input("Enter total price of rice: "))
# weight = float(input("Enter weight in kg: "))

# price_per_kg = total_price / weight

# print("Price per kg =", price_per_kg)

# 24. Time conversion: Accept a total number of hours and convert it into complete days and remaining hours. 

# hours = int(input("Enter total number of hours: "))

# days = hours // 24
# remaining_hours = hours % 24

# print("Days =", days)
# print("Remaining hours =", remaining_hours)

# 25. Power calculation: Accept a number and an exponent, then calculate the result using the ** operator.

# number = int(input("Enter a number:"))
# exponent = int(input("enter an exponent:"))
# result = number ** exponent
# print("Result =",result)

# ---------------------------------------------->pdf -2<---------------------------------------------------
# 1.College Event Registration

# age = int(input("Enter your age: "))
# student = input("Are you a student? (yes/no): ")

# if age >= 18 and age <= 25 and student == "yes":
#     print("Eligible for registration")
# else:
#     print("Not eligible for registration")

# 2. Online Shopping Discount

# amount = float(input("Enter order amount: "))
# membership = input("Are you a premium member? (yes/no): ")

# if amount >= 3000 or membership == "yes":
#     print("Customer qualifies for discount")
# else:
#     print("Customer does not qualify for discount")

# 3. Airport check-in 

# ticket = input("Is your ticket confirmed? (yes/no): ")
# passport = input("Is your passport valid? (yes/no): ")
# hours = float(input("Hours remaining until departure: "))

# if ticket == "yes" and passport == "yes" and hours > 2:
#     print("Online check-in is available")
# else:
#     print("Online check-in is not available")

# 4.Movie Ticket Booking

# age = int(input("enter your age:"))
# if age < 12 or age >= 60:
#     print("Qualified for Special Tickets")
# else:
#     print("Not Qualified for Special Tickets")

# 5. Bank Loan Pre - Eligiblity

# income = float(input("Enter monthly income: "))
# credit_score = int(input("Enter credit score: "))
# default = input("Do you have an existing loan default? (yes/no): ")

# if income >= 40000 and credit_score >= 700 and default == "no":
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")

# 6.Food Delivery Free Shipping

# amount = float(input("Enter order amount: "))
# premium = input("Premium membership? (yes/no): ")
# disabled = input("Is delivery temporarily disabled? (yes/no): ")

# if (amount >= 500 or premium == "yes") and disabled == "no":
#     print("Free delivery available")
# else:
#     print("Free delivery not available")

# 7.Employee Work from Home

# months =int(input("Enter months worked in company:" ))
# remote = input("Does the project allow remote work?(yes/no):")

# if months >=6 and remote == "yes":
#     print("Eligible to Work from Home")
# else:
#     print("Not Eligible to Work from Home")

#8.Hotel Room Booking

# available = input("Is the room available? (yes/no): ")
# payment = input("Is the payment method valid? (yes/no): ")
# stopped = input("Has the hotel stopped reservations? (yes/no): ")

# if available == "yes" and payment == "yes" and stopped == "no":
#     print("Booking can proceed")
# else:
#     print("Booking cannot proceed")

# 9. Online Access Exam

# logged = input("Is the student logged in? (yes/no): ")
# registered = input("Is exam registration confirmed? (yes/no): ")
# active = input("Is the exam active? (yes/no): ")
# blocked = input("Is the account blocked? (yes/no): ")

# if logged == "yes" and registered == "yes" and active == "yes" and blocked == "no":
#     print("Student can access the exam")
# else:
#     print("Student cannot access the exam")

# # 10. Gym Membership plan 

# years = float(input("Enter membership duration in years:"))
# active =input("Is Membership Active?(yes/no):")
# yearly = input("Has the member purchased a yearly plan?(yes/no):")

# if (years >=1 and active == "yes") or yearly == "yes":
#     print("Eligible for premium upgrade")
# else:
#     print("Not eligible for premium upgrade")

# 11. Ride Booking Application

# service = input("Is pickup within the service area? (yes/no): ")
# driver = input("Is a driver available? (yes/no): ")
# scheduled = input("Are scheduled rides enabled? (yes/no): ")

# if (service == "yes" and driver == "yes") or scheduled == "yes":
#     print("Booking is available")
# else:
#     print("Booking is not available")

# 12. E-Commerce Product Return

# days = int(input("Days since purchase: "))
# unused = input("Is the product unused? (yes/no): ")
# eligible = input("Is the product eligible for return? (yes/no): ")

# if days <= 7 and unused == "yes" and eligible == "yes" and days >= 0:
#     print("Return request accepted")
# else:
#     print("Return request rejected")

# 13. Library Book Borrowing

# overdue = input("Do you have overdue books? (yes/no): ")
# active = input("Is library membership active? (yes/no): ")
# available = input("Is the requested book available? (yes/no): ")

# if overdue == "no" and active == "yes" and available == "yes":
#     print("Student can borrow the book")
# else:
#     print("Student cannot borrow the book")

# 13. Library Book Borrowing
# overdue = input("Do you have overdue books? (yes/no): ")
# active = input("Is library membership active? (yes/no): ")
# available = input("Is the requested book available? (yes/no): ")
# if overdue == "no" and active == "yes" and available == "yes":   
#     print("Student can borrow the book")
# else:   
#     print("Student cannot borrow the book")



# 14. Job Application Screening
# experience = float(input("Enter Python experience in years: "))
# django = input("Do you know Django? (yes/no): ")
# fastapi = input("Do you know FastAPI? (yes/no): ")
# if experience >= 3 or (experience >= 1 and (django == "yes" or fastapi == "yes")):   
#      print("Candidate qualifies for the next stage")
# else:    
#     print("Candidate does not qualify for the next stage")



# # 15. Mobile Data Usage Alert
# usage = float(input("Enter data usage percentage: "))
# remaining = float(input("Enter remaining data in GB: "))
# unlimited = input("Is the data plan unlimited? (yes/no): ")
# if (usage >= 90 or remaining < 1) and unlimited == "no":    
#     print("Warning: Data usage is high")
# else:    
#     print("No warning")



# 16. Parking Lot Entry
# pass_valid = input("Do you have a valid parking pass? (yes/no): ")
# visitor = input("Are you paying for visitor parking? (yes/no): ")
# full = input("Is the parking lot full? (yes/no): ")
# if (pass_valid == "yes" or visitor == "yes") and full == "no":
#     print("Vehicle can enter")
# else:    
#     print("Vehicle cannot enter")



# 17. Scholarship Eligibility
# score = float(input("Enter academic score: "))
# attendance = float(input("Enter attendance percentage: "))
# if (score >= 85 and attendance >= 75) or score >= 95:    
#     print("Student is eligible for scholarship")
# else:    
#     print("Student is not eligible for scholarship")



# 18. Food Ordering – Restaurant Availability
# opened = input("Is the restaurant open? (yes/no): ")
# delivery = input("Does it deliver to your location? (yes/no): ")
# orders = input("Is it accepting online orders? (yes/no): ")
# if opened == "yes" and delivery == "yes" and orders == "yes":    
#     print("Order can be placed")
# else:    
#     print("Order cannot be placed")



# 19. Smart Home Security
# motion = input("Is motion detected? (yes/no): ")
# door = input("Is the main door open? (yes/no): ")
# armed = input("Is the security system armed? (yes/no): ")
# if armed == "yes" and (motion == "yes" or door == "yes"):    
#     print("Security alert triggered")
# else:    
#     print("Security alert not triggered")



# 20. Travel Insurance Eligibility
# age = int(input("Enter age: "))
# days = int(input("Enter trip duration in days: "))
# covered = input("Is the country covered by insurance? (yes/no): ")
# excluded = input("Is the destination excluded from coverage? (yes/no): ")
# if age >= 18 and age <= 65 and days > 0 and days <= 30 and covered == "yes" and excluded == "no":    
#     print("Eligible for travel insurance")
# else:    
#     print("Not eligible for travel insurance")

# --------------------->pdf -3<---------------------------------------------------


# 1.student grade calculator
# mark = int(input("Enter student mark: "))

# if mark >= 90 and mark <= 100:
#     print("Grade: A+")
# elif mark >= 80:
#     print("Grade: A")
# elif mark >= 70:
#     print("Grade: B")
# elif mark >= 60:
#     print("Grade: C")
# elif mark >= 50:
#     print("Grade: D")
# elif mark >= 0:
#     print("Fail")
# else:
#     print("Invalid mark")


# 2. atm withdrawal system
# balance = int(input("Enter account balance: "))
# amount = int(input("Enter withdrawal amount: "))

# if amount > balance:
#     print("Insufficient Balance")
# elif amount % 100 != 0:
#     print("Enter an amount in multiples of 100")
# else:
#     print("Withdrawal Successful")
#     print("Remaining Balance:", balance - amount)

# 3.online shoping delivery 

# amount = int(input("Enter order amount: "))

# if amount >= 5000:
#     delivery = 0
# elif amount >= 2000:
#     delivery = 50
# else:
#     delivery = 100

# print("Delivery Charge:", delivery)
# print("Final Amount:", amount + delivery)

# 4.employee performance rating
# score = int(input("Enter performance score: "))

# if score >= 90:
#     print("Excellent")
# elif score >= 75:
#     print("Very Good")
# elif score >= 60:
#     print("Good")
# elif score >= 40:
#     print("Needs Improvement")
# else:
#     print("Poor")

# 5.electricity bill calculation

# units = int(input("Enter units consumed: "))

# if units <= 100:
#     bill = units * 2
# elif units <= 200:
#     bill = (100 * 2) + (units - 100) * 3
# elif units <= 400:
#     bill = (100 * 2) + (100 * 3) + (units - 200) * 5
# else:
#     bill = (100 * 2) + (100 * 3) + (200 * 5) + (units - 400) * 7

# print("Electricity Bill:", bill)


# 6.movie ticket pricing
# age = int(input("Enter your age: "))

# if age < 5:
#     price = 0
# elif age <= 12:
#     price = 100
# elif age <= 59:
#     price = 200
# else:
#     price = 120

# print("Ticket Price:", price)

# 7 . traffic fine system

# speed = int(input("Enter vehicle speed: "))

# if speed <= 60:
#     print("No Fine")
# elif speed <= 80:
#     print("Fine: Rs.500")
# elif speed <= 100:
#     print("Fine: Rs.1000")
# else:
#     print("Fine: Rs.2000")
#     print("License Review")

# 8. resturant billing systeam
# bill = int(input("Enter total bill: "))

# if bill >= 5000:
#     discount = bill * 20 / 100
# elif bill >= 3000:
#     discount = bill * 15 / 100
# elif bill >= 1000:
    # discount = bill * 10 / 100
# else:
    # discount = 0

# final_bill = bill - discount

# print("Discount:", discount)
# print("Final Bill:", final_bill)

# 9. college admission decision
# score = int(input("Enter entrance exam score: "))

# if score >= 90:
#     print("Direct Admission")
# elif score >= 75:
#     print("Admission + Interview")
# elif score >= 60:
#     print("Waitlisted")
# else:
#     print("Not Eligible")

# 10.bank loan risk category
# score = int(input("Enter credit score: "))
# default = input("Existing loan default (yes/no): ")

# if default == "yes":
#     print("Loan Approval Requires Manual Review")
# else:
#     if score >= 750:
#         print("Low Risk")
#     elif score >= 650:
#         print("Medium Risk")
#     elif score >= 550:
#         print("High Risk")
#     else:
#         print("Very High Risk")

# 11.hotel room pricing

# room = input("Enter room type: ")
# nights = int(input("Enter number of nights: "))

# if room == "Standard":
#     price = 2000
# elif room == "Deluxe":
#     price = 3500
# elif room == "Suite":
#     price = 5000
# else:
#     price = 0
#     print("Invalid Room Type")

# total = price * nights

# if nights > 5:
#     total = total - (total * 10 / 100)

# print("Final Bill:", total)

# 12.employe bonus calculator

# salary = int(input("Enter annual salary: "))
# performance = int(input("Enter performance score: "))

# if performance >= 90:
#     bonus = salary * 20 / 100
# elif performance >= 75:
#     bonus = salary * 15 / 100
# elif performance >= 60:
#     bonus = salary * 10 / 100
# else:
#     bonus = 0

# print("Annual Bonus:", bonus)

# 13.mobile data plan
# data = int(input("Enter monthly data usage in GB: "))

# if data < 5:
#     print("Basic Plan - Rs.199")
# elif data <= 20:
#     print("Standard Plan - Rs.399")
# elif data <= 50:
#     print("Premium Plan - Rs.699")
# else:
#     print("Unlimited Plan - Rs.999")

# 14.parking fee calculator
# hours = int(input("Enter parking hours: "))
# vehicle = input("Is it an electric vehicle? (yes/no): ")

# if hours <= 2:
#     fee = 30
# elif hours <= 5:
#     fee = 50
# elif hours <= 10:
#     fee = 100
# else:
#     fee = 150

# if vehicle == "yes":
#     fee = fee - (fee * 20 / 100)

# print("Final Parking Fee:", fee)

# 15.online exam result
# theory = int(input("Enter theory mark: "))
# practical = int(input("Enter practical mark: "))

# if theory >= 40 and practical >= 40:
#     average = (theory + practical) / 2

#     if average >= 75:
#         print("Distinction")
#     elif average >= 60:
#         print("First Class")
#     elif average >= 50:
#         print("Second Class")
#     else:
#         print("Pass")
# else:
#     print("Fail")

# 16.fligthing bagging fee

# weight = int(input("Enter baggage weight: "))
# travel = input("Enter class (Economy/Business): ")

# if travel == "Business":
#     limit = 25
# else:
#     limit = 15

# if weight <= limit:
#     charge = 0
# elif weight <= 20:
#     charge = 500
# elif weight <= 30:
#     charge = 1000
# else:
#     charge = 2000

# print("Baggage Charge:", charge)

# 17.e commerce return eligibility
# days = int(input("Enter days since purchase: "))
# unused = input("Is the product unused? (yes/no): ")
# returnable = input("Is the product returnable? (yes/no): ")

# if days > 7:
#     print("Return Rejected: Purchase is older than 7 days")
# elif unused != "yes":
#     print("Return Rejected: Product is used")
# elif returnable != "yes":
#     print("Return Rejected: Product is not returnable")
# else:
#     print("Return Approved")

# 18.salary tax calculator

# salary = int(input("Enter annual salary: "))

# if salary <= 300000:
#     tax = 0
# elif salary <= 600000:
#     tax = salary * 5 / 100
# elif salary <= 1000000:
#     tax = salary * 10 / 100
# else:
#     tax = salary * 20 / 100

# final_salary = salary - tax

# print("Tax Amount:", tax)
# print("Salary After Tax:", final_salary)

# 19.ride fare calculator
# distance = int(input("Enter distance in km: "))
# peak = input("Is it peak hour? (yes/no): ")

# if distance <= 5:
#     fare = 100
# elif distance <= 15:
#     fare = 100 + (distance - 5) * 15
# elif distance <= 30:
#     fare = 100 + (10 * 15) + (distance - 15) * 12
# else:
#     fare = 100 + (10 * 15) + (15 * 12) + (distance - 30) * 10

# if peak == "yes":
#     fare = fare + (fare * 20 / 100)

# print("Final Ride Fare:", fare)

# 20.employee leave approval system
# available = int(input("Enter available leave days: "))
# requested = int(input("Enter requested leave days: "))

# if requested > available:
#     print("Leave Rejected")
# elif requested <= 3:
#     print("Leave Automatically Approved")
# elif requested <= 7:
#     print("Manager Approval Required")
# else:
#     print("HR Approval Required")



# ----------------->pdf -4 list practice<---------------------------------------------------
# 1.Find the Largest Element

# numbers =[10,5,25,8,15]
# largest = numbers[0]

# for i in numbers:
#     if i > largest:
#         largest = i
# print("Largest element:",largest)

# # 2.find the smallest element

# numbers = [10,5,25,8,15]
# smallest = numbers[0]

# for i in numbers:
#    if i < smallest:
#        smallest = i
# print("smallest element:",smallest)

# # 3. Find Sum of all Elements

# numbers = [1, 2, 3, 4, 5]

# total = 0

# for i in numbers:
#     total = total + i

# print("Sum:", total)

# # 4. Find Average of Elements

# numbers = [10, 20, 30, 40, 50]

# total = 0

# for i in numbers:
#     total = total + i

# average = total / len(numbers)

# print("Average:", average)

# # 5. Reverse a List Without Using reverse()

# numbers = [1, 2, 3, 4, 5]

# reverse = []

# for i in numbers:
#     reverse = [i] + reverse

# print(reverse)

# # Part 2: Logic-Based List Questions
# # 1. Remove Duplicates

# numbers = [1, 2, 2, 3, 4, 4, 5]

# result = []

# for i in numbers:
#     if i not in result:
#         result.append(i)

# print(result)

# # 2. Find Second Largest Number

# numbers = [10, 20, 50, 40, 30]

# largest = numbers[0]
# second = numbers[0]

# for i in numbers:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second and i != largest:
#         second = i

# print("Second largest:", second)

# # 3. Separate Even and Odd Numbers

# numbers = [1, 2, 3, 4, 5, 6]

# even = []
# odd = []

# for i in numbers:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print("Even numbers:", even)
# print("Odd numbers:", odd)

# # 4. Find Common Elements Between Two Lists

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# common = []

# for i in list1:
#     if i in list2:
#         common.append(i)

# print("Common elements:", common)

# # 5. Merge Two Lists Without Duplicates

# list1 = [1, 2, 3]
# list2 = [3, 4, 5]

# result = []

# for i in list1:
#     if i not in result:
#         result.append(i)

# for i in list2:
#     if i not in result:
#         result.append(i)

# print("Merged list:", result)


# # Part 3: Nested List Questions
# # 1. Sum of All Elements in a Matrix

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# total = 0

# for row in matrix:
#     for i in row:
#         total = total + i

# print("Total sum:", total)

# # 2. Find Largest Element in Matrix

# matrix = [
#     [1, 2, 3],
#     [10, 5, 6],
#     [7, 8, 9]
# ]

# largest = matrix[0][0]

# for row in matrix:
#     for i in row:
#         if i > largest:
#             largest = i

# print("Largest element:", largest)

# --------------------------->next pdf -5 set operations<--------------------------------------------------- 
# --1q--
# 1. Students Enrolled in Courses A training institute offers two courses: 
# • Python course students
#  • Data Analytics course students
#  python_students = {"Arun", "Megha", "Rahul", "Sneha"} 
# analytics_students = {"Sneha", "Rahul", "Aman", "Diya"} 
# Tasks 1. Find students enrolled in both courses.
#  2. Find students enrolled only in Python. 
# 3. Find students enrolled only in Data Analytics. 
# 4. Find all unique students.
#  5. Find students enrolled in exactly one course. 

# ---ans---
# python_students = {"Arun", "Megha", "Rahul", "Sneha"}
# analytics_students = {"Sneha", "Rahul", "Aman", "Diya"}

# # 1. Students in both courses
# print("Both courses:", python_students & analytics_students)

# # 2. Only Python
# print("Only Python:", python_students - analytics_students)

# # 3. Only Data Analytics
# print("Only Data Analytics:", analytics_students - python_students)

# # 4. All unique students
# print("All students:", python_students | analytics_students)

# # 5. Exactly one course
# print("Exactly one course:", python_students ^ analytics_students)

# ---2q--
# 2. Mobile Brands Purchased by Customers Two customers purchased different mobile brands. 
# customer1 = {"Samsung", "Apple", "OnePlus", "Realme"}
# customer2 = {"Apple", "Vivo", "Oppo", "Samsung"} 
# Tasks 
# 1. Find common brands purchased by both customers.
# 2. Find all brands purchased. 
# 3. Find brands purchased only by customer1.
# 4. Find brands purchased by only one customer

# ---2ans--
# customer1 = {"Samsung", "Apple", "OnePlus", "Realme"}
# customer2 = {"Apple", "Vivo", "Oppo", "Samsung"}

# # 1. Common brands
# print("Common brands:", customer1 & customer2)

# # 2. All brands
# print("All brands:", customer1 | customer2)

# # 3. Only customer1
# print("Only customer1:", customer1 - customer2)

# # 4. Only one customer
# print("Only one customer:", customer1 ^ customer2)

# ---3q---
# 3. Employees Using Software Tools
# Employees in two departments use different software tools.
# design_team = {"Figma", "Photoshop", "Canva", "Illustrator"} 
# marketing_team = {"Canva", "Excel", "Photoshop", "PowerBI"} 
# Tasks
# 1. Find tools used by both teams.
# 2. Find tools exclusive to the design team.
# 3. Find all software tools used in the company. 
# 4. Find tools used by only one team.
# ---3ans--

# design_team = {"Figma", "Photoshop", "Canva", "Illustrator"}
# marketing_team = {"Canva", "Excel", "Photoshop", "PowerBI"}

# # 1. Common tools
# print("Common tools:", design_team & marketing_team)

# # 2. Exclusive design tools
# print("Design team only:", design_team - marketing_team)

# # 3. All tools
# print("All tools:", design_team | marketing_team)

# # 4. Tools used by only one team
# print("Only one team:", design_team ^ marketing_team)


# ---4q--
# 4. Cricket and Football Fans
# A survey collected sports preferences of students.
# cricket_fans = {"Ajay", "Kiran", "Rohit", "Nisha"} 
# football_fans = {"Nisha", "Rahul", "Ajay", "David"} 
# Tasks 
# 1. Find students who like both sports. 
# 2. Find students who like only cricket. 
# 3. Find students who like only football.
# 4. Find all sports fans. 

# ---4ans---
# cricket_fans = {"Ajay", "Kiran", "Rohit", "Nisha"}
# football_fans = {"Nisha", "Rahul", "Ajay", "David"}

# # 1. Both sports
# print("Both sports:", cricket_fans & football_fans)

# # 2. Only cricket
# print("Only cricket:", cricket_fans - football_fans)

# # 3. Only football
# print("Only football:", football_fans - cricket_fans)

# # 4. All fans
# print("All fans:", cricket_fans | football_fans)


# ----5q---
# 5. Online Shopping Categories
# A customer purchased products from two categories.
# electronics = {"Laptop", "Headphones", "Mouse", "Keyboard"} 
# accessories = {"Keyboard", "Mouse Pad", "Laptop Stand", "Headphones"} 
# Tasks 
# 1. Find common purchased products.
# 2. Find products only in electronics.
# 3. Find all purchased items.
# 4. Find products available in only one category. 

# ---5ans---
# electronics = {"Laptop", "Headphones", "Mouse", "Keyboard"}
# accessories = {"Keyboard", "Mouse Pad", "Laptop Stand", "Headphones"}

# # 1. Common products
# print("Common products:", electronics & accessories)

# # 2. Only electronics
# print("Only electronics:", electronics - accessories)

# # 3. All products
# print("All products:", electronics | accessories)

# # 4. Products in only one category
# print("Only one category:", electronics ^ accessories)

# ---6q---
# 6. Languages Known by Employees

# ---6ans---
# employee1 = {"Python", "Java", "SQL", "C"}
# employee2 = {"Python", "JavaScript", "SQL", "Go"}

# # 1. Common languages
# print("Common languages:", employee1 & employee2)

# # 2. Only employee1
# print("Only employee1:", employee1 - employee2)

# # 3. All unique languages
# print("All languages:", employee1 | employee2)

# # 4. Languages known by only one employee
# print("Only one employee:", employee1 ^ employee2)


# ----7q---

# 7. OTT Platform Subscriptions
# ----7ans---
# friend1 = {"Netflix", "Prime", "Hotstar", "SonyLiv"}
# friend2 = {"Netflix", "Zee5", "Prime", "JioCinema"}

# # 1. Common subscriptions
# print("Common subscriptions:", friend1 & friend2)

# # 2. Unique to friend1
# print("Only friend1:", friend1 - friend2)

# # 3. All platforms
# print("All platforms:", friend1 | friend2)

# # 4. Platforms subscribed by only one friend
# print("Only one friend:", friend1 ^ friend2)

# ----8q---
# 8. Available and Sold Products
# ----8ans---
# available_products = {"Laptop", "Mouse", "Keyboard", "Monitor"}
# sold_products = {"Mouse", "Monitor"}

# # 1. Remaining available products
# print("Remaining products:", available_products - sold_products)

# # 2. Sold products
# print("Sold products:", sold_products)

# # 3. Add Printer
# available_products.add("Printer")
# print("After adding Printer:", available_products)

# # 4. Remove Keyboard
# available_products.remove("Keyboard")
# print("After removing Keyboard:", available_products)

# ----9q---
# 9. College Event Participation

# ----9ans---
# music_event = {"Anu", "David", "Riya", "Sam"}
# dance_event = {"Riya", "Sam", "Karthik", "John"}

# # 1. Both events
# print("Both events:", music_event & dance_event)

# # 2. Only music
# print("Only music:", music_event - dance_event)

# # 3. Only dance
# print("Only dance:", dance_event - music_event)

# # 4. All participants
# print("All participants:", music_event | dance_event)

# ----10q---
# 10. Website Visitors
# ----10ans---
# campaign_A = {"user101", "user102", "user103", "user104"}
# campaign_B = {"user103", "user104", "user105", "user106"}

# # 1. Common visitors
# print("Common visitors:", campaign_A & campaign_B)

# # 2. Unique to campaign A
# print("Only campaign A:", campaign_A - campaign_B)

# # 3. Total unique visitors
# print("Total visitors:", campaign_A | campaign_B)

# # 4. Visitors from only one campaign
# print("Only one campaign:", campaign_A ^ campaign_B)

# ---11q---
# Mini Challenge – Food Delivery App
# ----11ans---
# restaurant1 = {"Burger", "Pizza", "Fries", "Pasta"}
# restaurant2 = {"Pizza", "Sandwich", "Pasta", "Momos"}

# # 1. Common food items
# print("Common items:", restaurant1 & restaurant2)

# # 2. Exclusive items of restaurant1
# print("Restaurant 1 only:", restaurant1 - restaurant2)

# # 3. Exclusive items of restaurant2
# print("Restaurant 2 only:", restaurant2 - restaurant1)

# # 4. All available food items
# print("All food items:", restaurant1 | restaurant2)

# # 5. Items available in only one restaurant
# print("Only one restaurant:", restaurant1 ^ restaurant2)
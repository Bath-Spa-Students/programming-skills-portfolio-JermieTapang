#Q1:
#Write a python code that uses three variables x, y, and z with respective values 10,20 and 30. Add all the
##variables and then store the result in variable a. Print the value of a. 

x = 10
y = 20
z = 30

a = x+y+z

print (a)

## Q2:
# Write a python program that takes courses marks as input and then calculates average of all the
# courses. After calculating the average, calculate the percentage of a student using total marks. Assume
# the total of all the courses marks is 500 or take the total marks from the user as input. 

print("Enter the Marks to Obtained in 5 Subjects: ")
mark_one = int(input("Mark One : "))
mark_two = int(input("Mark Two :"))
mark_three = int(input("Mark Three :"))
mark_four = int(input("Mark Four :"))
mark_five = int(input("Mark Five :"))

final = mark_one+mark_two+mark_three+mark_four+mark_five
avg = final/5
perc = (final/500)*100

print(end="Average Marks = ")
print(avg)
print(end="Percentage Marks = ")
print(perc)



#Q3:
#Write a python program that takes an input 5 from user and then type cast those values to string, int
#and float in the separate variables. Print all the variables.

user_one = float(input("User One input :" ))
user_two = float(input("User two input: "))
user_three =float(input("User three input :"))
user_four =float(input("User Four input:"))
user_five =float(input("User Five input :"))


#Q4:
#Write a python program that stores an integer and string value to variables x and y. Print the type of
#variable x and y.

place = { 'country' : 'Canada', 'city' : 'Manila', 'town' : 'Tugatog'}
print (place.get("town"))
print (place.get("city"))

#Q5:
#Write a python program that stores fruit names in a list named fruits. Unpack the list into three
#variables x, y and z and then print the values of each variable.
fruit = { 'fruit' : 'Melon', 'round' : 'Orange', 'spiky' : 'Durian', 'favorite' : 'Lychee'}
print (fruit["spiky"])
print (fruit["round"])
print (fruit["fruit"])

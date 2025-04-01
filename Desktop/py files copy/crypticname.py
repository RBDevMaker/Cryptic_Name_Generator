'''
Cryptic name generator – You are creating a cryptic name generator 
and the first step in this process is to enter the user’s first name 
with a number after every character. Here are the steps to create this: 
a.  Ask user for their first name. 
b.  Create a cryptic_name variable with an empty string 
c.  Use a for loop to iterate through the user’s name  
d.  In each iteration of the loop, ask the user to input a number. This 
number should be appended after the character of the user’s first 
name and appended into the new cryptic_variable name. 
Example – If I input Kris as my first name, and I am asked four times 
for numbers: 10, 23, 55, 90. Then my  final cryptic name would be: 
K10r23i55s90.  Remember  you  can  access  the  ith  element  from  a 
string using string_name[i]. 
'''
name = input("give me a name: ")
cryptic_name = ''

for letter in name:
    number = "42"
    cryptic_name = cryptic_name + letter + number
    
print(cryptic_name)

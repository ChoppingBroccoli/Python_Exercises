#Receive input from the user
user_input = input("Enter a number:")

#Convert the user input from a str to a int
n = int(user_input)

#Initialize count to 0. count will store sum of all the numbers
count = 0

#Initialize iterations to 0. iterations will keep track of how many iterations it takes to complete the loop
iterations = 0

for x in range(1,n+1):
    #Store the value of count before it's changed
    pre_count = count
    print("Count is now", count, "and x is now", x)
    #Add the value of count to the value of x
    count = count + x
    print(pre_count,"plus", x, "is",count)
    #Increment iterations by one
    iterations = iterations + 1

print("You entered", user_input)
print("The sum of all numbers from 1 to", user_input, "is", count)
print("Loop completed in", iterations, "iterations")
"""
print(count)
"""

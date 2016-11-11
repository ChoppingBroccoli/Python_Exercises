user_integer = int(input("Enter a possitive number: "))
count = 1
x = int(user_integer)
while x >= 1 and user_integer <= 101:
    if x % 5 == 0:
        user_integer = user_integer + x
    count = count + 1

print("End loop")

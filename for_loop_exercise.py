count = 0

for x in range(1,102):
    if x % 2 == 0:
        print(x)
        count = count+x

print("The sum of all even numbers between 1 and 101 is",count)

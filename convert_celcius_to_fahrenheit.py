# This program converts Celsius to Fahrenheit
celsius=input("Enter degrees Censius: ")
fahrenheit=((float(celsius)*9)/5)+32
print(celsius,"degrees Censius is",fahrenheit,"degrees Fahrenheit")

if fahrenheit <= 32:
    print ("It is freezing")
elif fahrenheit > 32 and fahrenheit <= 50:
    print ("It is chilly")
elif fahrenheit > 50 and fahrenheit <= 90:
    print ("It is OK")
elif fahrenheit > 90:
    print ("It is hot")
else:
    print ("Something went wrong")

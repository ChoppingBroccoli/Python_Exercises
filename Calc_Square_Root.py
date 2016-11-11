user_response=float(input("Enter a number: "))
guess=user_response/2
accuracy=0.01
iteration=0
while abs(user_response-(guess**2)) > accuracy:
    print("Guessed square root is:",guess)
    guess=(guess+(user_response/guess))/2
    iteration=iteration+1
print("Original number is: ", user_response)
print("Square root of the number is: ", guess)
print("The loop ran",iteration,"times")

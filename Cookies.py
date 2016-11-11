user_response=int(input("How many cookies do you want? "))
cookies_eaten=0
while user_response > 0:
	user_response = user_response - 1
	cookies_eaten=cookies_eaten + 1
	print ("You have eaten",cookies_eaten, "cookies!")
print ("All out of cookies!")

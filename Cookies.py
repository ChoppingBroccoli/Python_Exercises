import random
cookies_available = random.randint(0,9) #Generate a random number of cookies
print("There are", cookies_available, "cookies available.") #Tell user how many cookies are available

cookies_wanted = int(input("How many would you like? ")) #Ask user how many cookies they want

while cookies_available > 0:
    if cookies_wanted > cookies_available:
        print("Sorry, we only have", cookies_available, "cookies available")
        break

    elif cookies_wanted == cookies_available:
        print("That's all the cookies")
        break
    elif cookies_wanted < cookies_available:
        cookies_available = cookies_available - cookies_wanted
        print("There are now",cookies_available,"cookies remaining.")



"""
######################################
########### Psuedo Code ##############
######################################
While there are more than 0 cookies in the jar, keep eating cookies.

If there are still cookies in the jar tell the user how many cookies there are then ask them if they 
want to continue eating. If yes, how many would they like to eat?

1) generate random number between 1 and 100
2) Tell user how many cookies there are
3) User inputs amount of cookies they want to eat
	a) if number is < cookies available, show user they ate the cookies
		i) show user how many cookies remain.
		ii) ask user if they want to eat more cookies.
		iii) ask user how many more cookies they want to eat.
	c) if number is = cookies avaible, tell user they ate all the cookies.
	d) if number is > cookies available, tell user we don't have that many cookies
This is a comment block
"""
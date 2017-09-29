'''
Takes an integer from the user then multiply all integers from 1 through n.
EXAMPLE: digit_fact(4) would be 4 * 3 * 2 * 1 and the product printed to the screen
'''

def digit_fact(n):
    #  Converts integer from user to a string. This is how we will iterate
    #  through the string later
    number_as_string = str(n)

    #  Initialize total_all_numbers to zero
    total_all_numbers = 0

    #  Iterate through number_as_string. Add each value at each index to total_all_numbers
    for x in number_as_string:
        total_all_numbers = total_all_numbers + int(x)

    #  Print the sum to the screen
    print(total_all_numbers)

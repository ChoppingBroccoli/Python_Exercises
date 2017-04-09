prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for each_fruit in prices:
    print (each_fruit)
    print "price: %s" % prices[each_fruit] #not sure why 'price' must be lower case but it does. Not sure what "%s" or "%" are needed.
    print "stock: %s" % stock[each_fruit]

def tuple_product(tup):
    return (lambda x, y: x*y, tup)
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)
product1 = tuple_product(tup1)
product2 = tuple_product(tup2)
print("The product of tup1 is:", product1)
print("The product of tup2 is:", product2)
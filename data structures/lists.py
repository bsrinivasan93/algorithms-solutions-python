fruits = ['apple','banana']
# for fruit in fruits:
#     # if 'apple' != fruit:
#         print(fruit)
# fruits.append('guava')
# print(fruits)
fruits.insert(1,'guavaa')
print(fruits)
del fruits[-1]
print(fruits)

squares = [x**2 for x in range(0,10)]
print(squares)
squares_two = squares[:2]
print(squares_two)
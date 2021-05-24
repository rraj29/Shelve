import shelve

# with shelve.open('Shelvetest') as fruit:
#     fruit['orange'] = 'a round, orange, citrus fruit'
#     fruit['apple'] = 'good for making cider'
#     fruit['lemon'] = 'a sour, yellow, citrus fruit'
#     fruit['grape'] = 'a small, sweet fruit growing in bunches'
#     fruit['lime'] = 'a sour, green citrus fruit'
#
#     print(fruit['lemon'])
#     print(fruit['apple'])
#
# print(fruit)

#both the above function and the below perform the same task.


fruit = shelve.open('Shelvetest')

# fruit['orange'] = 'a round, orange, citrus fruit'
# fruit['apple'] = 'good for making cider'
# fruit['lemon'] = 'a sour, yellow, citrus fruit'
# fruit['grape'] = 'a small, sweet fruit growing in bunches'
# fruit['lime'] = 'a sour, green citrus fruit'

# print(fruit['lemon'])
# print(fruit['apple'])
#
# fruit['lime'] = 'great with tequila'
# for snack in fruit:
#     print(snack +": "+fruit[snack])

# while True:
#     fruit_key = input("Please enter a fruit: ")
#     if fruit_key=="quit":
#         break
#     if fruit_key in fruit:
#         description = fruit[fruit_key]
#         print(description)
#     # description = fruit.get(fruit_key, "we don't have a {}".format(fruit_key))
#     # print(description)
#     else:
#         print("we don't have a {}".format(fruit_key))

ordered_keys = list(fruit.keys())       #we are sorting the keys in order.
ordered_keys.sort()

for key in ordered_keys:
    print(key + " - "+fruit[key])
print('-'*85)
for v in fruit.values():
    print(v)
print('-'*85)
print(fruit.values())
print('-'*85)
for v in fruit.items():
    print(v)
print('-'*85)
print(fruit.items())
print('-'*85)
fruit.close()

print(fruit)
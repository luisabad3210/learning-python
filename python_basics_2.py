# LIST 

friends = ['kevin', 'karen', 'jim', 'oscar', 'toby']

# print(friends)
# print (friends[0])
# print (friends[1])
# print (friends[2])

# print(friends[1:4])     # ['karen', 'jim', 'oscar']
friends[1] = 'mike'
# print(friends)

lucky_numbers = [1, 2, 3]
friends.extend(lucky_numbers)

friends.append('creed')

# print(friends)

friends.insert(1, 'kelly')
friends.remove('jim')
friends.pop() # removes the last element
# print(friends) 


# TUPLES

# tuples cant be changed or modified

coordinates = (4, 5)
# coordinates[1] = 10  # will return error
print(coordinates)


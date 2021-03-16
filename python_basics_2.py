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
# print(coordinates)



# FUNCTIONS

def say_hi():
    print('hello user')

# say_hi()

def cube(num):
    return num * num * num

# print(cube(3))


is_male = False
is_tall = False

# if is_male or is_tall:
#     print('you are a male or tall or both')
# elif is_male and not(is_tall):
#     print('you are a short male')
# elif not(is_male) and is_tall:
#     print('you are a male but is tall')
# else:
#     print('you are not a male nor tall')

def biggest_num(num1, num2, num3):
    if (num1 >= num2 and num1 >= num3):
        return num1
    elif (num2 >= num1 and num2 >= num3):
        return num2
    else:
        return num3

print(biggest_num(9, 4, 5))
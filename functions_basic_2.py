# def countdown(num):
#     list = []
#     for i in range (num, 0-1, -1):
#         list.append(i)
#     return list
# print(countdown(5))

# def print_and_return(list):
#     print(list[0])
#     return list[1]
# print(print_and_return([1,2]))

# def first_plus_length(list):
#     sum = list[0]
#     sum += len(list)
#     return sum
# print(first_plus_length([1,2,3,4,5]))

# def val_greater_than_second(list):

#     if len(list) < 2:
#         return False
#     new_list = []
#     count = 0
#     for i in range( len(list) ):
#         if( list[i] > list[1] ):
#             new_list.append(list[i])
#             count+=1
#     print(count)
#     return new_list
# print( val_greater_than_second([5,2,3,2,1,4]) )
# print( val_greater_than_second([3]) )

def this_that(size, value):
    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list
print( this_that(4,7) )
print( this_that(6,2) )


def insertion_sort(ul):
    for i in range(1, len(ul) ):
        current_index = i
        while( ul[current_index] < ul[current_index-1] and current_index > 0):
            ul[current_index], ul[current_index-1] = ul[current_index-1], ul[current_index]
            current_index-=1
        print(ul)

    return ul

# print( insertion_sort([8,7,6,5,4,3,2,1]) )
# print( insertion_sort([1,2,3,4,5,6,7,8]) )
print( insertion_sort([7,4,6,8,3,5,6,3]) )
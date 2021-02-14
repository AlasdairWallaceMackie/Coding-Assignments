def selection_sort(ul):
    for i in range( len(ul)-1 ):
        min_value_index = i
        for j in range(i+1, len(ul)):
            if( ul[j] < ul[min_value_index] ):
                min_value_index = j
        ul[i], ul[min_value_index] = ul[min_value_index], ul[i]
        print(ul)
    return ul

# selection_sort([8,7,6,5,4,3,2,1])
print( selection_sort([3,5,7,3,4,8,9,3,2,1]) )

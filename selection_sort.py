def selection_sort(ul):
    min_value = ul[0]
    
    for i in range( len(ul) ):
        flip_index = i
        for j in range(i, len(ul) ):
            if ul[j] < ul[i]:
                min_value = ul[j]
                flip_index = j
        if flip_index > i:
            ul[i], ul[flip_index] = ul[flip_index], ul[i]
        print(ul)

selection_sort([8,7,6,5,4,3,2,1])



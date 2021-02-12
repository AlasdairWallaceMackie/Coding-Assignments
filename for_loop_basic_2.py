def biggie(list):
    for i in range( len(list) ):
        if list[i]>0:
            list[i]="big"
    return list
print(biggie([-1,3,5,-5]))

def count_positives(list):
    count = 0
    for i in range( len(list) ):
        if list[i] > 0:
            count+=1
    list[len(list)-1] = count
    return list
print( count_positives([-1,1,1,1]) )

def sum_total(list):
    sum = 0
    for i in range( len(list) ):
        sum += list[i]
    return sum
print( sum_total([1,2,3,4]) )

def average(list):
    sum = sum_total(list)
    return sum / len(list)
print( average([1,2,3,4]) )

def length(list):
    return len(list)
print( length([37,2,1,-9]))

def minimum(list):
    if len(list)==0:
        return False
    min_value = list[0]
    for i in range( len(list) ):
        if list[i] < min_value:
            min_value = list[i]
    return min_value
print(minimum([3,7,6,-10]))

def maximum(list):
    if len(list)==0:
        return False
    max_value = list[0]
    for i in range( len(list) ):
        if list[i] > max_value:
            max_value = list[i]
    return max_value
print(maximum([3,7,6,-10]))

def ultimate_analysis(list):
    analysis = {
        "avg":         average(list),
        "total_sum":   sum_total(list),
        "max_number":  maximum(list),
        "min_number":  minimum(list)
    }
    return analysis
print( ultimate_analysis([37,2,1,-9]) )

def reverse_list(list):
    hold = None
    endpoint_index = len(list)-1
    for i in range( len(list) ):
        if i==endpoint_index or i>endpoint_index:
            return list
        hold = list[i]
        list[i] = list[endpoint_index]
        list[endpoint_index] = hold
        endpoint_index-=1
print( reverse_list([1,2,3,4,5,6,7]) )




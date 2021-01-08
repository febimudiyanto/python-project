def insertion_sort(x):
    array = x
    for i in range(len(array)-1):
        idx_min = i

        j=i+1
        while j<len(array):
            if (array[j] < array[idx_min]):
                idx_min = j
            j+=1


        if(idx_min != i):
            array[idx_min],array[i]=array[i],array[idx_min]
    return array


print(insertion_sort([12,3,43,12,11,0,5]))


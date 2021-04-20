#the bubble sort
#dari kecil ke terbesar
def bubble_sort(list):
    '''
    input: number list
    return: a sorted list
    '''
    swap = True
    while (swap == True):
        swap = False
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                swap = True
                list[i],list[i+1]= list[i+1],list[i]
    print(list)

bubble_sort([1, 3, 2, 3, 3, 4, 2, 10, 8, 7])
#output
#[1, 2, 2, 3, 3, 3, 4, 7, 8, 10]

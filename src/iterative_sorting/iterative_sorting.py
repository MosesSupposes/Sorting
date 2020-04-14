# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
             
        # TO-DO: swap
        y = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = y

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    if (len(arr) == 0): 
        return arr
    
    copy = arr.copy()

    for i in range(0, len(copy) - 1):
        if  copy[i] >= copy[i + 1]:
            #swap
            cur = copy[i]
            copy[i] = copy[i + 1]
            copy[i + 1] = cur
            return bubble_sort(copy)
    
    return copy


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


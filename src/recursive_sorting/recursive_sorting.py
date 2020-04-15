# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    #create a new array with the length of the combined lengths of both arrays.
    merged_arr = [0] * elements
    # TO-DO
    j = 0
    k = 0
    for i in range(0, len(merged_arr)):
        # if we exhausted through the first list
        if j == len(arrA):
            # add the rest of arrB to the merged_arr. Note that arrB is already sorted
            while k < len(arrB):
                merged_arr[i] = arrB[k]
                i += 1
                k += 1
            break
        # if we exhaust through the second list
        elif k == len(arrB):
            # add the rest of arrA to the merged_arr. Note that arrA is already sorted.
            while j < len(arrA):
                merged_arr[i] = arrA[j]
                i += 1
                j += 1
            break
            
        if j < len(arrA) and k < len(arrB):
            if arrA[j] < arrB[k]:
                merged_arr[i] = arrA[j]
                j += 1
            else:
                merged_arr[i] = arrB[k] 
                k += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    
    half = len(arr) // 2
    sorted_first_half = merge_sort(arr[0 : half]) 
    sorted_second_half = merge_sort(arr[half : len(arr)])

    return merge(sorted_first_half, sorted_second_half)


    # return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

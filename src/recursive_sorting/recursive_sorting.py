# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    #create a new array with the length of the combined lengths of both arrays.
    merged_arr = [0] * elements
    # TO-DO
    j = 0
    k = 0

    for i in range(0, len(merged_arr)):
        # if j == len(arrA) - 1:
        #     merged_arr.extend(arrB)
        #     break
        # elif k == len(arrB) - 1:
        #     merged_arr.extend(arrA) 
        #     break
            
        if j < len(arrA) and k < len(arrB):
            print("inside")
            if arrA[j] < arrB[k]:
                print("arrA[j] < arrB[k]", arrA[j])
                merged_arr[i] = arrA[j]
                print("i:", i, "merged_arr[i]:", merged_arr[i])
                j += 1

            else:
                print("arrB[k] < arrA[j]", arrB[k])
                merged_arr[i] = arrB[k] 
                print("i:", i, "merged_arr[i]:", merged_arr[i])
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

#myself
def solution(arr):
    if len(arr) == 1:
        return [-1]

    min = arr[0]
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]
    
    arr.remove(min)
    return arr

#-----------------------------------------------
#with other solution1 - single line
def solution_single(arr):
    if len(arr) == 1:
        return -1
    else:
        return [a for a in arr if a > min(arr) ]

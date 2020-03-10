# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. 
# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3
def centered_average(arr):
    #Set and sort array
    arr.sort()
    #remove smallest and largest number
    arr.pop()
    arr.pop(0)
    #return sum // length
    print(sum(arr) // len(arr))

centered_average([1, 2, 3, 4, 100])
centered_average([1, 1, 5, 5, 10, 8, 7]) 
centered_average([-10, -4, -2, -4, -2, 0]) 
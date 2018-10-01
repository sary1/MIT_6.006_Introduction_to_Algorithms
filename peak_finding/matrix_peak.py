lst = [
    [3, 5, 9, 122],
    [15, 8, 12, 23],
    [7, 6, 34, 24]
]

lst2 = [
    [3, 5, 9],
    [15, 8, 12],
    [7, 6, 4]
]

lst3 = [
    [3, 5, 9],
    [15, 8, 2],
    [7, 6, 4]
]

lst4 = [
    [3, 5],
    [15, 18],
    [7, 6]
]

lst5 = [
    [3],
    [15],
    [7]
]


# a function that returns the max item of a column and its index
def find_max(arr, mid):

    max_index = 0
    max_item = 0

    for i in range(len(arr)):
        if max_item < arr[i][mid]:
            max_item = arr[i][mid]
            max_index = i

    return max_item, max_index


# a function that returns a peak item that is greater than its neighbors
# top, bottom, right and left if they exist
# The worst case time complexity of this method would be O(nlog m).
# while having (n) rows and (m) columns
def find_peak(arr, rows, cols, mid):

    max_item, max_index = find_max(arr, mid)

    # in case of having only two columns, compare the max item in mid with
    # its only neighbor left or right
    if (cols == 2):
        return max(arr[max_index][0], arr[max_index][1])

    # check the max when the recursive function reaches the border
    if mid == 0 or mid == (cols - 1):
        return max_item

    # check if the max item in mid is the max of the side neighbors as well
    if (max_item >= arr[max_index][mid + 1] and
            max_item >= arr[max_index][mid - 1]):
        return max_item

    # if the right neighbor is greater then there must be a peak on the right
    elif (mid > 0 and arr[max_index][mid] < arr[max_index][mid + 1]):
        if (mid == (mid + mid // 2)):
            mid += 1
            return find_peak(arr, rows, cols, mid)
        return find_peak(arr, rows, cols, mid + mid // 2)

    # if the left neighbor is greater then there must be a peak on the left
    else:
        if (mid == (mid - mid // 2)):
            mid -= 1
            return find_peak(arr, rows, cols, mid)
        return find_peak(arr, rows, cols, mid - mid // 2)


def peak(arr, rows, cols):
    return find_peak(arr, rows, cols, cols // 2)


print("The first peak of the list 1 is: " + str(peak(lst, 3, 4)))
print("The first peak of the list 1 is: " + str(peak(lst2, 3, 3)))
print("The first peak of the list 1 is: " + str(peak(lst3, 3, 3)))
print("The first peak of the list 1 is: " + str(peak(lst4, 3, 2)))
print("The first peak of the list 1 is: " + str(peak(lst5, 3, 1)))

lst = [22, 35, 62, 84, 12, 25, 39, 99, 152, 124]
lst2 = [1, 2, 5, 922, 15]
lst3 = [11, 2]
lst4 = [5]
lst5 = []

# A function that makes a linear search
# The worst case time complexity of this method would be O(n).


def peak(arr):
    ''' A function that returns a peak in a linear search '''

    # if the array has one element return it
    if len(arr) == 1:
        return arr[0]

    # return the item that is greater that both its neighbors if the
    # exist
    for i in range(len(arr)):

        # if the very left item is greater that the right neighbor then
        # it is a peak
        if i == 0:
            if arr[i] >= arr[i + 1]:
                return arr[i]

        # if the very right item is greater that the left neighbor then
        # it is a peak
        elif i == len(arr) - 1:
            if arr[i] >= arr[i - 1]:
                return arr[i]

        # find a peak that is greater than both its neighbors
        else:
            if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
                return arr[i]


print("The first peak of the list 1 is: " + str(peak(lst)))
print("The first peak of the list 2 is: " + str(peak(lst2)))
print("The first peak of the list 3 is: " + str(peak(lst3)))
print("The first peak of the list 4 is: " + str(peak(lst4)))
print("The first peak of the list 5 is: " + str(peak(lst5)))

lst = [22, 35, 62, 84, 12, 25, 39, 99, 152, 124]
lst2 = [1, 2, 5, 922, 15]
lst3 = [11, 2]
lst4 = [5]
lst5 = []

# A function that uses a Divide and conquer method to find a peak
# The worst case time complexity of this method would be O(log n).


def find_peak(arr, low, high, n):

    # calculate index of mid item
    mid = int(low + (high - low) / 2)

    if len(arr) == 0:
        return None

    # the mid item is a peak when it is greater than its neighbors
    # (if they exist)
    if ((mid == 0 or arr[mid] >= arr[mid - 1]) and
            (mid == n - 1 or arr[mid] >= arr[mid + 1])):
        return arr[mid]

    # if the mid item is less than its left neighbor then there
    # must be a peak on the left
    elif (mid > 0 and arr[mid] < arr[mid - 1]):
        return find_peak(arr, low, mid - 1, n)

    # if the mid item is less than its right neighbor then there
    # must be a peak on the right
    else:
        return find_peak(arr, mid + 1, high, n)


def peak(arr, n):
    return find_peak(arr, 0, n - 1, n)


print("The first peak of the list 1 is: " + str(peak(lst, len(lst))))
print("The first peak of the list 2 is: " + str(peak(lst2, len(lst2))))
print("The first peak of the list 3 is: " + str(peak(lst3, len(lst3))))
print("The first peak of the list 4 is: " + str(peak(lst4, len(lst4))))
print("The first peak of the list 5 is: " + str(peak(lst5, len(lst5))))

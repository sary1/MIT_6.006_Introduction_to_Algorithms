lst = [22, 35, 62, 84, 12, 25, 39, 99, 152, 124]


# A function that makes a linear search 
# The worst case time complexity of this method would be O(n).
def peak(lst):
    
    for i in range(1, len(lst) - 1):
        if(lst[i] >= lst[i - 1] and lst[i] >= lst[i + 1]):
            return lst[i]
        
print("The first peak of the list is: " + str(peak(lst)))

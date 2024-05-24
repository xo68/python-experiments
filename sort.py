# Return the index of the Smallest element
def findSmallest(arr):
    smallest = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            index = i
    return index


# Selection sort
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        index = findSmallest(arr)
        newArr.append(arr.pop(index))
    return newArr


# Quick sort
def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


if __name__ == "__main__":
    arr = [5, 3, 4, 1, 2, 0]
    print(f"Array: {arr}")
    print(f"Selection Sort: {selectionSort(arr[:])}")
    print(f"Quick Sort: {quickSort(arr[:])}")

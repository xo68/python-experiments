# Find the smallest element
def find_smallest(arr):
    smallest = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            index = i
    return index


# Selection Sort
def selection_sort(arr):
    new_arr = []
    for _ in range(len(arr)):
        index = find_smallest(arr)
        new_arr.append(arr.pop(index))
    return new_arr


# Quick sort
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    uarr = [5, 3, 4, 1, 2, 0]
    print(f"Array: {uarr}")
    print(f"Selection Sort: {selection_sort(uarr[:])}")
    print(f"Quick Sort: {quick_sort(uarr[:])}")

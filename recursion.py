# Sum of all elements in a array
def array_sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr.pop()
    return arr.pop() + array_sum(arr)


if __name__ == "__main__":
    uarr = [5, 3, 4, 1, 2, 0]
    print(f"Sum array: {array_sum(uarr)}")

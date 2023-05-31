# Python3 implementation of QuickSort


# Function to find the partition position
def partition(arr, low, high):
    pivot = arr[high]
    i = low -1
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i+1],arr[high]) = (arr[high], arr[i+1])
    return i+1
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot -1)
        quick_sort(arr, pivot + 1, high) 
# Driver code
if __name__ == '__main__':
    array = [10, 7, 8, 9, 1, 5]
    quick_sort(array, 0, len(array) - 1)

    print(f'Sorted array: {array}')

    # This code is contributed by Adnan Aliakbar

def min_max_sort(arr, left, right):
    while left < right:
        min_index = left
        max_index = left

        for i in range(left, right + 1):
            if arr[i] < arr[min_index]:
                min_index = i
            if arr[i] > arr[max_index]:
                max_index = i

        swap(arr, left, min_index)

        if max_index == left:
            max_index = min_index

        swap(arr, right, max_index)

        left += 1
        right -= 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def main():
    n = int(input("Enter number of elements: "))
    arr = []

    print("Enter elements:")
    for i in range(n):
        arr.append(int(input()))

    min_max_sort(arr, 0, n - 1)

    print("Sorted Array:", arr)

if __name__ == "__main__":
    main()
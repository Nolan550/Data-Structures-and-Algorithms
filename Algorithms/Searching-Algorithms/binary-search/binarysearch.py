def binary_search(arr, target):
  
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    n = int(input("Enter the number of elements: "))

    arr = []
    print(f"Enter {n} elements:")
    for _ in range(n):
        arr.append(int(input()))

    # Binary search requires a sorted array
    arr.sort()
    print("Sorted array:", arr)

    target = int(input("Enter the target element: "))

    result = binary_search(arr, target)

    if result == -1:
        print("Element not found in the array.")
    else:
        print(f"Element {target} found at index {result}.")


if __name__ == "__main__":
    main()

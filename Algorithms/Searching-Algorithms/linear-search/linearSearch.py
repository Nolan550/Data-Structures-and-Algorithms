def linear_search(arr, target):
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def main():
    n = int(input("Enter the number of elements: "))

    arr = []
    print(f"Enter {n} elements:")
    for _ in range(n):
        arr.append(int(input()))

    target = int(input("Enter the target element: "))

    result = linear_search(arr, target)

    if result == -1:
        print("Element not found in the array.")
    else:
        print(f"Element {target} found at index {result}.")


if __name__ == "__main__":
    main()

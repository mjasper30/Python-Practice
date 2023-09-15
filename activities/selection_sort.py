def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i

        # Find the index of the minimum element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # Print the current state of the array
        print(f"Iteration {i + 1}: {arr}")


# Example usage:
if __name__ == "__main__":
    arr = [4, 1, 13, 8, 9, 6, 5, 7, 11, 3, 12, 2, 14, 15, 10]
    print("Original Array:", arr)
    selection_sort(arr)
    print("Sorted Array:", arr)

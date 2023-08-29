def two_sum(nums, target):
    num_to_index = {}  # A hash map to store the numbers and their indices

    for index, num in enumerate(nums):
        complement = target - num

        if complement in num_to_index:
            return [num_to_index[complement], index]

        num_to_index[num] = index

    return None  # If no solution is found


# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
if result:
    print("Indices of the two numbers:", result)
else:
    print("No solution found.")

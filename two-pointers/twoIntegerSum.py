def twoSum(numbers, target):

    # Return 1-indices should not start with 0

    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target and numbers[left] < numbers[right]:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
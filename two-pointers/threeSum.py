def threeSum(nums):
    # Brute force approach


    nums.sort()
    final_arr = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0 and i != j != k:
                    sorted_arr = [nums[i], nums[j], nums[k]]
                    if sorted_arr not in final_arr:
                        final_arr.append(sorted_arr)
            k += 1
        j += 1
    i += 1

    return final_arr
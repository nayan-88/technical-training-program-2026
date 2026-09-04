#find maximum number of consecutive 1s in a binary array
#logic iterate through the array keeping track of current consecutive 1s and maximum seen far
def find_max_consecutive_ones(nums):
    current_count = 0
    max_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count


nums = [1, 1, 0, 1, 1, 1]
print(find_max_consecutive_ones(nums))  # 3
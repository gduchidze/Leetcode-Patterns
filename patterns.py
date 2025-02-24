# Prefix Sum Pattern

# Prefix Sum Array-ის შექმნა
def prefix_sum(arr):
    n = len(arr)
    prefix_sum_arr = [0] * (n + 1)  # ერთი ელემენტით უფრო მეტი, რადგან პირველ ელემენტზე ჯამი 0 იქნება

    # Prefix sum-ის ამოხსნის პროცესი
    for i in range(1, n + 1):
        prefix_sum_arr[i] = prefix_sum_arr[i - 1] + arr[i - 1]

    return prefix_sum_arr

# სუბარეის ჯამის გამოთვლა
def range_sum(prefix_sum_arr, left, right):
    # ჯამი [left, right] ინტერვალისათვის
    return prefix_sum_arr[right + 1] - prefix_sum_arr[left]

# მაგალითი
arr = [1, 2, 3, 4, 5]
prefix_sum_arr = prefix_sum(arr)

# კითხვის პასუხი: ელემენტების ჯამი ინდექსების 1 და 3 შორის (2 + 3 + 4)
result = range_sum(prefix_sum_arr, 1, 3)

print(f"Prefix Sum Array: {prefix_sum_arr}")
print(f"Range sum from index 1 to 3: {result}")



# ამოცანა 1: Range Sum Query - Immutable

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


#O(1)

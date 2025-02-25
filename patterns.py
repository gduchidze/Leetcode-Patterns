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
        # Step 1 : ვქმნით ახალ მასივს სიგრძით Array Len + 1 რადგან 0 იდან დაიწყოს 
        self.prefix_sum = [0] * (len(nums) + 1)
        # Step 2 : ვავსებთ ახალ მასივს წინასწარ დაგროვილი ჯამთ და ვინახავთ უკეთესი TC სთვის
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# რატომ right + 1, მაგრამ left უცვლელი?
# 📌 მთავარი იდეა:

# prefix_sum[i] → ინახავს პირველი i ელემენტის ჯამს
# prefix_sum[right + 1] უნდა ავიღოთ, რადგან ის nums[right]-საც მოიცავს.
# მაგალითად, right = 5 და prefix_sum[5] მხოლოდ nums[0]-დან nums[4]-მდე ჯამს გვაძლევს,
# ამიტომ უნდა ავიღოთ prefix_sum[6], რომელიც nums[5]-საც შეიცავს.

# left უცვლელია, რადგან prefix_sum[left] უკვე არის left-1 ინდექსამდე ჯამის ბოლო მნიშვნელობა.


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


#O(1)

#Pattern 2 Sliding Window


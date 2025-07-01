from typing import List

# Running time: O(n * m), where n is the number of elements in nums and m is the minimum element in nums.
def findGCD(nums: List[int]) -> int:
    min_num = min(nums)
    for i in range(min_num, 0, -1):
        if all(num % i == 0 for num in nums):
            return i
    return 1

# Running time: O(n * log(m)), where n is the number of elements in nums and m is the maximum element in nums.
def findGCD_Euclidean(nums: List[int]) -> int:
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    
    result = nums[0]
    for num in nums[1:]:
        result = gcd(result, num)
    return result

def findLCM(nums: List[int]) -> int:
    def lcm(a: int, b: int) -> int:
        return a * b // findGCD([a, b])
    result = 1
    for num in nums:
        result = lcm(result, num)
    return result

import time
arr = [4, 6, 8, 9, 5, 20, 10, 12, 15, 18, 24, 30, 36, 40, 48, 60, 72, 80, 90, 100]
start_time = time.perf_counter()
print("GCD:", findGCD(arr)) 
end_time = time.perf_counter()
print(f"Time taken for GCD: {end_time - start_time:.6f} seconds")

start_time = time.perf_counter()
print("GCD (Euclidean):", findGCD_Euclidean(arr))
end_time = time.perf_counter()
print(f"Time taken for GCD (Euclidean): {end_time - start_time:.6f} seconds")
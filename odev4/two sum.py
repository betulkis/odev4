from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[nums[i]] = i
        return [-1, -1]

def run_test_case(nums: List[int], target: int):
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(f"nums: {nums}, target: {target} => Result: {result}")

if __name__ == "__main__":
    run_test_case([2, 7, 11, 15], 9)
    run_test_case([3, 2, 4], 6)
    run_test_case([3, 3], 6)





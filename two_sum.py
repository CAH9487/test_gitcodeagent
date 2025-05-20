from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

def test_two_sum():
    s = Solution()
    assert s.twoSum([2,7,11,15], 9) == [0,1] or s.twoSum([2,7,11,15], 9) == [1,0]
    assert s.twoSum([3,2,4], 6) == [1,2] or s.twoSum([3,2,4], 6) == [2,1]
    assert s.twoSum([3,3], 6) == [0,1] or s.twoSum([3,3], 6) == [1,0]
    print('All tests passed!')

if __name__ == "__main__":
    test_two_sum()

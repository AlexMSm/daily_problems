from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        array_length = len(nums)
        ans = [None] * 2 * array_length
        i = 0
        while i < 2 ** array_length:
            if i >= array_length:
                second_int = i - array_length
                ans[i] = nums[second_int]
            else:
                ans[i] = nums[i]
            i+=1
        return ans
    
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)  # Extend the list with itself
        return nums

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
    
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2
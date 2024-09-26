from typing import List
class Solution:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
          my_map = dict()
          for i in range (len(nums)):
               comp = target - nums[i]
               if comp in my_map:
                    return [my_map.get(comp), i]
               else:
                    my_map[nums[i]] = i

s = Solution()
print(s.twoSum([2,7,4,3], 9))
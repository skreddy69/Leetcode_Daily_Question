from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Convert all numbers to strings
        nums = list(map(str, nums))
        
        # Custom comparator to sort the numbers in the required order
        def compare(a, b):
            # Compare the concatenated results
            if a + b > b + a:
                return -1  # a should come before b
            elif a + b < b + a:
                return 1   # b should come before a
            else:
                return 0   # they are equal
        
        # Sort the list using the custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Join the sorted numbers into a single string
        largest_num = ''.join(nums)
        
        # Edge case: if the result starts with '0', return '0'
        if largest_num[0] == '0':
            return '0'
        
        return largest_num
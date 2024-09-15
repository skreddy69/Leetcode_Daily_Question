class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Mapping vowels to bit positions
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        
        # Initial mask is 0, meaning all vowels have even occurrences
        mask = 0
        
        # Dictionary to store the first occurrence of each mask
        first_occurrence = {0: -1}
        
        # Variable to keep track of the maximum length
        max_len = 0
        
        # Iterate through the string
        for i, char in enumerate(s):
            # If the character is a vowel, toggle the respective bit in the mask
            if char in vowel_to_bit:
                mask ^= (1 << vowel_to_bit[char])
            
            # Check if this mask has been seen before
            if mask in first_occurrence:
                # Update the maximum length of the substring
                max_len = max(max_len, i - first_occurrence[mask])
            else:
                # Store the first occurrence of this mask
                first_occurrence[mask] = i
        
        return max_len
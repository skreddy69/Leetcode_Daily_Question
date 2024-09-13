class Solution:
    def xorQueries(self, arr, queries):
        # Step 1: Compute the prefix XOR array
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] ^ arr[i]
        
        # Step 2: Answer each query using the prefix XOR array
        result = []
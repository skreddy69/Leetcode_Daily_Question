class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        # Memoization dictionary
        memo = {}

        # Helper function for recursive computation
        def compute(expression):
            # If the result for this expression is already computed, return it
            if expression in memo:
                return memo[expression]

            results = []
            # Traverse the expression
            for i, char in enumerate(expression):
                if char in "+-*":
                    # Recursively solve left and right parts
                    left_results = compute(expression[:i])
                    right_results = compute(expression[i+1:])
                    
                    # Combine results from left and right based on the operator
                    for left in left_results:
                        for right in right_results:
                            if char == '+':
                                results.append(left + right)
                            elif char == '-':
                                results.append(left - right)
                            elif char == '*':
                                results.append(left * right)

            # If no operator was found, it means the expression is a single number
            if not results:
                results.append(int(expression))

            # Memoize the result for this expression
            memo[expression] = results
            return results

        # Call the helper function for the full expression
        return compute(expression)
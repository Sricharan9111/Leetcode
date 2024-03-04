class Solution:
    def productExceptSelf(self,nums:List[int])->List[int]:
        n = len(nums)
        # Initialize left and right arrays
        left_products = [1] * n
        right_products = [1] * n
        # Calculate left products
        left_product = 1
        for i in range(1, n):
            left_product *= nums[i - 1]
            left_products[i] = left_product
    
    # Calculate right products
        right_product = 1
        for i in range(n - 2, -1, -1):
            right_product *= nums[i + 1]
            right_products[i] = right_product
    
    # Calculate the final answer
        result = [1]*n
        for i in range(n):
            result[i] = left_products[i]*right_products[i]
    
        return result
hello

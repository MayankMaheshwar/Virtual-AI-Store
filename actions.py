class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def dfs(index, current):
            # At each step, count the current subset if it is non-empty
            if current:
                self.res += 1
            
            # Explore further elements to add to the current subset
            for i in range(index, len(nums)):
                # Check if we can add nums[i] to the current subset
                if not current or all(abs(nums[i] - x) != k for x in current):
                    dfs(i + 1, current + [nums[i]])

        self.res = 0
        nums.sort()  # Sorting the numbers to make the problem easier to handle
        dfs(0, [])
        return self.res

# Example usage:
# sol = Solution()
# print(sol.beautifulSubsets([2, 4, 6], 2))  # Output: 4
# print(sol.beautifulSubsets([1], 1))  # Output: 1

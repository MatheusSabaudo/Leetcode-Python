class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # Initialize the first and last positions as -1
        # (-1 means the target has not been found yet)
        first = -1
        last = -1

        # Loop through the array with index and value
        for i, v in enumerate(nums):
            
            # Check if the current value matches the target
            if v == target:
                
                # If this is the first time we find the target,
                # store the index as the first occurrence
                if first == -1:
                    first = i
                
                # Always update last to the current index
                # so it ends up being the last occurrence
                last = i

        # Return the first and last positions of the target
        # If the target was not found, both remain -1
        return [first, last]
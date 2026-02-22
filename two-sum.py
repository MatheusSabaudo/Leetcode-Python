class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Dictionary to store numbers we have already seen
        # Format: {number : index}
        hash_map = {}
        
        # Loop through the list with both index and value
        for i, v in enumerate(nums):
            
            # Calculate the number needed to reach the target
            complement = target - v
            
            # Check if the complement already exists in the hash map
            if complement in hash_map:
                
                # If found, we have the solution:
                # return index of the complement and current index
                return [hash_map[complement], i]
            
            else:
                # Otherwise, store the current number with its index
                # so it can be used for future complements
                hash_map[v] = i
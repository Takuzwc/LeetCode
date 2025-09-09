# Sliding window is another common approach to solving problems related to arrays. 
# A sliding window is actually implemented using two pointers! Before we start, 
# we need to talk about the concept of a subarray.

# Subarrays
# Given an array, a subarray is a contiguous section of the array. 
# All the elements must be adjacent to each other in the original array 
# and in their original order. For example, with the array [1, 2, 3, 4], 
# Given an array, a subarray is a contiguous section of the array. the s
# ubarrays (grouped by length) are:

# Subarrays with length 1: [1], [2], [3], [4]
# Subarrays with length 2: [1, 2], [2, 3], [3, 4]
# Subarrays with length 3: [1, 2, 3], [2, 3, 4]
# Subarrays with length 4: [1, 2, 3, 4]

# A subarray can be defined by two indices, the start and end. For example, 
# with [1, 2, 3, 4], the subarray [2, 3] has a starting index of 1 and an ending
#  index of 2. Let's call the starting index the left bound and the ending index
#  the right bound. Another name for subarray in this context is "window".
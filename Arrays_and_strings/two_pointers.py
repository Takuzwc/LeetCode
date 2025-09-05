#Two pointers is an extremely common technique used to 
# solve array and string problems. It involves having two
#  integer variables that both move along an iterable. 
# In this article, we are focusing on arrays and strings. 
# This means we will have two integers, usually named something 
# like i and j, or left and right which each represent an index of the array or string.
#There are several ways to implement two pointers. To start, let's look at the following method:


#Start the pointers at the edges of the input. Move them towards each other until they meet.
#function fn(arr):
    # left = 0
    # right = arr.length - 1

    # while left < right:
    #     Do some logic here depending on the problem
    #     Do some more logic here to decide on one of the following:
    #         1. left++
    #         2. right--
    #         3. Both left++ and right--

# Example 1: Given a string s, return true if it is a palindrome, false otherwise.

# A string is a palindrome if it reads the 
# same forward as backward. That means, after reversing it, 
# it is still the same string. For example: "abcdcba", or "racecar".
# After reversing a string, the first character
# becomes the last character. If a string is the same after being 
# reversed, that means the first character is the same as the last character, 
# the second character is the same as the second last character, and so on. 
# We can use the two pointers technique here to check that all corresponding 
# characters are equal. To start, we check the first and last characters 
# using two separate pointers. To check the next pair of characters, we just need 
# to move our pointers toward each other one position. We continue until the 
# pointers meet each other or we find a mismatch.

def check_if_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

#Example 2: Given a sorted array of unique integers and a target integer, return true 
# if there exists a pair of numbers that sum to target, false otherwise. 
# This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

#For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true 
# because 4 + 9 = 13.

#Note: a similar version of this problem can be found on LeetCode: 167.
#  Two Sum II - Input Array Is Sorted

def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        # curr is the current sum
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1
    
    return False

#Another way to use two pointers

#This method where we start the pointers at the first and last indices and move them 
# towards each other is only one way to implement two pointers. Algorithms are 
# beautiful because of how abstract they are - "two pointers" is just an idea, and it can be implemented in many different ways. Let's look at another method and some new examples. The following method is applicable when the problem has two iterables in the input, for example, two arrays.
#Move along both inputs simultaneously until all elements have been checked.

#Here's some pseudocode illustrating the concept:

# function fn(arr1, arr2):
#     i = j = 0
#     while i < arr1.length AND j < arr2.length:
#         Do some logic here depending on the problem
#         Do some more logic here to decide on one of the following:
#             1. i++
#             2. j++
#             3. Both i++ and j++

#     // Step 4: make sure both iterables are exhausted
#     // Note that only one of these loops would run
#     while i < arr1.length:
#         Do some logic here depending on the problem
#         i++

#     while j < arr2.length:
#         Do some logic here depending on the problem
#         j++

#Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that 
# combines both of them and is also sorted.

def combine(arr1, arr2):
    # ans is the answer
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
    
    return ans

#Example 4: 392. Is Subsequence.

#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

#A subsequence of a string is a sequence of characters that can be obtained by deleting
#  some (or none) of the characters from the original string, while maintaining the 
# relative order of the remaining characters. For example, "ace" is a subsequence of 
# "abcde" while "aec" is not.
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)





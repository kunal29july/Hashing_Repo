'''
https://leetcode.com/problems/intersection-of-two-arrays-ii/
'''
'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as 
it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
'''
'''
Concept:
Similar patter to INTERSECTION OF TWO ARRAYS 1 
'''

#CODE 
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Hash_map={}
        ans=[]
        for num in range (len(nums1)):
            if nums1[num]  not in Hash_map:
                Hash_map[nums1[num]]=1
            else:
                 Hash_map[nums1[num]]= Hash_map[nums1[num]]+1


        for i in range (len(nums2)):
            if nums2[i] in Hash_map and Hash_map[nums2[i]]>0:
                ans.append(nums2[i]) 
                Hash_map[nums2[i]]=Hash_map[nums2[i]]-1       

        return ans

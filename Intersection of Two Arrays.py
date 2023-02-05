'''
https://leetcode.com/problems/intersection-of-two-arrays/description/

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

onstraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


'''
'''
concept:
1. traverse through the nums1 array and add numbers to hashmap.
2. key is number and value is True or False
3. traverse through the second array(nums2) and check if that element is present is hashmap.
  if the element not present---> we dont have to add that element into ans
  if element is present and its value is "True" then add that element to ans and make its value as "False"
4. return ans arr.
'''
#CODE



class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        memo={}
        ans=[]

        for i in range (len(nums1)):
            if nums1[i] not in memo:
                memo[nums1[i]]=True
        #print(memo)
        for val in range (len(nums2)):
            if nums2[val] in memo and memo[nums2[val]]==True:
                ans.append(nums2[val])
                memo[nums2[val]]=False
        return ans

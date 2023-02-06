'''
https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

Pre-require concept:
  ##Subarray with sum==0
  
  
1. find prefix sum of array
2. find largest distance between 2 same element

'''
'''
Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

Example 1:

Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.
Your Task:
You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
'''
class Solution:
    def maxLen(self, n, arr):
        #Code here
        prefix=[0]
        summ=0
        for ele in range (len(arr)):
            summ=summ+arr[ele]
            prefix.append(summ) #prefix sum ka array bna rhe
        
        #map se check kro duplicate
        ans=0
        mapp={}
        for i in range (len(prefix)):
            if prefix[i] not in mapp:
                mapp[prefix[i]]=i
            else:
                
                ans=max(ans,i-mapp[prefix[i]])
                mapp[prefix[i]]=min(i,mapp[prefix[i]])
        return ans

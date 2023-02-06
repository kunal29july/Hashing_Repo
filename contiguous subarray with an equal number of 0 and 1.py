'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''

'''
concept:
1.we need to covert this array in such way that it should form continuous largest array with sum==0
2. replace 0 with -1
3. find prefix sum
4. find largest distance between two duplicate numbers.

'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        temp=[]
        for i in range (len(nums)):
            if nums[i]==0:
                temp.append(-1)
            else:
                temp.append(nums[i])

        #print(temp)
        # find prefix sum

        pre=[0]
        summ=0
        for i in temp:
            summ=summ+i
            pre.append(summ)
        #print(pre)
        # find largest distance between two duplicates
        memo={}
        ans=0
        for i in range(len(pre)):
            if pre[i] not in memo:
                memo[pre[i]]=i

            else:
                ans=max(ans,i-memo[pre[i]])
                memo[pre[i]]=min(i,memo[pre[i]])



        return ans

'''
https://practice.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
'''
'''
Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.

Example 1:

Input:
5
4 2 -3 1 6

Output: 
Yes

Explanation: 
2, -3, 1 is the subarray 
with sum 0.
Example 2:

Input:
5
4 2 0 1 6

Output: 
Yes

Explanation: 
0 is one of the element 
in the array so there exist a 
subarray with sum 0.
Your Task:
You only need to complete the function subArrayExists() that takes array and n as parameters and returns true or false depending upon whether there is a subarray present with 0-sum or not. Printing will be taken care by the drivers code.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).
'''
'''
concept:

1.find prefix sum
2. find if there is duplicate,subaaray---> L-1 to R 
'''
#CODE
class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        pre=[0]
        summ=0
        for i in arr:
            summ=summ+i
            pre.append(summ)
        
        memo={}
        for i in range (len(pre)):
            if pre[i] not in memo:
                memo[pre[i]]=1
            else:
                memo[pre[i]]=memo[pre[i]]+1
                
        for j in range (len(pre)):
            if memo[pre[j]]>1:
                return True
        return False
        

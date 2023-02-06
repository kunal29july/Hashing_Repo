'''
Input:
n = 7
A[] = {1,0,0,1,0,1,1}
Output: 8
Explanation: The index range for the 8 
sub-arrays are: (0, 1), (2, 3), (0, 3), (3, 4), 
(4, 5) ,(2, 5), (0, 5), (1, 6)
Example 2:

Input:
n = 5
A[] = {1,1,1,1,0}
Output: 1
Explanation: The index range for the 
subarray is (3,4).

'''
'''
concept:
1.covert the question in subarray sum==0 by replacing 0 to -1
2.find prefix sum
3. count number of pairs, using freq(frq-1)//2---> which will give number of subarray with sum==0
'''
#User function Template for python3

class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        temp=[]
        for i in arr:
            if i==0:
                temp.append(-1)
            else:
                temp.append(1)
        #temp=[1,-1,-1,1,-1,1,1]
        
        pre=[0]
        summ=0
        for i in temp:
            summ=summ+i
            pre.append(summ)
        #pre=[0,1,0,-1,0,-1,0,1]
        
        #now question got converted into num of subarray with sum==0
        
        #count freq of each element and number of duplicate pairs
        memo={}
        for i in range(len(pre)):
            if pre[i] not in memo:
                memo[pre[i]]=1
            else:
                memo[pre[i]]=memo[pre[i]]+1
         
        #print(memo)       
        #count subarray using freq(freq-1)//2
        
        count=0
        
        for i in memo:
            p=memo[i]
            x=p-1
            r=(p*x)//2
            count=count+r
            
        return count

#maximum sum array

"""
1. using(Kadane’s Al) optimized technique with O(n) time complexity 
2. sum the elements in order and if val is greater than maxsm will update maxsm;
3. sum will continue till its sum of subarray is greater than 0, which mean it will have somthing to addup in total sum;
4. for all neg 2 step will help 
"""
def maxSumOpt(arr):
	maxsm=-9999
	tillmax=0
	for i in range(len(arr)):
		tillmax+=arr[i]
		if tillmax >maxsm:
			maxsm=tillmax
		if tillmax<=0:			
			tillmax=0
	return maxsm
#arr=[-2, -3, 4, -1, -2, 1, 5, -3]

"""
naive technique using 2 loops with O(n^2) time complexity. 
"""

def maxSumNaive(arr):
	sum=0
	maxtillnow=-999999
	n=len(arr)
	for i in range(0,n):
		sum=0
		for j in range(i,n):
			sum+=arr[j]
			if sum>maxtillnow:
				
				maxtillnow=sum
	
	return maxtillnow						

"""
using Divide and conqure technique with O(nlog(n)) time complexity. 
"""

def maxSumMidDAC(arr, l, m, r):
	sm=0 # initalize sum
	lsm=-99999 #very small no. to set lower limit of max sum 
	
	
	
	for i in range(m,l-1,-1):
		sm+=arr[i]
		if sm > lsm:
			lsm=sm
	sm=0
	rsm=-99999
	for i in range(m+1, r+1):
		sm+=arr[i]
		if sm > rsm:
			rsm=sm
	return rsm+lsm
				
def maxSumDAC(arr, l, r):
	
	"""
	Divde the list in three part 1) left to mid 2) right to mid and 3) crossover at mid
	then will retain the value which is max in above three cases
	Provide start point and lenght of array 
	"""
	if (l==r):
		return arr[l]
	m=(l+r)//2
	
	return max(maxSumDAC(arr,l,m),maxSumDAC(arr,m+1,r), maxSumMidDAC(arr, l, m, r))
	
arr=[-2, -3, 4, -1, -2, 1, 5, -3]

print( maxSumNaive(arr))

print(maxSumDAC(arr,0 , len(arr)-1))


print(maxSumOpt(arr))




#insert sort using recursion
'''
implementing insertion sort using recursion method:

1. The array elements are compared with each other sequentially and then arranged.
2. Inplace sorting algo
3. Avg and Worst time complexity O(n^2)
'''

def recursiveInsertSort(arr,i=1):
	#recursion stop condn when no more element is available to check 
    if i >len(arr)-1:
		print(arr)
		return

	j=i-1
    #keep moving till you find lower number
	while(j>=0 and arr[i]<arr[j]):
		
		j-=1
    # swap if lower number is find    
	if j+1<i:
		v=arr.pop(i)
		
		arr=arr[:j+1]+[v]+arr[j+1:]
		
	recursiveInsertSort(arr,i+1)
	
if __name__=="__main__":
    recursiveInsertSort([3,2,6,8,8,5,1,4,8])

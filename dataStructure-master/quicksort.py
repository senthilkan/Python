# quick Sort
'''Camparision sort:

1. Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. 
2. tree like sorting algo.
3. time complexity O(n^2), avg: O(nlog(n))

'''
def partition(arr,s,e): 
	k = s-1        
	pivot = arr[e]    

	for j in range(s , e): 

		# If current element is smaller than or 
		# equal to pivot 
		if   arr[j] <= pivot: 
		  
			# increment index of smaller element 
			k = k+1 
			arr[k],arr[j] = arr[j],arr[k] 

	arr[k+1],arr[e] = arr[e],arr[k+1] 
	return k+1 

# Function to do Quick sort 
def quickSort(arr,s,e): 
	if s < e: 

		k = partition(arr,s,e) 


		quickSort(arr, s, k-1) 
		quickSort(arr, k+1, e) 
	return arr
arr=[7,5,3,4,6,1,2,8,1]
print(quickSort(arr,0,len(arr)-1))

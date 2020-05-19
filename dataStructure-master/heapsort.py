#heap  Sort
'''
1. Heap sort is a comparison based sorting technique based on Binary Heap data structure.
    It is similar to selection sort where we first find the maximum element and place the maximum element at the end
2. Time Complexity: Time complexity of heapify is O(Logn).
    Time complexity of createAndBuildHeap() is O(n) and overall time complexity of Heap Sort is O(nLogn).
3. Binary tree    
'''

# l= 2*i +1
# r= 2*i +2

def heapSort(arr):
    #heapify to make root the largest no. between root and children
	def heapify(arr,i):
		n=len(arr)
		i+=1
        #traverse all left and right child
		l= i*2+1
		r= i*2+2
		# recursion break condition, reach leaf node
		if i>n:
			return	arr
            
		heapify(arr,i)
		if l<n and arr[l]>arr[i]:
			_=arr[i]
			arr[i] = arr[l]
			arr[l]=_
		
		if r<n and arr[r]>arr[i]:
			_=arr[i]
			arr[i] = arr[r]
			arr[r]=_
			
		#print(arr)
		return arr
	
    
	n=len(arr)
	arr1=[]
	i=-1
    
	arr=heapify(arr,i)
	for j in range(n):
		arr[0], arr[-1]=arr[-1],arr[0]
	
		arr1.append(arr.pop())
		
		arr=heapify(arr,-1)
	
		
	return arr1
if __name__=="__main__":		
    print(heapSort([6, 7, 4, 10, 12, 3, 1, 2, 9, 5, 11]))

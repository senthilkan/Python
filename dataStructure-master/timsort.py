#Timsort 
'''
TimSort is a sorting algorithm based on Insertion Sort and Merge Sort.
A stable sorting algorithm works in O(n Log n) time
Used in Java’s Arrays.sort() as well as Python’s sorted() and sort().
First sort small pieces using Insertion Sort, then merges the pieces using merge of merge sort.
worst case nlog(n).


'''
import math
def timSort(arr):
	k=math.floor(math.log(len(arr)))
	
	def insertionSort(arr):
		k1=len(arr)
		for i in range(1,k1):
			
			for j in range(i, k1-1):
				while(j>0 and arr[j]<arr[i]):
					j-=1
				if j>=0:
					v=arr.pop(i)
					
					arr=arr[:j]+v+arr[j:]
		return arr
		
	def mergeSort(arr,k):
		if len(arr)>k:
			m=len(arr)//2
			l=arr[:m]
			r=arr[m:]
			L=mergeSort(l,k)
			R=mergeSort(r,k)
			#print(L,R)
			x=0
			y=0
			z=0
			
			while  x<len(L) and y<len(R):
				
				if L[x]<R[y]:
					arr[z]=L[x]
					z+=1
					x+=1
				else:
					arr[z]=R[y]
					z+=1
					y+=1		
			
			
			while(x<len(L)):
				
				arr[z]=L[x]
				z+=1
				x+=1		
			
			while(y<len(R)):
				arr[z]=R[y]
				z+=1
				y+=1
			#print(arr)	
			return arr
		else:
			return insertionSort(arr)
	return (mergeSort(arr,k))
    
if __name__=="__main__":			
    print(timSort([1,2,4,-7,5,3])		)
				
				
				
				
				

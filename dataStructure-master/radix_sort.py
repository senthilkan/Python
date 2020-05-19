# Radix Sort
'''
We can’t use counting sort because counting sort will take O(n2) which is worse than comparison based sorting algorithms. 
Can we sort such an array in linear time?
Radix Sort is the answer. The idea of Radix Sort is to do digit by digit sort starting from least significant digit to most significant digit. 
Radix sort uses counting sort as a subroutine to sort.
it sort from LSD to MSD
'''
def radix_sort(arr):
	
	
	def count_sort(arr,i):
        
		count={j:[] for j in range(0,10)}
		j=10**i
		for val in arr:
			print(val,j)
			count[val%(j)//(j*0.1)].append(val)
		ans=[]
        
		for val in count.keys():
			if count[val] !=[]:
				
				ans=ans+count[val]
		return ans				 
    # count sort based on decimal places using i 
	n=len(str(arr[0]))
	for i in range(n):
		
		arr=count_sort(arr,i+1)
		
	return arr

if __name__=="__main__":
	print(radix_sort([21,41,50,61,75,84,17,11,21,5,3]))
						

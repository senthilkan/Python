#counting sort

'''
1. Counting sort is a sorting technique based on keys between a specific range.
 It works by counting the number of objects having distinct key values (kind of hashing).
 Then doing some arithmetic to calculate the position of each object in the output sequence.
2. Time Complexity: O(n+k) where n is the number of elements in input array and k is the range of input.
'''
def count_sort(arr):
	count={i:0 for i in range(0,10)}
	
	#created and initialize the counter using dictionary or alternate is to use array where index use as the key
	for val in arr:
		count[val]+=1
	ans=[]
	#print(count)
    # keep updating the counter keys and then combine to get the output 
	for val in count.keys():
		if count[val]>0:
			print([val]*count[val])
			ans=ans+([val]*count[val])
	return ans				


if __name__=="__main__":
	print(count_sort([3,2,6,5,8,1,9,3,4,9,9,5]))

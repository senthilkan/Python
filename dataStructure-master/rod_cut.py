#rod-cut problem

#recursive method

def Rrod_cutter(arr,n):
	max_val=-999999
	#setting lowest val to initialize the max_val
	
	if n<1:
	#return when each value is checked and exit statement of recursion
		return 0
	#cheking max val of each no and combination below n
	#1,2,3,4,5,6,7
	#all possible can be obtain sum of i and n-i like, 1+6, 2+5, 3+4 etc for 7 	
	for i in range(n):
		max_val=max(max_val,arr[i]+Rrod_cutter(arr,n-i-1))
		
	return max_val
	
	
#dynamic program:
def Drod_cutter(arr,n,d):
	#creating dictionary to store the value of calculated n previously, rest is same
	#if max val is already calculated for n, otherwise run recursion for that time
	if n in d.keys():
		return d[n]
	else:
		max_val=-999999
	
		if n<1:
			return 0
		for i in range(n):
			max_val=max(max_val,arr[i]+Drod_cutter(arr,n-i-1,d))
		d[n]=max_val	
		return max_val
		
	
	

if __name__ == "__main__":
	
	n=20
	#don't increase n value too much, as recursion method willl breakdown
	import time
	
	arr=[1,5,8,9,10,17,17,20,24,30,1,5,8,9,10,17,17,20,24,30,1,5,8,9,10,17,17,20,24,30,1,5,8,9,10,17,17,20,24,30]
	#running dynamic method 
	t1=time.time()
	print(Drod_cutter(arr, n,{}))
	print(time.time()-t1)
	
	#running recursive method
	t1=time.time()
	print(Rrod_cutter(arr, n))
	print(time.time()-t1)
	
	
	

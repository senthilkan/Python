#insertion sort 

'''
1. The array elements are compared with each other sequentially and then arranged.
2. Inplace sorting algo
3. Avg and Worst time complexity O(n^2)
'''
def insertion_sort(arr, order="asec"):
    for i in range(1,len(arr)):
        j=i-1
        insertion=False
        #print(arr[j], arr[i])
        if order=="desc":
        
            #print(arr[j],arr[i])
            #print(i)
            while (j>=0 and arr[j]< arr[i]):
                #print(arr[j],arr[i])
                j-=1
                
                insertion=True
                
            
        else:
            
            while j>=0 and arr[j]> arr[i]:
            
                j-=1
                insertion=True
        if insertion:
            #print(arr[j],arr[i])
            val=arr.pop(i)
            
            arr.insert(j+1,val)
            
            
        print(("after iter {} : {}").format(i,arr))
    return arr

if __name__=="__main__":    
    print("\nsorted list : ",insertion_sort([1,5,4,2,3,4]))

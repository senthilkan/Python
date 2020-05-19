#selection sort
'''
1. The selection sort algorithm sorts an array by repeatedly finding the minimum element 
    (considering ascending order) from unsorted part and putting it at the beginning.
2. Inplace sorting algo
3. Worst time complexity O(n^2)
    
'''
def select_sort(arr,order='asec'):
    for i in range(0,len(arr)):
        swap=False
        key=i
        for j in range(i+1, len(arr)):
            if order=="asec":
                if arr[key]>arr[j]:
                    key=j
                    swap=True
            elif order == "desc":        
                if arr[key]<arr[j]:
                        key=j
                        swap=True        
        if swap:
            _=arr[i]
            arr[i]=arr[key]
            arr[key]=_
        print(("after iter {} : {}").format(i,arr))
    return arr
    
if __name__=="__main__":
    print("\nSorted list: ",select_sort([1,5,4,4,7,8],order="desc"))
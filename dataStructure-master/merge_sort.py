#merge sort

def mergeSort(arr,order="asec"):
    if len(arr)>1:
            
            
        n=len(arr)//2
        L=arr[:n]
        R=arr[n:]
        
        mergeSort(L,order)
        mergeSort(R,order)
        i,j,k=0,0,0
        #create temp orted array
        while i<len(L) and j<len(R):
            if L[i]<R[j] and order=="asec":
                arr[k]=L[i]
                i+=1
            elif L[i]>R[j] and order=="desc":
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1    
                
        while i<len(L):
            arr[k]=L[i]
            k+=1
            i+=1
        while j<len(R):
            arr[k]=R[j]
            k+=1
            j+=1
    return arr 
if __name__=='__main__':
    print(mergeSort([3, 41, 52, 26, 38, 57, 9,49],'desc'))
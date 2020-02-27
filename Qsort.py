
def Qsort(vlas,low , high ):
    if low<high:
        pivot=partition(vals,low,high)
        Qsort(vals,low,pivot-1)
        Qsort(vals,pivot+1,high)
    else:
        return 

def partition(vals,low,high):
    pivot = vals[low]
    i=low
    j=high
    while i<j:
        while vals[j]>=pivot:
            if j>low:
                j=j-1
            else:
                break
        while vals[i]<=pivot:
            if i<high:
            
                i=i+1
            else:
                break
            
        if i<j:
           
            vals[i],vals[j]=vals[j],vals[i]
           
            
    
    vals[low],vals[j]= vals[j],vals[low]
   
    return j

vals =[5,9,3,4,1,8,88,0,98,100]
l=len(vals)
low=0
high=l-1
Qsort(vals,low,high)

for i in range(l):
    print(vals[i])
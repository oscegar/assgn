# @arg arr The input list like object to be sorted
# @arg cmp A compare function which takes two element in the array, 
#          cmp(a,b)<0   if a should be placed before b,
#          cmp(a,b)==0  if arr is still sorted after a and b are exchanged,
#          cmp(a,b)>0   if a should be placed behind b.
def multi_sort(arr, cmp, method="None"):
    if(method=="quick"):
        quick_sort(arr,cmp)
    elif(method=="merge"):
        merge_sort(arr,cmp)
    elif(method=="None"): # do nothing
        return
    else:
        print("invalid argument!")




def gaps(gap,cmp):
    if cmp(gap,1) <= 0:
        return 0
    return int(math.ceil(gap/2))

def swap(arr, i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j]= temp

def inPlaceMerge(nums,start, end,cmp):

    gap = end - start + 1
    gap = gaps(gap)

    while cmp(gap,0) > 0:
        i = start
        while cmp(i+gap, end) <=0:
            j = i + gap

            if cmp(nums[i],nums[j]) > 0:
                swap(nums, i, j)

            i += 1

        gap = gaps(gap)

def ms(arr, start, end,cmp):
    if cmp(start,end) == 0:
        return
    mid = (start + end) // 2
    ms(arr,start, mid,cmp )
    ms(arr, mid+1, end,cmp)

    inPlaceMerge(arr,start,end,cmp)

#in place ms
def merge_sort(arr,cmp):
    ms(arr, 0, len(arr) - 1,cmp)
    pass

# must be in-place sort
def part(arr,s,e,cmp):
    pvt = s
    for i in range(s+1,e+1):
        if cmp(arr[i],arr[s]) <= 0 :
            pvt+=1
            arr[i],arr[pvt] = arr[pvt], arr[i]
    return pvt


def qs(arr, s, e = None,cmp):
    if cmp(e,None) == 0:
        e = len(arr) - 1
    if cmp(s,e) <= 0:
        return
    pvt = part(arr,s,e,cmp)

    qs(arr,s,pvt-1,cmp)
    qs(arr,pvt+1, e,cmp)

def quick_sort(arr,cmp):
    qs(arr,0,None,cmp)
    pass

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




def gaps(gap):
    if gap <=1:
        return 0

    return int(math.ceil(gap/2))
def swap(arr, i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j]= temp

def inPlaceMerge(nums,start, end):

    gap = end - start + 1
    gap = gaps(gap)

    while gap > 0:
        i = start
        while (i + gap) <= end:
            j = i + gap

            if nums[i] > nums[j]:
                swap(nums, i, j)

            i += 1

        gap = gaps(gap)

def ms(arr, start, end):
    if start == end:
        return
    mid = (start + end) // 2
    ms(arr,start, mid )
    ms(arr, mid+1, end)

    inPlaceMerge(arr,start,end)

#in place ms
def merge_sort(arr,cmp):
    ms(arr, 0, len(arr) - 1)
    pass

# must be in-place sort
def quick_sort(arr,cmp):
    pass

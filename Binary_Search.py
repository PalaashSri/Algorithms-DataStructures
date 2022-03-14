class BinarySearch_Implementation:

    def Binary_Search(self,arr,key):
        low = 0
        high = len(arr)

        while low<high-1:
            mid = (low+high)//2
            if key==arr[mid]:return mid
            if key>arr[mid]:
                low = mid
            else:
                high = mid
        if arr[low]==key:return low
        else: return None

binary = BinarySearch_Implementation()
print(binary.Binary_Search([1,2,3,4,5,6,7,8,9,10],1))



class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lb, ub = 0, len(arr) - 1
        while lb <= ub:
            mid = (lb + ub) // 2
            if mid > 0 and arr[mid] > arr[mid - 1] and mid < (len(arr) - 1) and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                lb = mid + 1
            else:
                ub = mid - 1
        return -1
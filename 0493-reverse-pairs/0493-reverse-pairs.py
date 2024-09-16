class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # Helper function to perform merge sort and count reverse pairs
        def mergeSort(arr: List[int], low: int, high: int) -> int:
            if low >= high:
                return 0
            
            mid = (low + high) // 2
            count = mergeSort(arr, low, mid) + mergeSort(arr, mid + 1, high)
            
            # Count reverse pairs
            count += self.countPairs(arr, low, mid, high)
            
            # Merge the sorted halves
            self.merge(arr, low, mid, high)
            
            return count
        
        # Helper function to count reverse pairs
        def countPairs(arr: List[int], low: int, mid: int, high: int) -> int:
            count = 0
            right = mid + 1
            for i in range(low, mid + 1):
                while right <= high and arr[i] > 2 * arr[right]:
                    right += 1
                count += (right - (mid + 1))
            return count
        
        # Helper function to merge two sorted halves
        def merge(arr: List[int], low: int, mid: int, high: int):
            temp = []
            left = low
            right = mid + 1
            
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
            
            while left <= mid:
                temp.append(arr[left])
                left += 1
            
            while right <= high:
                temp.append(arr[right])
                right += 1
            
            for i in range(low, high + 1):
                arr[i] = temp[i - low]
        
        return mergeSort(nums, 0, len(nums) - 1)


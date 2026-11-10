class Solution(object):
    def sortArray(self, nums):

        n = len(nums)

        # Maintain Max Heap property
        def heapify(n, i):

            largest = i

            left = 2 * i + 1
            right = 2 * i + 2

            # Check left child
            if left < n and nums[left] > nums[largest]:
                largest = left

            # Check right child
            if right < n and nums[right] > nums[largest]:
                largest = right

            # If parent is not largest, swap
            if largest != i:

                nums[i], nums[largest] = nums[largest], nums[i]

                heapify(n, largest)

        # Step 1: Build Max Heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        # Step 2: Extract maximum repeatedly
        for i in range(n - 1, 0, -1):

            # Move largest element to the end
            nums[0], nums[i] = nums[i], nums[0]

            # Restore heap property
            heapify(i, 0)

        return nums
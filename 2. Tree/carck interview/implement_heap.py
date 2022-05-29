"""
實作min heap
1. heapify an array
2. pop
3. push

"""

class MinHeap():
    def get_children_idx(self, n_idx, nums):
        l_idx, r_idx = 2*n_idx+1, 2*n_idx+2
        if l_idx >= len(nums):
            l_idx = None
        if r_idx >= len(nums):
            r_idx = None
        return l_idx, r_idx

    def get_parent_idx(self, n_idx):
        if n_idx % 2 == 0: # right node
            f_idx = int((n_idx - 2) // 2)
        else:
            f_idx = int((n_idx - 1) // 2)
        return f_idx

    def heap_down(self, idx, nums):
        while idx < len(nums):
            l_idx, r_idx = self.get_children_idx(idx, nums)
            left_child = float('inf') if not l_idx else nums[l_idx]
            right_child = float('inf') if not r_idx else nums[r_idx]

            if nums[idx] > left_child and left_child <= right_child:
                nums[idx], nums[l_idx] = nums[l_idx], nums[idx]
                idx = l_idx
            elif nums[idx] > right_child and right_child <= left_child:
                nums[idx], nums[r_idx] = nums[r_idx], nums[idx]
                idx = r_idx
            else:
                break

    def heap_up(self, idx, nums):
        while idx >= 0:
            parent_idx = self.get_parent_idx(idx)
            if nums[parent_idx] > nums[idx]:
                nums[idx], nums[parent_idx] = nums[parent_idx], nums[idx]
                idx = parent_idx
            else:
                break

    def heapify(self, nums):
        for n_idx in range(len(nums))[::-1]:  # 由後往前檢查
            self.heap_down(n_idx, nums)

    def pop(self, nums):
        if not nums:
            return None
        min_nums = nums[0]
        latest_num = nums.pop(-1)
        if nums:
            nums[0] = latest_num
            self.heap_down(0, nums)
        return min_nums

    def push(self, nums, new_num):
        nums.append(new_num)
        self.heap_up(len(nums)-1, nums)

    def pushpop(self, nums, new_num):
        if new_num <= nums[0]:
            return new_num
        min_num = nums[0]
        nums[0] = new_num
        self.heap_down(0, nums)
        return min_num



heap = MinHeap()
nums = [5,1,2,7,8,9,10,7,11,0]
print("nums: ", nums)
heap.heapify(nums)
print("heapify: ", nums)
v = heap.pop(nums)
print("pop: ", v, nums)
v = heap.push(nums, 4)
print("push 4: ", v, nums)
v = heap.pop(nums)
print("pop: ", v, nums)
v = heap.pushpop(nums, 6)
print("pushpop 6: ", v, nums)
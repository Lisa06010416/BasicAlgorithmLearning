"""382. Linked List Random Node"""
import random
from typing import Optional

class Solution:

    def __init__(self, head: Optional[ListNode]):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        pool_size = 1
        pool = [self.head.val]

        temp_head = self.head.next
        node_nums = 1
        while temp_head:
            if random.randint(0, node_nums) == 0:
                pool[0] = temp_head.val
            temp_head = temp_head.next
            node_nums += 1

        return pool[0]
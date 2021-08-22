class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



"""143. Reorder List"""
class Solution:
    """將一個 linking list 由 1->2->3->4 改為 1->4->2->3"""
    def reorderList(self, head: ListNode) -> None:
        """
        找到 linking list 的中間點，將 linking list 由中間點斷開，將尾部的linking list反轉並插入前面的
        """
        # 找到中間點
        faster, slow = head, head
        while faster.next and faster.next.next:
            faster = faster.next.next
            slow = slow.next

        # 斷開
        first_list_head = head
        second_list_head = slow.next
        slow.next = None

        # 反轉 second list
        pre_node = None
        while second_list_head:
            next_node = second_list_head.next
            second_list_head.next = pre_node
            pre_node = second_list_head
            second_list_head = next_node

        second_list_head = pre_node

        # insert
        while second_list_head:
            temp_node1 = first_list_head.next
            temp_node2 = second_list_head.next
            first_list_head.next = second_list_head
            second_list_head.next = temp_node1
            first_list_head = temp_node1
            second_list_head = temp_node2



"""206. Reverse Linked List"""
class Solution:
    """反轉一個linking list"""
    def reverseList(self, head: ListNode) -> ListNode:
        """
        1. record next node
        2. modify point
        3. record prenode
        4. go to next node
        """
        pre_node = None
        while head:
            next_node = head.next
            head.next = pre_node
            pre_node = head
            if next_node:
                head = next_node
            else:
                break
        return head
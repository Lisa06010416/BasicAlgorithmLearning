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
        nh   p    h
        O -> O -> o
        """
        new_head = None
        while head:
            # record point node
            point = head
            # move head
            head = head.next
            # modify linking
            point.next = new_head
            # record reivious node
            new_head = point
        return new_head


"""146. LRU Cache"""
class Node:
    def __init__(self, key=None, val=None, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next


class DoubleLinklingList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail  # latest

    def add_new_node(self, key, val):
        new_node = Node(key, val, self.tail)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head, self.tail = new_node, new_node
        return new_node

    def arrange_node(self, node):
        pren, nextn = node.pre, node.next
        if pren:
            pren.next = nextn
        if nextn:
            nextn.pre = pren

        node.pre = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node

        # !! 如果 node 是 head 的情況
        if node == self.head:
            self.head = nextn

    def del_head(self):
        key = self.head.key
        self.head = self.head.next
        self.head.pre = None
        return key


class LRUCache:
    """
    實作LRT(Least Recently Used) Catch，要求get/put時間在O(1)內
    使用 DICT + Double Linking List
    用DICT記住每一個key對應到的node，在用Double Linking List維護使用的順序
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_dict = {}
        self.node_num = 0
        self.lru_sequence = DoubleLinklingList()

    def get(self, key: int) -> int:
        # 查詢並且更正lru_sequence的順序
        if key in self.node_dict:
            node = self.node_dict[key]
            self.lru_sequence.arrange_node(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 新增一個node
        if key not in self.node_dict:
            new_node = self.lru_sequence.add_new_node(key, value)
            self.node_dict[key] = new_node
            self.node_num += 1
        else:  # key之前已經出現過，更正一個node
            new_node = self.node_dict[key]
            new_node.val = value
            self.lru_sequence.arrange_node(new_node)

        # 如果node數量大於capacity，則刪除head
        if self.node_num > self.capacity:
            key = self.lru_sequence.del_head()
            del self.node_dict[key]
            self.node_num -= 1

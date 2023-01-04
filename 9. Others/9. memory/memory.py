class Solution:
    """由 Linking List 中刪掉一個 node, 但不會給head只會給要刪掉的node"""
    def deleteNode(self, node):
        """
        運用memory的特性
        """
        node.val = node.next.val
        node.next = node.next.next

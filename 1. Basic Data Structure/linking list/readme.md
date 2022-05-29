# Linking List
主要是在考指針的修改 or 使用Linking List的結構減少複雜度

**題型:**
* 指針修改 ex merge/modify/insert
    * reverse
    * find mid/split link list - fast/slow point
        ```
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_head = slow.next
        ```
* 使用 Linking List 的結構減少複雜度
    * ex
        * LRU Catch - Dict + Double Linking List

**技巧:**
* new head
* fast/slow point
    * 判斷是否有環
    * 找中點

**需要注意的地方:**
* 頭尾是否有空值的問題
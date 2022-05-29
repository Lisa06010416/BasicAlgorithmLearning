
"""367 · Expression Tree Build"""
class ExpressionTreeNode:
    def __init__(self, symbol):
        self.symbol = symbol
        self.left, self.right = None, None

class Solution:
    """
    Input: ["2","*","6","-","(","23","+","7",")","/","(","1","+","2",")"]
    build a expression tree :
	                 [ - ]
	             /          \
	        [ * ]              [ / ]
	      /     \           /         \
	    [ 2 ]  [ 6 ]      [ + ]        [ + ]
	                     /    \       /      \
	                   [ 23 ][ 7 ] [ 1 ]   [ 2 ]
    """
    def build(self, expression):
        # write your code here
        """
        1. 給予每個符號給每符weight，*,/ 為 2、+,-為1、數字為極大值，當遇到(時提升時提升weight，
            遇到)時降低降weight
        2. monotonic stack :
          如果stack top的weight大於新的element,則 pop
           a. 如果如pop後stack為空，則則pop的元素為新元素的左孩子
           b. 如果新的stack top weight < new element weight => pop element 是 new element 的左孩子
           c. 如果新的stack top weight >= new element weight => pop element 是 stack top 的右孩子
           d. 最後被pop出來的是root
        """
        symbol2weight = {
            "*": 2,
            "/": 2,
            "+": 1,
            "-": 1,
        }
        expression.append("@")  # tips 讓全部的值都可以出 stack
        stack = [] # 遞增stack
        add_weight = 0
        root = None
        for new_element in expression:
            # get element weight
            if new_element in symbol2weight:
                new_weight = symbol2weight[new_element] + add_weight
            elif new_element == "(":
                add_weight += 1
                continue
            elif new_element == ")":
                add_weight -= 1
                continue
            elif new_element == "@":
                root = stack[0]
                new_weight = float("-inf")
            else:
                new_weight = float("inf")

            # new node
            new_node = ExpressionTreeNode(new_element)
            if not stack or stack[-1][1] < new_weight:  # 如果stack為空 or top weight < new_weight  => 直接 push
                stack.append([new_node, new_weight])
            else: # 當stack不維持遞增時
                while stack and new_weight <= stack[-1][1]:
                    pop_element = stack.pop()
                    if not stack or stack[-1][1] < new_weight: # 如果新的stack top weight < new element weight => pop element 是 new element 的左孩子
                        new_node.left = pop_element[0]
                        stack.append([new_node, new_weight])
                    else:
                        stack[-1][0].right = pop_element[0]  # 如果新的stack top weight >= new element weight => pop element 是 stack top 的右孩子

            for e in stack:
                print(e[0].symbol, e[0].left, e[0].right, e[1])
        return root[0]

s = Solution()
ans = s.build(["2","*","6","-","(","23","+","7",")","/","(","1","+","2",")"])
print(ans, ans.symbol, ans.left.symbol, ans.left.left.symbol)
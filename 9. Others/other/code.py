"""
251. Flatten 2D Vector

給予一個2D的array，寫一個iterator，可以透過next()拿到相對的值，直到hasenext()為false
"""

# 作法一：直接用yield,但不符合題目的要求函式呼叫方式
def Vector2D(vec2d):
    for i in vec2d:
        for j in i:
            yield j

vec2d = [[1,2,3], [4,5,6]]
iter = Vector2D(vec2d)
print(next(iter))

# 作法二：建立一個類別處理iterator
class Vector2D():
    def __init__(self, vec2d):
        self.iter = self._get_iter(vec2d)
        self.count = 0
        self.ele_num = 0
        for i in vec2d:
            self.ele_num += len(i)

    def _get_iter(self, vec2d):
        def IterVector2D(vec2d):
            for i in vec2d:
                for j in i:
                    yield j
        return IterVector2D(vec2d)

    def next(self):
        self.count += 1
        return next(self.iter)

    def has_next(self):
        if self.count >= self.ele_num:
            return False
        return True

vec2d = [[1,2,3], [4,5,6]]
iter = Vector2D(vec2d)
print(iter.next())
print(iter.next())
print(iter.has_next())

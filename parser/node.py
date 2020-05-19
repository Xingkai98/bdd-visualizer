
# 用于语义分析的节点
class BooleanVariableNode():
    def __init__(self, value=None):
        self.value = value

class ExprNode():
    def __init__(self, left=None, right=None, child=None, value=None):
        self.value = value
        self.left = left
        self.right = right
        self.child = child
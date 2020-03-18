
class BooleanVariableNode():
    def __init__(self, value=None):
        self.value = value

class ExprNode():
    def __init__(self, left=None, right=None, child=None, value=None):
        self.value = value
        self.left = left
        self.right = right
        self.child = child

class EvaluationVisitor():

    variables = {
        'x1' : True,
        'x2' : False,
    }

    def __init__(self, variables=None):
        self.variables = variables

    def visit(self, node):
        if isinstance(node, ExprNode):
            if node.value == '¬':
                return bool(1-self.visit(node.child))
            elif node.value == '∧':
                return self.visit(node.left) and self.visit(node.right)
            elif node.value == '∨':
                return self.visit(node.left) or self.visit(node.right)
            elif node.value == '<=>':
                return bool(self.visit(node.left) == self.visit(node.right))
            elif node.value == '=>':
                left = self.visit(node.left)
                right = self.visit(node.right)
                if left and not right:
                    return False
                else:
                    return True
        elif isinstance(node, BooleanVariableNode):
            if node.value in self.variables:
                return bool(self.variables[node.value])
            else:
                print(str(node.value) + '变量未定义。')
                return False
        else:
            return
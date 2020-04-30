
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

    variables = {}

    def visit(self, node, variables): # 获取表达式的值
        self.variables = variables
        return self.visit_for_value(node=node)

    def visit_for_value(self, node):   # 获取表达式的值-递归函数
        if isinstance(node, ExprNode):
            if node.value == '¬':
                return bool(1-self.visit_for_value(node.child))
            elif node.value == '∧':
                return self.visit_for_value(node.left) and self.visit_for_value(node.right)
            elif node.value == '∨':
                return self.visit_for_value(node.left) or self.visit_for_value(node.right)
            elif node.value == '<=>':
                return bool(self.visit_for_value(node.left) == self.visit_for_value(node.right))
            elif node.value == '=>':
                left = self.visit_for_value(node.left)
                right = self.visit_for_value(node.right)
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

    def visit_for_var_list(self, node):   # 获取变量列表
        var_list = []
        if isinstance(node, ExprNode):
            if node.value == '¬':
                return self.visit_for_var_list(node.child)
            elif node.value == '∧' or '∨' or '<=>' or '=>':
                left_vlist = self.visit_for_var_list(node.left)
                right_vlist = self.visit_for_var_list(node.right)
                return list(set(left_vlist).union(right_vlist))
            else:
                pass
        elif isinstance(node, BooleanVariableNode):
            var_list.append(str(node.value))
            print(str(node.value))
            return var_list
        else:
            pass
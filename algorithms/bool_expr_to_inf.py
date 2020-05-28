from antlr_facility import *
import queue
from graph_node import *

class Obj:
    def __init__(self,a,current_var,node=None):
        self.a = a
        self.current_var = current_var
        self.node = node

# a -> b1, b2 (current_var)
# b1为取值为1的分支，b2为取值为0的分支，类型为str或bool
class INFExpr:

    index = 0 # 表明当前的current_var在所有相同变量的下标顺序
    highlighted = False # 是否高亮

    def __init__(self, t='t', a='', current_var=None, b1=None, b2=None,
                 tree_position=None):
        self.t = t
        if isinstance(a, str):
            self.a = a

        if isinstance(current_var, str):
            self.current_var = current_var

        self.b1 = b1
        self.b2 = b2

        self.tree_position = tree_position

    def highlight(self):
        self.highlighted = True

    @property
    def is_highlighted(self):
        return self.highlighted

    def to_str(self):
        s = self.t + self.a + ' -> '
        if isinstance(self.b1,bool):
            s += str(int(self.b1))
        else:
            s += 't' + self.b1

        s += ','

        if isinstance(self.b2,bool):
            s += str(int(self.b2))
        else:
            s += 't' + self.b2

        s += ' (' + self.current_var + ')'
        return s

    def equals(self, inf_expr):
        if self.current_var == inf_expr.current_var and self.b1 == inf_expr.b1 and self.b2 == inf_expr.b2:
            return True
        else:
            return False

class BoolExprToInf:
    variables = {}
    var_list = []
    result_table = {}
    bool_expr = ''

    inf_list = []  # INF范式
    decision_tree = None  # 决策树
    simplified_inf_list = []  # 简化后的INF范式
    simplified_inf_dict = {}  # 根据a得到INF范式的字典{'001': INFExpr,...}
    obdd_tree = None  # OBDD
    obdd_node = {}  # 根据变量名得到OBDD节点坐标列表
    a_to_node = {}  # 根据a得到变量节点及下标顺序

    def __init__(self, canvas=None, var_list=None,
                 default_var='t', bool_expr='',
                 variables=None,
                 root_center=None):
        self.canvas = canvas
        self.var_list = var_list
        self.variables = variables
        self.default_var = default_var
        self.bool_expr = bool_expr
        self.root_center = root_center

        self.p = AntlrFacility()
        self.generate_result_table()  # 得到真值表
        # print('真值表：')
        # print(self.result_table)

    # '{'x1'=1,x2=0'}' <==> '10'
    def dict_to_str(self, variables):
        s = ''
        for i in variables:
            s += str(int(variables[i]))
        return s

    # '10' <==> '{'x1'=1,'x2'=0}'
    def str_to_dict(self, str):
        variables = {}
        if len(str) == len(self.var_list):
            for index, ch in enumerate(str):
                variables[self.var_list[index]] = int(ch)
        return variables

    # 6 => '110'
    def num_to_str(self, num):
        l = len(self.var_list)
        return str(bin(num).zfill(l + 2)).replace('b', '')[1:]

    # 2 => '{'x1'=1,'x2'=0}'
    def num_to_dict(self, num):
        s = self.num_to_str(num)
        return self.str_to_dict(s)

    def generate_result_table(self):
        l = len(self.var_list)
        for i in range(2 ** l):
            variables = self.num_to_dict(i)
            result = self.p.get_parse_result(text=self.bool_expr, variables=variables)
            self.result_table[self.num_to_str(i)] = result

    def get_inf_list(self, generate_decision_tree=True, debug=False):
        self.generate_raw_inf_list(generate_decision_tree=generate_decision_tree,
                                   debug=debug)
        self.simplify_inf_list(debug=debug)  # 得到简化后的INF
        return self.simplified_inf_list

    def get_inf_dict(self, generate_decision_tree=True, debug=False):
        self.generate_raw_inf_list(generate_decision_tree=generate_decision_tree,
                                   debug=False)
        self.simplify_inf_list(debug=debug)  # 得到简化后的INF
        return self.simplified_inf_dict

    def generate_raw_inf_list(self, generate_decision_tree=True, debug=False):
        self.inf_list.clear()
        decay = 10
        if generate_decision_tree is True:
            root_node = Node(canvas=self.canvas, center=self.root_center,
                             text=self.var_list[0],
                             d=60, h=60)
            init_obj = Obj(a='', current_var=self.var_list[0], node=root_node)
        else:
            init_obj = Obj(a='', current_var=self.var_list[0])

        if debug is True:
            print("INF范式：")
        q = queue.Queue()
        q.put(init_obj)

        while not q.empty():
            cur_obj = q.get()
            l = self.create_inf_bfs(a=cur_obj.a, current_var=cur_obj.current_var)

            if generate_decision_tree is True:
                # len(l) 说明两子节点都非终端节点，若l[0]l[1]都为bool则都为终端节点
                if len(l):
                    # '1' high
                    if l[0] is not False and l[0] is not True:
                        cur_obj.node.create_child_node(direc='high', text=l[0][1],
                                                       decay=decay)
                        child_node = cur_obj.node.high_child
                        obj = Obj(a=l[0][0], current_var=l[0][1], node=child_node)
                        q.put(obj)
                    else:
                        cur_obj.node.create_child_node(direc='high', text=str(int(l[0])),
                                                       decay=decay, isLeaf=True)
                    # '0' low
                    if l[1] is not False and l[1] is not True:
                        cur_obj.node.create_child_node(direc='low', text=l[1][1],
                                                       decay=decay)
                        child_node = cur_obj.node.low_child
                        obj = Obj(a=l[1][0], current_var=l[1][1], node=child_node)
                        q.put(obj)
                    else:
                        cur_obj.node.create_child_node(direc='low', text=str(int(l[1])),
                                                       decay=decay, isLeaf=True)
            else:
                # len(l) 说明两子节点都非终端节点，若l[0]l[1]都为bool则都为终端节点
                if len(l):
                    # '1' high
                    if l[0] is not False and l[0] is not True:
                        obj = Obj(a=l[0][0], current_var=l[0][1])
                        q.put(obj)

                    # '0' low
                    if l[1] is not False and l[1] is not True:
                        obj = Obj(a=l[1][0], current_var=l[1][1])
                        q.put(obj)

        if debug is True:
            for i in self.inf_list:
                print(i.to_str())

    def simplify_inf_list(self, debug=False):
        self.simplified_inf_list.clear()
        if len(self.inf_list) <= 1:  # 若只有一条INF，则无需简化
            self.simplified_inf_list = self.inf_list
            return
        index = len(self.inf_list) - 1

        tmp = self.inf_list
        while index > 0:
            for i in range(index - 1, -1, -1):  # 从尾部扫描到头部
                # print('index: '+ str(index) + ', ' + 'i: ' + str(i))
                if tmp[index].equals(tmp[i]) and index != i:  # 若相同，保留数字小的，比如"001""111"保留前者
                    smaller_one = tmp[index].a
                    bigger_one = tmp[i].a
                    if int(tmp[index].a) > int(tmp[i].a):
                        smaller_one = tmp[i].a
                        bigger_one = tmp[index].a
                        tmp.remove(tmp[index])
                    else:
                        tmp.remove(tmp[i])
                    for each in tmp:
                        if each.b1 == bigger_one:
                            each.b1 = smaller_one
                        if each.b2 == bigger_one:
                            each.b2 = smaller_one
                    index -= 1  # 因为删去了一个，所以index减1
            index -= 1
        self.simplified_inf_list = tmp

        for inf in self.simplified_inf_list:
            self.simplified_inf_dict[inf.a] = inf

        if debug is True:
            print('简化后的INF:')
            for inf in self.simplified_inf_list:
                print(inf.to_str())

        # 从前向后再进行简化
        for index, inf in enumerate(self.simplified_inf_list):
            to_replace = ''
            replaced_by = ''
            if inf.b1 == inf.b2: # 高低端子节点相同
                to_replace = inf.a
                replaced_by = inf.b1
                self.simplified_inf_list.remove(inf)
            for j in range(index):
                tmp_inf = self.simplified_inf_list[j]
                if tmp_inf.b1 == to_replace:
                    tmp_inf.b1 = replaced_by
                if tmp_inf.b2 == to_replace:
                    tmp_inf.b2 = replaced_by

        if debug is True:
            print('简化后的INF:')
            for inf in self.simplified_inf_list:
                print(inf.to_str())


    # l = [ [a,next_var]|bool, [a,next_var]|bool]
    # 若为bool则表明该子节点为终端节点
    def create_inf_bfs(self, a='', current_var=None):
        l = [[a, current_var], [a, current_var]]
        branch = [a + '1', a + '0']
        for index, i in enumerate(branch):
            if len(i) == len(self.var_list):
                branch[index] = self.result_table[i]
            else:
                all = [j for j in self.result_table if j[:len(i)] == i]
                # 是否其余变量的所有取值对应的结果都相同
                if len(all):
                    flag = True
                    for other in all:
                        if self.result_table[other] != self.result_table[all[0]]:
                            flag = False
                    if flag:
                        branch[index] = self.result_table[all[0]]
        inf = INFExpr(a=a, current_var=current_var,
                      b1=branch[0], b2=branch[1])
        self.inf_list.append(inf)

        if len(a) == len(self.var_list) - 1:
            return [branch[0], branch[1]]

        next_var = ''
        for index, var in enumerate(self.var_list):
            if var == current_var and index < len(self.var_list) - 1:
                next_var = self.var_list[index + 1]

        l[0][0] = branch[0]
        l[0][1] = next_var
        l[1][0] = branch[1]
        l[1][1] = next_var

        if branch[0] is False or branch[0] is True:
            l[0] = branch[0]
        if branch[1] is False or branch[1] is True:
            l[1] = branch[1]
        return l

    # 对inf_list根据变量取值进行高亮
    def highlight_inf_and_node(self, variables=None):
        if len(self.simplified_inf_list) == 0:  # INF列表为空则退出
            return
        tmp_inf = self.simplified_inf_list[0]

        # 对高亮节点所在的式子进行高亮
        while True:
            tmp_inf.highlight()
            val = variables[tmp_inf.current_var]
            if isinstance(tmp_inf.b1, bool) and isinstance(tmp_inf.b2, bool):
                break
            if val is True:  # 指向b1
                if isinstance(tmp_inf.b1, bool):  # 若指向0或1的终端节点，则退出
                    break
                tmp_inf = self.simplified_inf_dict[tmp_inf.b1]
            elif val is False:  # 指向b2
                if isinstance(tmp_inf.b2, bool):  # 若指向0或1的终端节点，则退出
                    break
                tmp_inf = self.simplified_inf_dict[tmp_inf.b2]
            else:
                continue
        for i in self.simplified_inf_list:
            if i.is_highlighted:
                this_node = self.obdd_node[i.current_var][i.index]  # 找出当前节点
                this_node.highlight()

                # 如果指向尾端0或1节点，对其进行高亮
                if variables[i.current_var]:  # 指向b1
                    if isinstance(i.b1, bool):
                        self.obdd_node[str(int(i.b1))][0].highlight()
                elif variables[i.current_var] is False:  # 指向b2
                    if isinstance(i.b2, bool):
                        self.obdd_node[str(int(i.b2))][0].highlight()
                else:
                    continue

if __name__ == '__main__':
    b = BoolExprToInf(bool_expr='(x1<=>y1)∧(x2<=>y2)',
                      var_list=['x1','y1','x2','y2'],
                      variables={
                          'x1':False,
                          'y1':False,
                          'x2':False,
                          'y2':False
                      })
    inf_list = b.get_inf_list()
    for i in inf_list:
        print(i.to_str())
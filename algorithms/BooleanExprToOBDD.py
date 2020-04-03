from ParsingUtility import *
import queue
from painter import *

class Obj:
    def __init__(self,a,current_var,node):
        self.a = a
        self.current_var = current_var
        self.node = node

class BoolExprToINF:

    variables = {}
    var_list = []
    result_table = {}
    bool_expr = ''

    inf_list = []
    decision_tree = None
    simplified_inf_list = []
    obdd_tree = None

    def __init__(self, canvas=None, var_list=None,
                 default_var='t', bool_expr='',
                 variables=None):
        self.canvas = canvas
        self.var_list = var_list
        self.variables = variables
        self.default_var = default_var
        self.bool_expr = bool_expr

        self.p = ParsingUtility()
        self.generate_result_table() # 得到真值表
        print('真值表：')
        print(self.result_table)

        self.generate_inf_list() # 得到INF，并画决策树
        self.simplify_inf_list() # 简化后的INF

    # 生成INF范式 （目前画决策树的部分也在此）
    def generate_inf_list(self):
        self.inf_list.clear()
        decay = 10
        root_node = Node(canvas=self.canvas, center=[250,30],
                         text=self.var_list[0],
                         d=60, h=60)
        print("INF范式：")
        q = queue.Queue()
        init_obj = Obj(a='',current_var=self.var_list[0],node=root_node)
        q.put(init_obj)
        while not q.empty():
            cur_obj = q.get()
            l = self.create_inf_bfs(a=cur_obj.a,current_var=cur_obj.current_var)
            print(l)
            #len(l) 说明两子节点都非终端节点，若l[0]l[1]都为bool则都为终端节点
            if len(l):
                # '1' right
                if l[0] is not False and l[0] is not True:
                    cur_obj.node.create_child_node(direc='right',text=l[0][1],
                                                    decay=decay)
                    child_node = cur_obj.node.right_child
                    obj = Obj(a=l[0][0],current_var=l[0][1],node=child_node)
                    q.put(obj)
                else:
                    cur_obj.node.create_child_node(direc='right', text=str(int(l[0])),
                                                   decay=decay, isLeaf=True)
                # '0' left
                if l[1] is not False and l[1] is not True:
                    cur_obj.node.create_child_node(direc='left', text=l[1][1],
                                                    decay=decay)
                    child_node = cur_obj.node.left_child
                    obj = Obj(a=l[1][0], current_var=l[1][1],node=child_node)
                    q.put(obj)
                else:
                    cur_obj.node.create_child_node(direc='left', text=str(int(l[1])),
                                                   decay=decay, isLeaf=True)
        print('INF:')
        for inf in self.inf_list:
            print(inf.to_str())

        self.decision_tree = Tree(root_node=root_node)
        self.decision_tree.draw()
        #print("---DFS:---")
        #self.create_inf_dfs(a='',current_var=self.var_list[0])

    def simplify_inf_list(self):
        self.simplified_inf_list.clear()
        if len(self.inf_list) <= 1:
            self.simplified_inf_list = self.inf_list
            return
        index = len(self.inf_list) - 1

        tmp = self.inf_list
        while index > 0: 
            for i in range(index-1, -1, -1):# 从尾部扫描到头部
                print('index: '+ str(index) + ', ' + 'i: ' + str(i))
                if tmp[index].equals(tmp[i]) and index!=i: # 若相同，保留数字小的，比如"001""111"保留前者
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
                    index -= 1 # 因为删去了一个，所以index减1
            index -= 1
        self.simplified_inf_list = tmp

        print('简化后的INF:')
        for inf in self.simplified_inf_list:
            print(inf.to_str())

    # l = [ [a,next_var]|bool, [a,next_var]|bool]
    # 若为bool则表明该子节点为终端节点
    def create_inf_bfs(self, a='', current_var=None):
        l = [[a,current_var],[a,current_var]]
        branch = [a+'1',a+'0']
        for index, i in enumerate(branch):
            if len(i) == len(self.var_list):
                branch[index] = self.result_table[i]
            else:
                all = [j for j in self.result_table if j[:len(i)] == i]
                #是否其余变量的所有取值对应的结果都相同
                if len(all):
                    flag = True
                    for other in all:
                        if self.result_table[other] != self.result_table[all[0]]:
                            flag = False
                    if flag:
                        branch[index] = self.result_table[all[0]]
        inf = INFExpr(a=a,current_var=current_var,
                      b1=branch[0],b2=branch[1])
        self.inf_list.append(inf)

        if len(a) == len(self.var_list)-1:
            return [branch[0], branch[1]]

        next_var = ''
        for index, var in enumerate(self.var_list):
            if var == current_var and index<len(self.var_list)-1:
                next_var = self.var_list[index+1]

        l[0][0] = branch[0]
        l[0][1] = next_var
        l[1][0] = branch[1]
        l[1][1] = next_var


        if branch[0] is False or branch[0] is True:
            l[0] = branch[0]
        if branch[1] is False or branch[1] is True:
            l[1] = branch[1]
        return l

    def create_inf_dfs(self, a='', current_var=None):
        branch = [a+'1',a+'0']
        for index, i in enumerate(branch):
            if len(i) == len(self.var_list):
                branch[index] = self.result_table[i]
            else:
                all = [j for j in self.result_table if j[:len(i)] == i]
                #是否其余变量的所有取值对应的结果都相同
                if len(all):
                    flag = True
                    for other in all:
                        if self.result_table[other] != self.result_table[all[0]]:
                            flag = False
                    if flag:
                        i = self.result_table[all[0]]
        inf = INFExpr(a=a,current_var=current_var,
                      b1=branch[0],b2=branch[1])
        self.inf_list.append(inf)

        if len(a) == len(self.var_list)-1:
            return

        next_var = ''
        for index, var in enumerate(self.var_list):
            if var == current_var and index<len(self.var_list)-1:
                next_var = self.var_list[index+1]

        if branch[0] is not False and branch[0] is not True:
            self.create_inf_dfs(a=branch[0],current_var=next_var)
        if branch[1] is not False and branch[1] is not True:
            self.create_inf_dfs(a=branch[1],current_var=next_var)




    # '{'x1'=1,x2=0'}' <==> '10'
    def dict_to_str(self, variables):
        s = ''
        for i in variables:
            s += str(int(variables[i]))
        return s

    # '10' <==> '{'x1'=1,'x2'=0}'
    def str_to_dict(self, str):
        variables = {}
        if len(str)==len(self.var_list):
            for index, ch in enumerate(str):
                variables[self.var_list[index]] = int(ch)
        return variables


    # 6 => '110'
    def num_to_str(self, num):
        l = len(self.var_list)
        return str(bin(num).zfill(l+2)).replace('b', '')[1:]

    # 2 => '{'x1'=1,'x2'=0}'
    def num_to_dict(self, num):
        s = self.num_to_str(num)
        return self.str_to_dict(s)


    def generate_result_table(self):
        l = len(self.var_list)
        for i in range(2**l):
            variables = self.num_to_dict(i)
            result = self.p.get_parse_result(text=self.bool_expr, variables=variables)
            self.result_table[self.num_to_str(i)] = result


class INFExpr:

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

    def to_str(self):
        s = self.t + self.a + ' = ' + self.current_var + ' -> '
        if isinstance(self.b1,bool):
            s += str(int(self.b1))
        else:
            s += 't' + self.b1

        s += ','

        if isinstance(self.b2,bool):
            s += str(int(self.b2))
        else:
            s += 't' + self.b2
        return s

    def equals(self, inf_expr):
        if self.current_var == inf_expr.current_var and self.b1 == inf_expr.b1 and self.b2 == inf_expr.b2:
            return True
        else:
            return False


if __name__ == '__main__':
    inf = INFExpr(current_var='x1',b1='1',b2='0')
    inf.a='000'
    inff = INFExpr(current_var='x1',b1='1',b2='0')
    inff.a = '111'
    print(inf.equals(inff))
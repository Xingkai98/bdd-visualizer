from antlr_facility import *
import queue
from graph_node import *
from bool_expr_to_inf import BoolExprToInf
from bdd import BDD


class INFToBDD:
    __var_to_node = {}
    __a_to_node = {}

    def get_bdd(self,
                canvas=None,
                root_center=None,            # 起始变量的坐标
                h=60,            # 变量间竖直距离
                w=40,          # 每行变量的横向距离
                var_list=None,
                inf_list=None,
                inf_dict=None,
                debug=False):
        self.__var_to_node.clear()
        self.__a_to_node.clear()

        for var in var_list:
            self.__var_to_node[var] = []

        pre_var_num = 0
        # 确定节点的位置
        for index, var in enumerate(var_list): # 遍历每个变量
            var_num = 0   # 暂存每行变量的数量
            for inf in inf_list:
                cur_var = inf.current_var
                if cur_var == var:   # 找到当前变量
                    inf.index = var_num
                    var_num += 1

            pre_var_num = var_num
            #print(var + ': ' + str(var_num))
            coord_list = []  # 暂存每行节点的中心位置（从右到左）
            y = root_center[1] + index * h
            root_x = root_center[0]
            if var_num == 1:  # 一个变量
                tune = 0
                if pre_var_num == 1: # 若这个变量和上一个变量都只有一个节点，就需要调整x坐标避免同线
                    if index % 2 == 1:
                        tune = w
                coord_list.append((root_x+tune,y))
                self.__var_to_node[var] = [Node(canvas=canvas,
                                            center=(root_x+tune,y),
                                            text=var)] # 生成节点列表
                continue
            if var_num % 2:  # 奇数个变量
                start = int(root_x + var_num // 2 * w * 2)
                end = int(root_x - (var_num // 2 + 1) * w * 2)
                step = -int(w * 2)
                for x in range(start,end,step):
                    coord_list.append((x,y))
                    self.__var_to_node[var].append(Node(canvas=canvas,
                                                    center=(x, y),
                                                    text=var)) # append入节点列表

            else:            # 偶数个变量
                start = int(root_x + (var_num - 1) * w)
                end = int(root_x - (var_num - 1) * w - 2 * w)
                step = -int(w * 2)
                for x in range(start,end,step):
                    coord_list.append((x,y))
                    self.__var_to_node[var].append(Node(canvas=canvas,
                                                    center=(x, y),
                                                    text=var)) # append入节点列表

        terminal_y = int(root_center[1] + len(var_list) * h) # 终端节点坐标的y值
        self.__var_to_node['0'] = [LeafNode(canvas=canvas,
                                        center=(int(root_center[0] - w * 1.5), terminal_y),
                                        text='0')]
        self.__var_to_node['1'] = [LeafNode(canvas=canvas,
                                        center=(int(root_center[0] + w * 1.5), terminal_y),
                                        text='1')]

        if debug is True:
            for var in self.__var_to_node:
                print(var)
                node_list = self.__var_to_node[var]
                for node in node_list:
                    print(node.center)
        
        bdd = BDD(var_to_node=self.__var_to_node,
                  a_to_node=self.__a_to_node,
                  root_center=root_center,
                  inf_list=inf_list,
                  inf_dict=inf_dict,
                  root_node=self.__var_to_node[inf_list[0].current_var][0])
        return bdd
        

if __name__ == '__main__':
    bf = BoolExprToInf(bool_expr='(x1<=>y1)∧(x2<=>y2)',
                      var_list=['x1', 'y1', 'x2', 'y2'],
                      variables={
                          'x1': False,
                          'y1': False,
                          'x2': False,
                          'y2': False
                      },
                      root_center=(500, 30))
    inf_list = bf.get_inf_list()
    inf_dict = bf.get_inf_dict()
    ib = INFToBDD()
    ib.get_bdd(var_list=['x1','y1','x2','y2'],
               inf_list=inf_list,
               inf_dict=inf_dict,
               debug=True,
               root_center=(500, 30))
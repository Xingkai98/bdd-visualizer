from graph_node import *


class BDD:
    __var_to_node = {}
    __a_to_node = {}
    __root_center = []

    def __init__(self, var_to_node, a_to_node, root_center):
        self.__var_to_node = var_to_node
        self.__a_to_node = a_to_node
        self.__root_center = root_center

    def set_var_to_node(self, var_to_node):
        self.__var_to_node = var_to_node

    def get_var_to_node(self):
        return self.__var_to_node

    def set_a_to_node(self, a_to_node):
        self.__a_to_node = a_to_node

    def get_a_to_node(self):
        return self.__a_to_node

    def paint(self, canvas=None,
              inf_list=None,
              inf_dict=None,
              h=60,  # 变量间竖直距离
              w=40,  # 每行变量的横向距离
              highlight=False,  # 是否高亮，若高亮则需用到variables
              var_list=None,
              variables=None,
              debug=False):
        self.__var_to_node.clear()
        self.__a_to_node.clear()

        if variables and len(variables):  # 更新变量取值以便高亮
            self.variables = variables

        for var in var_list:
            self.__var_to_node[var] = []

        # 确定节点的位置
        for index, var in enumerate(var_list):  # 遍历每行变量
            var_num = 0  # 暂存每行变量的数量
            for inf in inf_list:
                cur_var = inf.current_var
                if cur_var == var:  # 找到当前变量
                    inf.index = var_num
                    var_num += 1
            # print(var + ': ' + str(var_num))
            coord_list = []  # 暂存每行节点的中心位置（从右到左）
            y = self.__root_center[1] + index * h
            root_x = self.__root_center[0]
            if var_num == 1:  # 一个变量
                coord_list.append((root_x, y))
                self.__var_to_node[var] = [Node(canvas=canvas,
                                            center=(root_x, y),
                                            text=var)]  # 生成节点列表
                continue
            if var_num % 2:  # 奇数个变量
                start = int(root_x + var_num // 2 * w * 2)
                end = int(root_x - (var_num // 2 + 1) * w * 2)
                step = -int(w * 2)
                for x in range(start, end, step):
                    coord_list.append((x, y))
                    self.__var_to_node[var].append(Node(canvas=canvas,
                                                    center=(x, y),
                                                    text=var))  # append入节点列表

            else:  # 偶数个变量
                start = int(root_x + (var_num - 1) * w)
                end = int(root_x - (var_num - 1) * w - 2 * w)
                step = -int(w * 2)
                for x in range(start, end, step):
                    coord_list.append((x, y))
                    self.__var_to_node[var].append(Node(canvas=canvas,
                                                    center=(x, y),
                                                    text=var))  # append入节点列表

        terminal_y = int(self.__root_center[1] + len(var_list) * h)  # 终端节点坐标的y值
        self.__var_to_node['0'] = [LeafNode(canvas=canvas,
                                        center=(int(self.__root_center[0] - w * 1.5), terminal_y),
                                        text='0')]
        self.__var_to_node['1'] = [LeafNode(canvas=canvas,
                                        center=(int(self.__root_center[0] + w * 1.5), terminal_y),
                                        text='1')]

        if debug is True:
            for var in self.__var_to_node:
                print(var)
                node_list = self.__var_to_node[var]
                for node in node_list:
                    print(node.center)

        # 根据现有变量取值对路径进行高亮
        # self.highlight_inf_and_node(variables=variables)

        # 对于INF中的每一条，画OBDD节点之间的连线
        for inf in inf_list:
            start_node = self.__var_to_node[inf.current_var][inf.index]  # 找出起点位置

            # 找出终点位置（高端）
            if inf.b1 == False:
                b1_node = self.__var_to_node['0'][0]
            elif inf.b1 == True:
                b1_node = self.__var_to_node['1'][0]
            else:
                b1_varname = inf_dict[inf.b1].current_var  # 变量名
                b1_index = inf_dict[inf.b1].index  # 顺序
                b1_node = self.__var_to_node[b1_varname][b1_index]  # 获取节点

            # 找出终点位置（低端）
            if inf.b2 == False:
                b2_node = self.__var_to_node['0'][0]
            elif inf.b2 == True:
                b2_node = self.__var_to_node['1'][0]
            else:
                b2_varname = inf_dict[inf.b2].current_var
                b2_index = inf_dict[inf.b2].index
                b2_node = self.__var_to_node[b2_varname][b2_index]

            # 画线
            start_node.draw_line_towards(node=b1_node, isDashed=False)
            start_node.draw_line_towards(node=b2_node, isDashed=True)

        # 画OBDD节点
        for var in self.__var_to_node:
            node_list = self.__var_to_node[var]
            for node in node_list:
                node.draw_center()
                print(node.text + ' ' + str(node.is_highlighted))

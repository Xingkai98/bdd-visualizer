from graph_node import *

# 二元决策图类
class BDD:
    __var_to_node = {}
    __a_to_node = {}
    __root_center = []
    __root_node = None

    def __init__(self, var_to_node,
                       a_to_node,
                       root_center,
                       inf_list,
                       inf_dict,
                       root_node):
        self.__var_to_node = var_to_node  # 变量-节点位置列表的词典
        self.__a_to_node = a_to_node
        self.__root_center = root_center
        self.__inf_list = inf_list  # INF列表
        self.__inf_dict = inf_dict
        self.__root_node = root_node  # 跟节点

        for inf in inf_list:
            start_node = self.__var_to_node[inf.current_var][inf.index]  # 找出起点位置

            # 找出终点位置（高端）
            if inf.b1 is False:
                b1_node = self.__var_to_node['0'][0]
            elif inf.b1 is True:
                b1_node = self.__var_to_node['1'][0]
            else:
                b1_varname = inf_dict[inf.b1].current_var  # 变量名
                b1_index = inf_dict[inf.b1].index  # 顺序
                b1_node = self.__var_to_node[b1_varname][b1_index]  # 获取节点
            start_node.high_child = b1_node

            # 找出终点位置（低端）
            if inf.b2 is False:
                b2_node = self.__var_to_node['0'][0]
            elif inf.b2 is True:
                b2_node = self.__var_to_node['1'][0]
            else:
                b2_varname = inf_dict[inf.b2].current_var
                b2_index = inf_dict[inf.b2].index
                b2_node = self.__var_to_node[b2_varname][b2_index]
            start_node.low_child = b2_node

    def set_root_node(self, root_node):
        self.__root_node = root_node

    def get_root_node(self):
        return self.__root_node

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
                  highlight=False,  # 是否高亮，若高亮则需用到variables，即各变量取值
                  var_list=None,
                  variables=None,
                  debug=False):

        if variables and len(variables):  # 更新变量取值以便高亮
            self.variables = variables

        self.sub_paint(self.__root_node)

        # 画BDD节点
        for var in self.__var_to_node:
            node_list = self.__var_to_node[var]
            for node in node_list:
                node.draw_center()

    # 递归调用
    def sub_paint(self, node):
        if isinstance(node, LeafNode):
            return
        if node.is_low_edge_highlighted:
            node.draw_line_towards(node=node.low_child,
                                   isDashed=True,
                                   highlight=True)
        else:
            node.draw_line_towards(node=node.low_child,
                                   isDashed=True,
                                   highlight=False)
        self.sub_paint(node.low_child)

        if node.is_high_edge_highlighted:
            node.draw_line_towards(node=node.high_child,
                                   isDashed=False,
                                   highlight=True)
        else:
            node.draw_line_towards(node=node.high_child,
                                   isDashed=False,
                                   highlight=False)
        self.sub_paint(node.high_child)
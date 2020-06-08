from bool_expr_to_inf import *
from inf_to_bdd import *

# 绘制决策图的Frame
class ImgFrame(Frame):

    r = 15
    dash = (4,4)

    def __init__(self, root_frame,
                 expr=None,
                 var_list=None,
                 root_frame_geometry=None,
                 variables=None,
                 h=60,  # 默认节点间高度
                 w=40):  # 默认节点间宽度
        super().__init__(root_frame)
        self.expr = expr
        self.var_list = var_list
        self.variables = variables
        self.root_frame_geometry = root_frame_geometry
        self.root_center = (int(self.root_frame_geometry[0] / 2), 30)
        self.canvas = Canvas(self)
        self.bdd = None
        self.inf_list = []
        self.var_to_node = {}
        self.h = h
        self.w = w
        self.get_bdd()

    def get_bdd(self):  # 生成INF和BDD
        bool_to_inf = BoolExprToInf(canvas=self.canvas,
                                    bool_expr=self.expr,
                                    var_list=self.var_list,
                                    variables=self.variables,
                                    root_center=self.root_center)
        self.inf_list = bool_to_inf.get_inf_list(debug=True)
        self.inf_dict = bool_to_inf.simplified_inf_dict

        ib = INFToBDD()
        self.bdd = ib.get_bdd(var_list=self.var_list,
                              inf_list=self.inf_list,
                              inf_dict=self.inf_dict,
                              debug=False,
                              root_center=self.root_center,
                              h=self.h,
                              w=self.w,
                              canvas=self.canvas)
        self.var_to_node = self.bdd.get_var_to_node()

    def draw(self, highlight=False):
        self.pack(fill=BOTH, expand=1)
        if self.bdd:
            if highlight:
                self.highlight_node(variables=self.variables)
            self.bdd.paint(canvas=self.canvas,
                          inf_list=self.inf_list,
                          inf_dict=self.inf_dict,
                          var_list=self.var_list,
                          variables=self.variables,
                          debug=False)

        self.canvas.pack(fill=BOTH, expand=1)

    def highlight_node(self, variables=None):
        self.sub_highlight_node(self.bdd.get_root_node(),self.variables)

    def sub_highlight_node(self, node, variables):
        node.highlight()
        if isinstance(node, LeafNode):
            return
        if node.text in variables:
            if variables[node.text] is True:
                node.highlight_high_edge()
                self.sub_highlight_node(node=node.high_child,variables=variables)
            else:
                node.highlight_low_edge()
                self.sub_highlight_node(node=node.low_child,variables=variables)

    def highlight_inf_and_node(self, variables=None):
        if len(self.inf_list) == 0: # INF列表为空则退出
            return
        tmp_inf = self.inf_list[0]

        # 对高亮节点所在的式子进行高亮
        while True:
            tmp_inf.highlight()
            val = variables[tmp_inf.current_var]
            if isinstance(tmp_inf.b1, bool) and isinstance(tmp_inf.b2, bool):
                break
            if val is True:  # 指向b1
                if isinstance(tmp_inf.b1, bool):  # 若指向0或1的终端节点，则退出
                    break
                tmp_inf = self.inf_dict[tmp_inf.b1]
            elif val is False:  # 指向b2
                if isinstance(tmp_inf.b2, bool):  # 若指向0或1的终端节点，则退出
                    break
                tmp_inf = self.inf_dict[tmp_inf.b2]
            else:
                continue
        for i in self.inf_list:
            if i.is_highlighted:
                this_node = self.var_to_node[i.current_var][i.index]  # 找出当前节点
                this_node.highlight()

                # 如果指向尾端0或1节点，对其进行高亮
                if variables[i.current_var]:  # 指向b1
                    if isinstance(i.b1, bool):
                        self.var_to_node[str(int(i.b1))][0].highlight()
                elif variables[i.current_var] is False:  # 指向b2
                    if isinstance(i.b2, bool):
                        self.var_to_node[str(int(i.b2))][0].highlight()
                else:
                    continue
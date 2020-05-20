from bool_expr_to_bdd import *
from bool_expr_to_inf import *
from inf_to_bdd import *

class ImgFrame(Frame):

    d = 70
    h = 40
    r = 15
    dash = (4,4)

    def __init__(self, root_frame,
                 expr=None,
                 var_list=None,
                 root_frame_geometry=None,
                 variables=None):
        super().__init__(root_frame)
        self.expr = expr
        self.var_list = var_list
        self.variables = variables
        self.root_frame_geometry = root_frame_geometry
        self.root_center = (int(self.root_frame_geometry[0] / 2), 30)
        self.canvas = Canvas(self)

    def draw(self):
        self.pack(fill=BOTH, expand=1)

        # 生成INF和BDD
        bool_to_inf = BoolExprToInf(canvas=self.canvas,
                                    bool_expr=self.expr,
                                    var_list=self.var_list,
                                    variables=self.variables,
                                    root_center=self.root_center)
        il = bool_to_inf.get_inf_list(debug=True)
        idict = bool_to_inf.simplified_inf_dict
        for each in il:
            print(each.to_str())
        ib = INFToBDD()
        bdd = ib.get_bdd(var_list=self.var_list,
                         inf_list=il,
                         debug=True,
                         root_center=self.root_center,
                         canvas=self.canvas)
        bdd.paint(canvas=self.canvas,
                  inf_list=il,
                  inf_dict=idict,
                  h=60,  # 变量间竖直距离
                  w=40,  # 每行变量的横向距离
                  highlight=False,  # 是否高亮，若高亮则需用到variables
                  var_list=self.var_list,
                  variables=self.variables,
                  debug=False)

        #生成INF和BDD
        '''
        bool_to_obdd = BoolExprToOBDD(canvas=self.canvas,
                                      bool_expr=self.expr,
                                      var_list=self.var_list,
                                      root_center=self.root_center)
        bool_to_obdd.generate_inf(generate_decision_tree=True,
                                  debug=True)
        #画BDD
        bool_to_obdd.draw_obdd(root_center=self.root_center,
                               highlight=True,
                               variables=self.variables)
        '''

        self.canvas.pack(fill=BOTH, expand=1)

    def highlight_inf_and_node(self, variables=None):
        print(variables)
        if len(self.simplified_inf_list) == 0: # INF列表为空则退出
            return
        tmp_inf = self.simplified_inf_list[0]

        # 对高亮节点所在的式子进行高亮
        while True:
            tmp_inf.highlight()
            print(tmp_inf.current_var + ' highlighted.')
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
                this_node = self.__bdd_node[i.current_var][i.index]  # 找出当前节点
                this_node.highlight()
                print(this_node.text + ' index: ' + str(i.index) + ' highlighted.')

                # 如果指向尾端0或1节点，对其进行高亮
                if variables[i.current_var]:  # 指向b1
                    if isinstance(i.b1, bool):
                        self.__bdd_node[str(int(i.b1))][0].highlight()
                elif variables[i.current_var] is False:  # 指向b2
                    if isinstance(i.b2, bool):
                        self.__bdd_node[str(int(i.b2))][0].highlight()
                else:
                    continue

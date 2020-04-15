import tkinter as tk
import tkinter.messagebox as msgbox
from ParsingUtility import ParsingUtility
import sys
from antlr4 import InputStream
from img_frame import ImgFrame
from bool_expr_to_obdd import *
from list_permuter import *

class BddDemo(tk.Tk):

    variables = {}
    var_list = []
    expr = ''
    width = 1024
    height = 768
    img = None
    p = ParsingUtility()

    def __init__(self, vars=None):
        super().__init__()
        if not vars:
            self.vars = []
        else:
            self.vars = vars

        self.title("BDD")
        self.geometry(str(self.width) + "x" + str(self.height))

        self.expr_label = tk.Label(self, text="Default", bg="lightgrey", fg="black",
                         pady=10)
        self.var_sequence_label = tk.Label(self, text="变量顺序： ", bg="lightgrey", fg="black",
                                   pady=10)

        self.vars.append(self.expr_label)
        self.vars.append(self.var_sequence_label)

        for task in self.vars:
            task.pack(side=tk.TOP, fill=tk.X)

        # 输入框
        self.text_input = tk.Text(self, height=3)
        self.text_input.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_input.focus_set()

        self.update_expr_button = tk.Button(self, text='更新表达式', command=self.update_expr)
        self.update_expr_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.set_variable_value_button = tk.Button(self, text='变量赋值', command=self.set_variable_value)
        self.set_variable_value_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.set_variable_seq_button = tk.Button(self, text='更新变量顺序', command=self.set_variable_seq)
        self.set_variable_seq_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.set_variable_seq_button = tk.Button(self, text='更新变量顺序为最简', command=self.set_variable_seq_as_optimal)
        self.set_variable_seq_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

    # 更新命题取值
    def set_variable_value(self, event=None):
        var_text = str(self.text_input.get(1.0, tk.END).strip())

        if len(var_text) > 0 and '=' in var_text:
            pass
            # new_var = tk.Label(self, text=var_text, pady=10)
        else:
            msgbox.showwarning('提示','请输入变量赋值语句。')
            return

        var_assign_expr_list = var_text.split(',')
        for var_assign_expr in var_assign_expr_list:
            var = var_assign_expr.split('=')
            var_name = var[0]
            var_value = var[1]
            if var_name in self.variables:
                self.variables[var_name] = bool(int(var_value))
            else:
                msgbox.showerror('错误', '变量不存在。')
                return
            if var_value != '0' and var_value!='1':
                msgbox.showerror('错误', '请将变量赋值为0或1。')
                return
        new_result = self.p.get_parse_result(text=self.expr, variables=self.variables)
        self.expr_label["text"] = self.expr + ': ' + str(new_result)

    # 更新命题顺序并重画
    def set_variable_seq(self,event=None):
        variables = {}
        var_list = []
        var_text = str(self.text_input.get(1.0, tk.END).strip())
        for var in var_text.split(','):
            if var in self.variables:
                variables[var] = self.variables[var]
                var_list.append(var)
            else:
                msgbox.showerror('错误', str(var) + '变量不存在。')
                return
        self.variables = variables
        self.var_list = var_list

        self.var_sequence_label["text"] = '变量顺序： '
        for var in self.var_list:
            self.var_sequence_label["text"] += str(var) + ', '

        self.update_image()

    # 更新命题顺序为复杂度最低的OBDD并重画
    def set_variable_seq_as_optimal(self):
        lp = ListPermuter()
        var_list_permuted = lp.permute(self.var_list)

        smallest_num = -1
        result = var_list_permuted[0]

        for var_list in var_list_permuted:
            bool_to_obdd = BoolExprToOBDD(bool_expr=self.expr,
                                          var_list=var_list,
                                          variables=self.variables)
            bool_to_obdd.generate_inf(generate_decision_tree=False,
                                      debug=True)
            node_num = bool_to_obdd.get_obdd_node_num()
            if smallest_num < 0:
                smallest_num = node_num
            if node_num < smallest_num:
                smallest_num = node_num
                result = var_list
            print(var_list)
            print(str(node_num))
        print('最简变量顺序:')
        print(result)
        print(str(smallest_num))
        self.var_list = result
        self.update_var_seq_text()
        self.update_image(text=self.expr)


    # 更新表达式并重新画图
    def update_expr(self, event=None):

        text = str(self.text_input.get(1.0, tk.END).strip())
        self.expr = text

        # 每次需要从表达式中更新命题
        self.var_list = self.p.get_variable_list(text=text)
        self.var_sequence_label["text"] = '变量顺序： '
        for var in self.var_list:
            self.variables[var] = False
            self.var_sequence_label["text"] += str(var) + ', '

        self.var_sequence_label["text"] = self.var_sequence_label["text"][:-2]
        self.expr_label["text"] = text

        self.update_image(text=text)

    # 根据当前的命题顺序改变显示的文字
    def update_var_seq_text(self):
        self.var_sequence_label["text"] = '变量顺序： '
        for var in self.var_list:
            self.var_sequence_label["text"] += str(var) + ', '
        self.var_sequence_label["text"] = self.var_sequence_label["text"][:-2]

    # 根据当前的表达式和命题顺序画图
    def update_image(self, text=None):
        expr = self.expr
        if text:
            expr = text
        if expr != '':
            if self.img:
                self.img.pack_forget()
            self.img = ImgFrame(expr=expr, var_list=self.var_list,
                                root_frame_geometry=[self.width, self.height],
                                variables=self.variables)
            self.img.draw()
            self.img.pack()
        else:
            msgbox.showerror('错误','输入不能为空。')
            return


if __name__ == "__main__":
    bdd = BddDemo()
    bdd.mainloop()

import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import *
from img_frame import ImgFrame
from bool_expr_to_bdd import *
from list_permuter import *
from functools import partial

class MainFrame(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("二元决策图图形展示工具")
        self.__variables = {}
        self.__var_list = []
        self.__expr = ''
        self.__img_frame = None
        self.__var_frame = [] # 变量Frame列表
        self.__antlr_facility = AntlrFacility()
        self.width = 1024
        self.height = 768
        self.geometry(str(self.width) + "x" + str(self.height))

        self.__left_frame = Frame(self, bg='grey', width=self.width/4, height=self.height)
        self.__mid_frame = Frame(self, width=self.width/2, height=self.height)
        self.__right_frame = Frame(self, width=self.width/4, height=self.height)

        # left_frame
        # TODO：变量列表，能够设置取值和顺序
        self.import_button = tk.Button(self.__left_frame, text='导入')
        self.import_button.pack(side=tk.TOP, fill=BOTH)

        self.save_button = tk.Button(self.__left_frame, text='保存')
        self.save_button.pack(side=tk.TOP, fill=BOTH)

        # 输入表达式的确定按钮
        self.update_expr_button = tk.Button(self.__left_frame, text='确定', command=self.update_expr)
        self.update_expr_button.pack(side=tk.BOTTOM, fill=BOTH)

        # 输入框
        self.text_input = tk.Text(self.__left_frame, height=2,width=40, highlightbackground='grey')
        self.text_input.pack(side=tk.BOTTOM, fill=BOTH)
        self.text_input.focus_set()

        self.update_expr_label = tk.Label(self.__left_frame, text="输入表达式", bg="white", fg="black")
        self.update_expr_label.pack(side=tk.BOTTOM, fill=BOTH)

        self.var_list_label = tk.Label(self.__left_frame, text="变量列表", bg="grey", fg="black")
        self.var_list_label.pack(side=tk.TOP, fill=BOTH)

        # mid_frame
        self.save_pic_button = tk.Button(self.__mid_frame, text='保存为图片',width=70)
        self.save_pic_button.pack(side=tk.BOTTOM, fill=BOTH)

        # right_frame
        # TODO:单位宽度、高度，是否高亮，是否展示inf
        self.save_params_button = tk.Button(self.__right_frame, text='保存参数',width=25)
        self.save_params_button.pack(side=tk.BOTTOM, fill=BOTH)

        self.set_param_label = tk.Label(self.__right_frame, text="参数设置", bg="white", fg="black")
        self.set_param_label.pack(side=tk.TOP, fill=BOTH)

        # 设置宽
        self.width_param_frame = tk.Frame(self.__right_frame, highlightcolor='grey')
        tk.Label(self.width_param_frame, text="设置单位宽度", fg="black").pack(side=tk.LEFT, fill=BOTH)
        tk.Text(self.width_param_frame, bd=1, height=1, width=20, highlightbackground='grey').pack(side=tk.LEFT)

        # 设置高
        self.height_param_frame = tk.Frame(self.__right_frame, highlightcolor='grey')
        tk.Label(self.height_param_frame, text="设置单位高度", fg="black").pack(side=tk.LEFT, fill=BOTH)
        tk.Text(self.height_param_frame, bd=1, height=1, width=20, highlightbackground='grey').pack(side=tk.LEFT)

        # 设置是否高亮
        self.highlight_param_frame = tk.Frame(self.__right_frame, highlightcolor='grey')
        t1 = tk.Checkbutton(self.highlight_param_frame)
        t1.pack(side=tk.LEFT)
        tk.Label(self.highlight_param_frame, text="是否高亮", fg="black").pack(side=tk.LEFT, fill=BOTH)

        # 设置是否展示INF
        self.inf_param_frame = tk.Frame(self.__right_frame, highlightcolor='grey')
        t2 = tk.Checkbutton(self.inf_param_frame)
        t2.pack(side=tk.LEFT)
        tk.Label(self.inf_param_frame, text="是否展示INF列表", fg="black").pack(side=tk.LEFT, fill=BOTH)

        self.width_param_frame.pack(side=TOP, fill=BOTH)
        self.height_param_frame.pack(side=TOP, fill=BOTH)
        self.highlight_param_frame.pack(side=TOP, fill=BOTH)
        self.inf_param_frame.pack(side=TOP, fill=BOTH)

        self.__left_frame.pack(side=LEFT, fill=BOTH)
        self.__right_frame.pack(side=RIGHT, fill=BOTH)
        self.__mid_frame.pack(side=LEFT, fill=BOTH)



    def get_variables(self):
        return self.__variables

    def get_var_list(self):
        return self.__var_list

    def get_expr(self):
        return self.__expr

    def move_var_up(self, var_name):
        index = 0  # 变量下标
        for i, var in enumerate(self.__var_list):
            if var == var_name:
                index = i
        if index == 0:
            return
        self.__var_list.remove(var_name)
        self.__var_list.insert(index-1,var_name)
        print(self.__var_list)
        self.repack_var()
        self.update_image()

    def move_var_down(self, var_name):
        index = 0   # 变量下标
        for i, var in enumerate(self.__var_list):
            if var == var_name:
                index = i
        if index == len(self.__var_list) - 1:
            return
        self.__var_list.remove(var_name)
        self.__var_list.insert(index + 1, var_name)
        print(self.__var_list)
        self.repack_var()
        self.update_image()

    def set_variable_value(self, name, value):
        if self.__variables[name]:
            self.__variables[name] = value

    def set_variable_seq(self, var_list):
        self.__var_list = var_list

    def set_seq_as_optimal(self):
        pass

    def set_expr(self, expr):
        self.__expr = expr

    def repack_var(self):
        # 清空变量Frame
        if len(self.__var_frame):
            for frame in self.__var_frame:
                frame.pack_forget()
        self.__var_frame.clear()
        for var in self.__var_list:

            frame = tk.Frame(self.__left_frame, highlightbackground='grey',highlightcolor='grey',highlightthickness=2)
            tmp_label = tk.Label(frame, text=var, bg="white", fg="black", bd=4)
            tmp_label.pack(side=tk.LEFT, fill=Y)

            move_down_button = tk.Button(frame, text='↓', command=partial(self.move_var_down, var))
            move_down_button.pack(side=tk.RIGHT, fill=BOTH)
            move_up_button = tk.Button(frame, text='↑', command=partial(self.move_var_up, var))
            move_up_button.pack(side=tk.RIGHT, fill=BOTH)
            true_button = tk.Button(frame, text='1')
            true_button.pack(side=tk.RIGHT, fill=BOTH)
            false_button = tk.Button(frame, text='0')
            false_button.pack(side=tk.RIGHT, fill=BOTH)

            self.__var_frame.append(frame)
            frame.pack(side=tk.TOP, fill=BOTH)

    def update_expr(self): # 根据表达式、是否高亮的参数更新变量列表、决策图图形
        text = str(self.text_input.get(1.0, tk.END).strip())
        if text == '':
            msgbox.showerror('错误', '请输入格式正确的表达式。')
            return
        text = text.replace('*', '∧')
        text = text.replace('+', '∨')
        text = text.replace('-', '¬')
        self.set_expr(text)

        # 从表达式中更新变量列表
        self.__var_list = self.__antlr_facility.get_variable_list(text=text)
        if len(self.__var_list) == 0:
            msgbox.showerror('错误', '请输入格式正确的表达式。')
            return
        self.__variables.clear()
        for var in self.__var_list:
            self.__variables[var] = False  # 默认设置每个变量的取值为False

        self.repack_var()
        self.update_image()

    def update_var_seq(self):
        pass

    def update_image(self):
        if self.__expr != '':
            if self.__img_frame:
                self.__img_frame.pack_forget()
            self.__img_frame = ImgFrame(root_frame=self.__mid_frame,
                                        expr=self.__expr,
                                        var_list=self.__var_list,
                                        root_frame_geometry=[self.width/2, self.height],
                                        variables=self.__variables)
            self.__img_frame.draw()
            self.__img_frame.pack()
        else:
            msgbox.showerror('错误','输入不能为空。')
            return


if __name__ == "__main__":
    main_frame = MainFrame()
    main_frame.mainloop()
import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import *
from img_frame import ImgFrame
from bool_expr_to_bdd import *
from list_permuter import *

class MainFrame(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("二元决策图图形展示工具")
        self.__variables = {}
        self.__var_list = []
        self.__expr = ''
        self.__img_frame = None
        self.__var_frame = None
        self.__antlr_facility = AntlrFacility()
        self.width = 1024
        self.height = 768
        self.geometry(str(self.width) + "x" + str(self.height))

        self.__left_frame = Frame(self, bg='grey', width=self.width/4, height=self.height)
        self.__mid_frame = Frame(self, width=self.width/2, height=self.height)
        self.__right_frame = Frame(self, bg='grey', width=self.width/4, height=self.height)

        # left_frame
        self.import_button = tk.Button(self.__left_frame, text='导入')
        self.import_button.pack(side=tk.TOP, fill=BOTH)

        self.save_button = tk.Button(self.__left_frame, text='保存')
        self.save_button.pack(side=tk.TOP, fill=BOTH)

        # 输入表达式的确定按钮
        self.update_expr_button = tk.Button(self.__left_frame, text='确定', command=self.update_expr)
        self.update_expr_button.pack(side=tk.BOTTOM, fill=BOTH)

        # 输入框
        self.text_input = tk.Text(self.__left_frame, height=2,width=40)
        self.text_input.pack(side=tk.BOTTOM, fill=BOTH)
        self.text_input.focus_set()

        self.update_expr_label = tk.Label(self.__left_frame, text="输入表达式", bg="white", fg="black")
        self.update_expr_label.pack(side=tk.BOTTOM, fill=BOTH)

        self.var_list_label = tk.Label(self.__left_frame, text="变量列表", bg="grey", fg="black")
        self.var_list_label.pack(side=tk.TOP, fill=BOTH)

        #mid_frame
        self.save_pic_button = tk.Button(self.__mid_frame, text='保存为图片',width=70)
        self.save_pic_button.pack(side=tk.BOTTOM, fill=BOTH)

        #right_frame
        self.save_params_button = tk.Button(self.__right_frame, text='保存参数',width=25)
        self.save_params_button.pack(side=tk.BOTTOM, fill=BOTH)

        self.set_param_label = tk.Label(self.__right_frame, text="参数设置", bg="white", fg="black")
        self.set_param_label.pack(side=tk.TOP, fill=BOTH)

        self.set_param_label = tk.Label(self.__right_frame, text="是否高亮", bg="grey", fg="black")
        self.set_param_label.pack(side=tk.TOP, fill=BOTH)

        self.__left_frame.pack(side=LEFT, fill=BOTH)
        self.__right_frame.pack(side=RIGHT, fill=BOTH)
        self.__mid_frame.pack(side=LEFT, fill=BOTH)



    def get_variables(self):
        return self.__variables

    def get_var_list(self):
        return self.__var_list

    def get_expr(self):
        return self.__expr

    def set_variable_value(self, name, value):
        pass

    def set_variable_seq(self, var_list):
        pass

    def set_seq_as_optimal(self):
        pass

    def set_expr(self, expr):
        self.__expr = expr

    def update_expr(self):
        text = str(self.text_input.get(1.0, tk.END).strip())
        self.set_expr(text)

        # 每次需要从表达式中更新命题
        self.__var_list = self.__antlr_facility.get_variable_list(text=text)
        self.__variables.clear()
        for var in self.__var_list:
            self.__variables[var] = False  # 默认设置每个变量的取值为False
            frame = tk.Frame(self.__left_frame, highlightcolor='grey')
            tmp_label = tk.Label(frame, text=var, bg="white", fg="black", bd=4)
            tmp_label.pack(side=tk.LEFT, fill=BOTH)
            frame.pack(side=tk.TOP, fill=BOTH)
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
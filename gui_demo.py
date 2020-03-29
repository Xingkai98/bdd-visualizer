import tkinter as tk
import tkinter.messagebox as msgbox
from ParsingUtility import ParsingUtility
import sys
from antlr4 import InputStream
from img_frame import ImgFrame

class BddDemo(tk.Tk):

    variables = {}
    var_list = []

    def __init__(self, vars=None):

        super().__init__()


        if not vars:
            self.vars = []
        else:
            self.vars = vars

        self.title("BDD")
        self.geometry("500x500")

        self.expr_label = tk.Label(self, text="Default", bg="lightgrey", fg="black",
                         pady=10)

        self.vars.append(self.expr_label)

        for task in self.vars:
            task.pack(side=tk.TOP, fill=tk.X)

        # 输入框
        self.text_input = tk.Text(self, height=3)
        self.text_input.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_input.focus_set()

        self.update_expr_button = tk.Button(self, text='更新表达式', command=self.update_expr)
        self.update_expr_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.add_variable_button = tk.Button(self, text='变量赋值', command=self.add_variable)
        self.add_variable_button.pack(side=tk.BOTTOM, fill=tk.X)
        

        #self.bind("<Return>", self.update_expr)

        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]


    def add_variable(self, event=None):
        var_text = str(self.text_input.get(1.0, tk.END).strip())

        if len(var_text) > 0 and '=' in var_text:
            new_var = tk.Label(self, text=var_text, pady=10)
        else:
            msgbox.showwarning('提示','请输入变量赋值语句。')
            return

        var = var_text.split('=')
        var_name = var[0]
        var_value = var[1]

        if var_value != '0' and var_value!='1':
            msgbox.showerror('错误', '请将变量赋值为0或1。')
            return

        self.variables[var_name] = bool(int(var_value))

        _, task_style_choice = divmod(len(self.vars), 2)

        my_scheme_choice = self.colour_schemes[task_style_choice]

        new_var.configure(bg=my_scheme_choice["bg"])
        new_var.configure(fg=my_scheme_choice["fg"])

        new_var.pack(side=tk.TOP, fill=tk.X)

        self.vars.append(new_var)


    def update_expr(self, event=None):
        p = ParsingUtility(self.variables)
        text = str(self.text_input.get(1.0, tk.END).strip())
        result_text = text + ': ' + str(p.get_parse_result(text))

        self.expr_label["text"] = result_text

        self.var_list = [i for i in self.variables]

        img = ImgFrame(expr=text, var_list=self.var_list)
        img.pack()


if __name__ == "__main__":
    bdd = BddDemo()
    bdd.mainloop()

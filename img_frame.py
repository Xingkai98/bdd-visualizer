from tkinter import Tk, Canvas, Frame, BOTH, W
from painter import *
from shannon_expansion import *

class ImgFrame(Frame):

    geometry = [500, 800]
    d = 70
    h = 40
    root_center = [250,30]
    r = 15
    dash = [4,4]

    def __init__(self, canvas=None, expr=None, var_list=None):
        super().__init__()
        self.expr = expr
        self.var_list = var_list
        if canvas:
            self.canvas = canvas
        else:
            self.canvas = Canvas(self)
        self.initUI()

    def initUI(self):

        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        #生成INF+画决策树
        bool_to_inf = BoolExprToINF(canvas=self.canvas,bool_expr=self.expr,var_list=self.var_list)

        self.canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = ImgFrame()
    root.geometry(str(ImgFrame.geometry[0]) + 'x' + str(ImgFrame.geometry[1]))
    root.mainloop()


if __name__ == '__main__':
    main()
from tkinter import Tk, Canvas, Frame, BOTH, W
from painter import *
from ShannonExpansion import *

class ImgFrame(Frame):

    d = 70
    h = 40
    root_center = [500,30]
    r = 15
    dash = [4,4]

    def __init__(self, canvas=None, expr=None, var_list=None,
                 root_frame_geometry=None,
                 variables=None):
        super().__init__()
        self.expr = expr
        self.var_list = var_list
        self.variables = variables
        self.root_frame_geometry = root_frame_geometry
        self.root_center[0] = int(self.root_frame_geometry[0] / 2)
        if canvas:
            self.canvas = canvas
        else:
            self.canvas = Canvas(self)
        self.initUI()

    def initUI(self):

        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        #生成INF+画决策树
        bool_to_inf = BoolExprToINF(canvas=self.canvas,
                                    bool_expr=self.expr,
                                    var_list=self.var_list)

        self.canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = ImgFrame()
    root.geometry(str(ex.root_frame_geometry[0]) + 'x' + str(ex.root_frame_geometry[1]))
    root.mainloop()


if __name__ == '__main__':
    main()
from tkinter import Tk, Canvas, Frame, BOTH, W
from painter import *
from bool_expr_to_obdd import *

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

    def draw(self):
        self.master.title("Binary Decision Diagram")
        self.pack(fill=BOTH, expand=1)

        #生成INF+画决策树
        bool_to_obdd = BoolExprToOBDD(canvas=self.canvas,
                                      bool_expr=self.expr,
                                      var_list=self.var_list,
                                      root_center=self.root_center)
        bool_to_obdd.generate_inf(generate_decision_tree=True,
                                  debug=True)
        #bool_to_obdd.decision_tree.draw()
        bool_to_obdd.draw_obdd(root_center=self.root_center,
                               highlight=True,
                               variables=self.variables)

        self.canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = ImgFrame()
    root.geometry(str(ex.root_frame_geometry[0]) + 'x' + str(ex.root_frame_geometry[1]))
    root.mainloop()


if __name__ == '__main__':
    main()
from tkinter import Tk, Canvas, Frame, BOTH, W
from painter import *
from shannon_expansion import *

class ImgFrame(Frame):

    geometry = [500, 500]
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

        bool_to_inf = BoolExprToINF(self.var_list)
        print(bool_to_inf.INF_list)

        decay = 20 #每向下一层，连接子节点的线段的宽度的减少值

        node = Node(canvas=self.canvas, center=self.root_center,text='x1',
                    d=self.d, h=self.h)
        node.create_child_node(direc='left',text='x2',decay=decay)
        node.create_child_node(direc='right',text='y1',decay=decay)
        node.left_child.create_child_node(direc='left',text='y2',isLeaf=True)

        tree = Tree(root_node=node)
        tree.draw()

        self.canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = ImgFrame()
    root.geometry(str(ImgFrame.geometry[0]) + 'x' + str(ImgFrame.geometry[1]))
    root.mainloop()


if __name__ == '__main__':
    main()
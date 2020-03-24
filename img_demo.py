from tkinter import Tk, Canvas, Frame, BOTH, W
from painter import *

class ImgFrame(Frame):

    geometry = [500, 500]
    d = 30
    h = 60
    root_center = [250,30]
    r = 15
    dash = [4,4]

    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self)
        self.initUI()

    def initUI(self):

        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        node = Node(canvas=self.canvas, center=self.root_center,text='x1')
        node.create_child_node(direc='left',text='x2')
        node.create_child_node(direc='right',text='y1')
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
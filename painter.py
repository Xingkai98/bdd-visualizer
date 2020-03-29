
from tkinter import Tk, Canvas, Frame, BOTH, W, CENTER

class Tree:


    def __init__(self, root_node=None):
        self.root_node = root_node

    def draw_all_lines(self, node): # 画出所有连线
        if node:
            node.draw_right_line()
            node.draw_left_line()
        if node.left_child:
            self.draw_all_lines(node.left_child)
        if node.right_child:
            self.draw_all_lines(node.right_child)

    def draw_all_nodes(self, node): # 画出所有节点内容
        if node:
            node.draw_center()
        if node.left_child:
            self.draw_all_nodes(node.left_child)
        if node.right_child:
            self.draw_all_nodes(node.right_child)

    def draw(self): # 画出整个树
        self.draw_all_lines(self.root_node)
        self.draw_all_nodes(self.root_node)



class Node:

    def __init__(self, canvas=None, center=(0,0), r=15,
                 d=40, h=60, dash=(4,4), decay=10,
                 left_child=None, right_child=None, text=None):
        self.canvas = canvas
        self.center = center
        self.r = r
        self.d = d
        self.h = h
        self.dash = dash
        self.left_child = left_child
        self.right_child = right_child
        self.text = text
        self.decay = decay

    def create_child_node(self, direc=None, d=None, h=None,
                          isLeaf=False, text=None, decay=None):

        child_d = self.d
        child_h = self.h

        if h:
            child_h = h
        if d:
            child_d = d
        if decay:
            child_d -= decay

        x = self.center[0]
        y = self.center[1]

        if isLeaf:
            child_node = LeafNode(canvas=self.canvas,d=child_d,h=child_h)
        else:
            child_node = Node(canvas=self.canvas,d=child_d,h=child_h)

        if text:
            child_node.text = text

        if direc == 'left':
            child_node.center = [x - self.d, y + self.h]
            self.left_child = child_node
        elif direc == 'right':
            child_node.center = [x + self.d, y + self.h]
            self.right_child = child_node

    def draw_text(self):
        if self.text:
            self.canvas.create_text(self.center[0], self.center[1], anchor=CENTER, font="Purisa",
                                    text=str(self.text))

    def draw_center(self):
        self.canvas.create_oval(self.center[0]-self.r, self.center[1]-self.r, self.center[0]+self.r, self.center[1]+self.r, outline="black",
                                fill="white", width=2)
        self.draw_text()

    def draw_left_line(self):
        self.canvas.create_line(self.center[0], self.center[1],
                                self.center[0] - self.d, self.center[1] + self.h,
                                dash=self.dash)

    def draw_right_line(self):
        self.canvas.create_line(self.center[0], self.center[1],
                                self.center[0] + self.d, self.center[1] + self.h)

class LeafNode(Node):

    def draw_center(self, text=None):
        self.canvas.create_rectangle(self.center[0]-self.r, self.center[1]-self.r, self.center[0]+self.r, self.center[1]+self.r,
                                     outline='black',fill='white',width=2)
        self.draw_text()

    def draw_left_line(self):
        pass

    def draw_right_line(self):
        pass

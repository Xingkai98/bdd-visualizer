from tkinter import Tk, Canvas, Frame, BOTH, W, CENTER

class Node:

    highlight_color = 'blue'  # 高亮路径的颜色
    highlighted = False  # 默认非高亮

    def __init__(self, canvas=None, center=(0,0), r=15,
                 d=40, h=60, dash=(4,4), decay=10,
                 low_child=None, high_child=None, text=None):
        self.canvas = canvas
        self.center = center
        self.r = r
        self.d = d
        self.h = h
        self.dash = dash
        self.low_child = low_child
        self.high_child = high_child
        self.text = text
        self.decay = decay

    def highlight(self):
        self.highlighted = True

    @property
    def is_highlighted(self):
        return self.highlighted

    # 绘制二叉树相关
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

        if direc == 'low':
            child_node.center = [x - self.d, y + self.h]
            self.low_child = child_node
        elif direc == 'high':
            child_node.center = [x + self.d, y + self.h]
            self.high_child = child_node

    def draw_text(self, highlight = False):
        if self.text:
            if self.is_highlighted or highlight is True:
                self.canvas.create_text(self.center[0], self.center[1], anchor=CENTER, font="Purisa",
                                        text=str(self.text),
                                        fill=self.highlight_color)
            else:
                self.canvas.create_text(self.center[0], self.center[1], anchor=CENTER, font="Purisa",
                                        text=str(self.text),
                                        fill='black')

    def draw_center(self, highlight = False):
        if self.is_highlighted or highlight is True:
            self.canvas.create_oval(self.center[0]-self.r, self.center[1]-self.r, self.center[0]+self.r, self.center[1]+self.r,
                                    outline=self.highlight_color,
                                    fill="white", width=2)
        else:
            self.canvas.create_oval(self.center[0] - self.r, self.center[1] - self.r, self.center[0] + self.r,
                                    self.center[1] + self.r,
                                    outline="black",
                                    fill="white", width=1)
        self.draw_text(highlight=highlight)

    def draw_low_line(self):
        self.canvas.create_line(self.center[0], self.center[1],
                                self.center[0] - self.d, self.center[1] + self.h,
                                dash=self.dash)

    def draw_high_line(self):
        self.canvas.create_line(self.center[0], self.center[1],
                                self.center[0] + self.d, self.center[1] + self.h)

    def draw_line_manual(self, isDashed, d, h, highlight = None):
        color = 'black'
        if highlight is True:
            color = self.highlight_color
        if isDashed:
            self.canvas.create_line(self.center[0], self.center[1],
                                    self.center[0] + d, self.center[1] + h,
                                    dash=self.dash, fill=color)
        else:
            self.canvas.create_line(self.center[0], self.center[1],
                                    self.center[0] + d, self.center[1] + h,
                                    fill=color)

    def draw_line_towards(self, isDashed, node, highlight=False):
        width = 1
        color = 'black'
        if highlight or (self.is_highlighted and node.is_highlighted) is True:
            color = self.highlight_color
            width = 2
        if isDashed:
            self.canvas.create_line(self.center[0], self.center[1],
                                    node.center[0], node.center[1],
                                    dash=self.dash, fill=color,
                                    width=width)
        else:
            self.canvas.create_line(self.center[0], self.center[1],
                                    node.center[0], node.center[1],
                                    fill=color,
                                    width=width)

class LeafNode(Node):

    def draw_center(self, text=None, r=15, highlight=False):
        self.r = r
        if self.is_highlighted or highlight is True:
            self.canvas.create_rectangle(self.center[0]-self.r, self.center[1]-self.r, self.center[0]+self.r, self.center[1]+self.r,
                                         outline=self.highlight_color,fill='white',width=2)
        else:
            self.canvas.create_rectangle(self.center[0] - self.r, self.center[1] - self.r, self.center[0] + self.r,
                                         self.center[1] + self.r,
                                         outline="black", fill='white', width=1)
        self.draw_text(highlight=highlight)

    def draw_low_line(self):
        pass

    def draw_high_line(self):
        pass


class Tree:

    def __init__(self, root_node=None):
        self.root_node = root_node

    def draw_all_lines(self, node): # 画出所有连线
        if node:
            node.draw_high_line()
            node.draw_low_line()
        if node.low_child:
            self.draw_all_lines(node.low_child)
        if node.high_child:
            self.draw_all_lines(node.high_child)

    def draw_all_nodes(self, node): # 画出所有节点内容
        if node:
            node.draw_center()
        if node.low_child:
            self.draw_all_nodes(node.low_child)
        if node.high_child:
            self.draw_all_nodes(node.high_child)

    def draw(self): # 画出整个树
        self.draw_all_lines(self.root_node)
        self.draw_all_nodes(self.root_node)

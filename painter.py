
class Tree:

    def __init__(self, root_node=None):
        self.root_node = root_node

    def draw_all_lines(self, node): # 画出所有连线
        if node:
            node.draw_right_line()
            node.draw_left_line()
        if node.lchild:
            self.draw_all_lines(node.lchild)
        if node.rchild:
            self.draw_all_lines(node.rchild)

    def draw_all_nodes(self, node): # 画出所有节点内容
        if node:
            node.draw_circle()
        if node.lchild:
            self.draw_all_nodes(node.lchild)
        if node.rchild:
            self.draw_all_nodes(node.rchild)

    def draw(self): # 画出整个树
        self.draw_all_lines(self.root_node)
        self.draw_all_nodes(self.root_node)



class Node:

    def __init__(self, canvas=None, center=(0,0), r=15, d=30, h=60, dash=(4,4),
                       lchild=None, rchild=None):
        self.canvas = canvas
        self.center = center
        self.r = r
        self.d = d
        self.h = h
        self.dash = dash
        self.lchild = lchild
        self.rchild = rchild

    def create_child_node(self, direc=None, d=None, h=None):

        child_d = self.d
        child_h = self.h

        if d:
            child_d = d
        if h:
            child_h = h

        x = self.center[0]
        y = self.center[1]

        if direc == 'left':
            self.lchild = Node(canvas=self.canvas, center=[x-child_d, y+child_h])
        elif direc == 'right':
            self.rchild = Node(canvas=self.canvas, center=[x+child_d, y+child_h])

    def draw_circle(self):
        self.canvas.create_oval(self.center[0]-self.r, self.center[1]-self.r, self.center[0]+self.r, self.center[1]+self.r, outline="black",
                                fill="white", width=2)

    def draw_left_line(self):
        self.canvas.create_line(self.center[0], self.center[1],
                                self.center[0] - self.d, self.center[1] + self.h,
                                dash=self.dash)

    def draw_right_line(self):
        self.canvas.create_line(self.center[0], self.center[1],
                                self.center[0] + self.d, self.center[1] + self.h)



import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import *
from img_frame import ImgFrame
from bool_expr_to_bdd import *
from list_permuter import *

class MainFrame(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("BDD")
        self.width = 1024
        self.height = 768
        self.geometry(str(self.width) + "x" + str(self.height))

        self.left_frame = Frame(self)
        self.mid_frame = Frame(self)
        self.right_frame = Frame(self)

        l1 = Label(self.left_frame, text='p1',bg='red')
        b1 = Button(self.left_frame)
        l2 = Label(self.mid_frame, text='p2', bg='blue')
        l3 = Label(self.right_frame, text='p3', bg='green')

        l1.pack(side=LEFT, fill=BOTH)
        b1.pack(fill=BOTH)
        l2.pack(side=RIGHT, fill=BOTH)
        l3.pack(fill=BOTH)

        self.left_frame.pack(side=LEFT, fill=BOTH)
        self.mid_frame.pack(side=RIGHT, fill=BOTH)
        self.right_frame.pack(fill=BOTH)


if __name__ == "__main__":
    main_frame = MainFrame()
    main_frame.mainloop()
import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("test")
        self.geometry("800x600")
        self.label = tk.Label(self, text="Hello World")
        self.button = tk.Button(text="Run",command=self.test_button_clicked)
        self.label.pack()
        self.button.pack()
        self.task_create = tk.Text(self, height=3, bg="white", fg="black")

        self.task_create.pack(side=tk.BOTTOM)
        self.task_create.focus_set()

        self.bind("<Return>", self.test_button_clicked)

    def test_button_clicked(self,a):
        print("Button clicked.")

if __name__ == "__main__":
    root = Root()
    root.mainloop()
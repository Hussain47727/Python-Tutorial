import tkinter as tk
import random

class snake:
    def __init__(self, root):
        self.root = root
        self.root.title('Snake Game')
        self.canvas = tk.Canvas(root, width=400, height=400,bg='red')



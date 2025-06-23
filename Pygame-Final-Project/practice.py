import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Snake Game')
        self.canvas = tk.Canvas(root, width=400, height=400, bg='red')
        self.canvas.pack()
        self.snake = [[100, 100]]
        self.food = self.create_food()
        self.direction = 'right'
        self.running = True
        self.draw_snake()
        self.draw_food()
        self.root.after(150, self.move_snake)

    def create_food(self):
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        return [x, y]

    def draw_snake(self):
        for block in self.snake:
            x, y = block
            self.canvas.create_rectangle(x, y, x + 20, y + 20, fill='green')

    def draw_food(self):
        x, y = self.food
        self.canvas.create_oval(x, y, x + 20, y + 20, fill='yellow')

    def move_snake(self):
        if not self.running:
            return

        head_x, head_y = self.snake[0]

        if self.direction == 'right':
            head_x += 20
        elif self.direction == 'left':
            head_x -= 20
        elif self.direction == 'up':
            head_y -= 20
        elif self.direction == 'down':
            head_y += 20

        new_head = [head_x, head_y]
        self.snake.insert(0, new_head)
        self.snake.pop()

        self.canvas.delete("all")
        self.draw_snake()
        self.draw_food()

        self.root.after(150, self.move_snake)

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()

import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack()
        self.snake = [[100, 100]]
        self.food = self.spawn_food()
        self.direction = "Right"
        self.running = True
        self.move_snake()
        self.root.bind("<Key>", self.change_dir)

    def spawn_food(self):
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        return [x, y]

    def change_dir(self, event):
        key = event.keysym
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if key in opposites and opposites[key] != self.direction:
            self.direction = key

    def move_snake(self):
        if not self.running:
            return

        head = self.snake[0][:]
        moves = {"Up": (0, -20), "Down": (0, 20), "Left": (-20, 0), "Right": (20, 0)}
        move = moves[self.direction]
        head[0] += move[0]
        head[1] += move[1]

        if head in self.snake or not (0 <= head[0] < 400 and 0 <= head[1] < 400):
            self.game_over()
            return

        self.snake.insert(0, head)
        if head == self.food:
            self.food = self.spawn_food()
        else:
            self.snake.pop()

        self.canvas.delete("all")
        self.canvas.create_rectangle(*self.food, self.food[0]+20, self.food[1]+20, fill="red")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+20, y+20, fill="green")

        self.root.after(200, self.move_snake)

    def game_over(self):
        self.running = False
        self.canvas.create_text(200, 200, text="Game Over", fill="white", font=("Arial", 24))

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()

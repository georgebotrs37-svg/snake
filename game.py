import random
import tkinter as tk


WIDTH = 600
HEIGHT = 400
CELL = 20
INITIAL_SPEED_MS = 120
MIN_SPEED_MS = 65
SPEEDUP_STEP_MS = 2


class SnakeGame:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Snake Game (Python)")
        self.root.resizable(False, False)

        self.score_var = tk.StringVar(value="Score: 0")
        score_label = tk.Label(
            root,
            textvariable=self.score_var,
            font=("Segoe UI", 12, "bold"),
            padx=8,
            pady=6,
        )
        score_label.pack(fill="x")

        self.canvas = tk.Canvas(
            root,
            width=WIDTH,
            height=HEIGHT,
            bg="#101820",
            highlightthickness=0,
        )
        self.canvas.pack()

        self.root.bind("<Up>", lambda _: self.change_direction("Up"))
        self.root.bind("<Down>", lambda _: self.change_direction("Down"))
        self.root.bind("<Left>", lambda _: self.change_direction("Left"))
        self.root.bind("<Right>", lambda _: self.change_direction("Right"))
        self.root.bind("<w>", lambda _: self.change_direction("Up"))
        self.root.bind("<s>", lambda _: self.change_direction("Down"))
        self.root.bind("<a>", lambda _: self.change_direction("Left"))
        self.root.bind("<d>", lambda _: self.change_direction("Right"))
        self.root.bind("<space>", lambda _: self.restart())

        self.game_over = False
        self.after_id = None
        self.restart()

    def restart(self) -> None:
        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
            self.after_id = None

        self.game_over = False
        self.direction = "Right"
        self.next_direction = "Right"
        self.score = 0
        self.speed_ms = INITIAL_SPEED_MS

        start_x = WIDTH // 2
        start_y = HEIGHT // 2
        self.snake = [
            (start_x, start_y),
            (start_x - CELL, start_y),
            (start_x - 2 * CELL, start_y),
        ]
        self.food = self.random_food_position()
        self.update_score()
        self.draw()
        self.tick()

    def change_direction(self, new_dir: str) -> None:
        if self.game_over:
            return

        opposites = {
            "Up": "Down",
            "Down": "Up",
            "Left": "Right",
            "Right": "Left",
        }
        if opposites[self.direction] != new_dir:
            self.next_direction = new_dir

    def random_food_position(self) -> tuple[int, int]:
        while True:
            x = random.randrange(0, WIDTH, CELL)
            y = random.randrange(0, HEIGHT, CELL)
            if (x, y) not in self.snake:
                return (x, y)

    def move_head(self, head: tuple[int, int]) -> tuple[int, int]:
        x, y = head
        if self.direction == "Up":
            return (x, y - CELL)
        if self.direction == "Down":
            return (x, y + CELL)
        if self.direction == "Left":
            return (x - CELL, y)
        return (x + CELL, y)

    def tick(self) -> None:
        if self.game_over:
            return

        self.direction = self.next_direction
        new_head = self.move_head(self.snake[0])

        x, y = new_head
        hit_wall = x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT
        hit_self = new_head in self.snake
        if hit_wall or hit_self:
            self.end_game()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.speed_ms = max(MIN_SPEED_MS, self.speed_ms - SPEEDUP_STEP_MS)
            self.food = self.random_food_position()
            self.update_score()
        else:
            self.snake.pop()

        self.draw()
        self.after_id = self.root.after(self.speed_ms, self.tick)

    def update_score(self) -> None:
        self.score_var.set(f"Score: {self.score}")

    def draw(self) -> None:
        self.canvas.delete("all")

        fx, fy = self.food
        self.canvas.create_rectangle(
            fx + 2,
            fy + 2,
            fx + CELL - 2,
            fy + CELL - 2,
            fill="#ff6b6b",
            width=0,
        )

        for i, (x, y) in enumerate(self.snake):
            color = "#7DFF9A" if i == 0 else "#3EDB6A"
            self.canvas.create_rectangle(
                x + 1,
                y + 1,
                x + CELL - 1,
                y + CELL - 1,
                fill=color,
                width=0,
            )

    def end_game(self) -> None:
        self.game_over = True
        self.draw()
        self.canvas.create_rectangle(
            0,
            HEIGHT // 2 - 40,
            WIDTH,
            HEIGHT // 2 + 40,
            fill="#000000",
            stipple="gray25",
            width=0,
        )
        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2 - 12,
            text="Game Over",
            fill="white",
            font=("Segoe UI", 22, "bold"),
        )
        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2 + 16,
            text="Press Space to Restart",
            fill="white",
            font=("Segoe UI", 12),
        )


def main() -> None:
    root = tk.Tk()
    SnakeGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()

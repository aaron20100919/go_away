import tkinter as tk
from config import *
from os import system


class GridApp:
    def __init__(self, root, rows, cols):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.grid_buttons = []
        self.box = [[False for _ in range(cols)] for _ in range(rows)]

        self.ok_button = tk.Button(root, text="ok", command=self.ok)

        for i in range(rows):
            row_buttons = []
            for j in range(cols):
                btn = tk.Button(
                    root,
                    text=f"{i},{j}",
                    command=lambda row=i, col=j: self.on_button_click(row, col),
                )
                btn.config(bg="white")
                btn.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(btn)
            self.grid_buttons.append(row_buttons)
        self.ok_button.grid()

    def on_button_click(self, row, col):
        if self.grid_buttons[row][col].cget("bg") == "white":
            self.grid_buttons[row][col].config(bg="gray")
            self.box[row][col] = True
        else:
            self.grid_buttons[row][col].config(bg="white")
            self.box[row][col] = False

    def ok(self):
        system("cls")
        for i in range(self.rows):
            for j in range(self.cols):
                if self.box[i][j]:
                    print(f"room.append(({i}, {j}))")


def main():
    rows = screen_size[1] // box_size[1]
    cols = screen_size[0] // box_size[0]

    root = tk.Tk()
    root.title("Grid Example")

    app = GridApp(root, rows, cols)

    root.mainloop()


if __name__ == "__main__":
    main()

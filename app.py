import tkinter as tk
import random

# Constants
BOARD_SIZE = 8
SHIP_SIZE = 3
NUM_SHIPS = 3

class BattleshipGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Battleship Game")
        self.board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.ships = []
        self.create_board()
        self.place_ships()

    def create_board(self):
        self.buttons = [[tk.Button(self.root, width=3, height=1, command=lambda x=x, y=y: self.check_hit(x, y))
                         for y in range(BOARD_SIZE)] for x in range(BOARD_SIZE)]

        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                self.buttons[x][y].grid(row=x, column=y)

    def place_ships(self):
        for _ in range(NUM_SHIPS):
            while True:
                direction = random.choice(['horizontal', 'vertical'])
                if direction == 'horizontal':
                    ship_x, ship_y = random.randint(0, BOARD_SIZE - 1 - SHIP_SIZE), random.randint(0, BOARD_SIZE - 1)
                    if all(self.board[ship_x + i][ship_y] == 0 for i in range(SHIP_SIZE)):
                        for i in range(SHIP_SIZE):
                            self.board[ship_x + i][ship_y] = 1
                        self.ships.append([(ship_x + i, ship_y) for i in range(SHIP_SIZE)])
                        break
                else:
                    ship_x, ship_y = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1 - SHIP_SIZE)
                    if all(self.board[ship_x][ship_y + i] == 0 for i in range(SHIP_SIZE)):
                        for i in range(SHIP_SIZE):
                            self.board[ship_x][ship_y + i] = 1
                        self.ships.append([(ship_x, ship_y + i) for i in range(SHIP_SIZE)])
                        break

    def check_hit(self, x, y):
        if any((x, y) in ship for ship in self.ships):
            self.buttons[x][y].config(text="X", state=tk.DISABLED, disabledforeground="red")
            for ship in self.ships:
                if (x, y) in ship:
                    ship.remove((x, y))
                    if len(ship) == 0:
                        self.ships.remove(ship)
                        if len(self.ships) == 0:
                            self.end_game("You won!")
                            # add messagebox
                            tk.messagebox.Message(master = "you win", **"ok")
                    break
        else:
            self.buttons[x][y].config(text="O", state=tk.DISABLED, disabledforeground="blue")

    def end_game(self, message):
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                self.buttons[x][y].config(state=tk.DISABLED)
        print(message)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = BattleshipGame()
    game.run()
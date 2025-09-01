#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        # Print column headers
        print('   ', end='')
        for i in range(self.width):
            print(f'{i:2d}', end='')
        print()
        
        # Print rows with row numbers
        for y in range(self.height):
            print(f'{y:2d} ', end='')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('* ', end='')
                    else:
                        count = self.count_mines_nearby(x, y)
                        if count > 0:
                            print(f'{count} ', end='')
                        else:
                            print('  ', end='')
                else:
                    print('. ', end='')
            print()
        print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:  # Skip the current cell
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def is_valid_coordinate(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def reveal(self, x, y):
        # Check if coordinates are valid
        if not self.is_valid_coordinate(x, y):
            return None
        
        # Check if already revealed
        if self.revealed[y][x]:
            return True
        
        # Check if it's a mine
        if (y * self.width + x) in self.mines:
            return False
        
        # Reveal the cell
        self.revealed[y][x] = True
        
        # If no mines nearby, reveal adjacent cells
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if self.is_valid_coordinate(nx, ny) and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def check_win(self):
        for y in range(self.height):
            for x in range(self.width):
                if not self.revealed[y][x] and (y * self.width + x) not in self.mines:
                    return False
        return True

    def play(self):
        print("Welcome to Minesweeper!")
        print(f"Board size: {self.width}x{self.height}, Mines: {len(self.mines)}")
        print("Enter coordinates (x y) to reveal a cell, or 'q' to quit")
        
        while True:
            self.print_board()
            
            try:
                user_input = input("Enter x and y coordinates (or 'q' to quit): ").strip()
                
                if user_input.lower() == 'q':
                    print("Thanks for playing!")
                    break
                
                coords = user_input.split()
                if len(coords) != 2:
                    print("Please enter exactly two coordinates separated by space.")
                    input("Press Enter to continue...")
                    continue
                
                x, y = int(coords[0]), int(coords[1])
                
                if not self.is_valid_coordinate(x, y):
                    print(f"Invalid coordinates! Please enter values between 0-{self.width-1} for x and 0-{self.height-1} for y.")
                    input("Press Enter to continue...")
                    continue
                
                if self.revealed[y][x]:
                    print("This cell is already revealed!")
                    input("Press Enter to continue...")
                    continue
                
                result = self.reveal(x, y)
                
                if result is False:  # Hit a mine
                    self.print_board(reveal=True)
                    print("💥 Game Over! You hit a mine.")
                    break
                elif self.check_win():
                    self.print_board()
                    print("🎉 Congratulations! You've won the game!")
                    break
                    
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                input("Press Enter to continue...")
            except KeyboardInterrupt:
                print("\nGame interrupted. Thanks for playing!")
                break

if __name__ == "__main__":
    game = Minesweeper()
    game.play()

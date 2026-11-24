grid_1 = [
    ["X", "X", "X"],
    ["O", "O", "X"],
    ["O", "X", "O"]
]

grid_2 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "O", "X"]
]

grid_3 = [
    ["X", "O", "O"],
    ["O", "X", "X"],
    ["O", "X", "X"]
]

grid_4 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "X", "X"]
]

def display_grid(grid):
    for row in range(3):
        print(" " + grid[row][0] + " | " + grid[row][1] + " | " + grid[row][2])
        if row < 2:
            print("---+---+---")


def determine_winner(grid):
    for row in range(3):
        if grid[row][0] == grid[row][1] and grid[row][1] == grid[row][2]:
            return grid[row][0]

    for col in range(3):
        if grid[0][col] == grid[1][col] and grid[1][col] == grid[2][col]:
            return grid[0][col]

    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
        return grid[0][0]

    if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
        return grid[0][2]

    return "tie"
print("grid 1")
display_grid(grid_1)
result = determine_winner(grid_1)
if result == "tie":
    print("tie")
else:
    print("winner:", result)
print()

print("grid 2")
display_grid(grid_2)
result = determine_winner(grid_2)
if result == "tie":
    print("tie")
else:
    print("winner:", result)
print()

print("grid 3")
display_grid(grid_3)
result = determine_winner(grid_3)
if result == "tie":
    print("tie")
else:
    print("winner:", result)
print()

print("Ggrid 4")
display_grid(grid_4)
result = determine_winner(grid_4)
if result == "tie":
    print("tie")
else:
    print("winner:", result)
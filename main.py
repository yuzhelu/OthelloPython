
import Board


b = Board.Board()
b.print_game_board()

game = True

print("Starting Game")
print("Black goes first")

# while game:
white_available_points = b.get_valid_points('W', 'B')

black_available_points = b.get_valid_points('B', 'W')

b.display_valid_spots(black_available_points, 'B', 'W')







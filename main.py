
import Board

b = Board.Board()
b.print_game_board()

game = True

print("Starting Game")
print("Black goes first")

while game:
    white_available_points = b.get_valid_points('W', 'B')
    black_available_points = b.get_valid_points('B', 'W')

    b.display_valid_spots(black_available_points, 'B', 'W')
    result = b.move_result(white_available_points, black_available_points)

    if result == 1:
        game = False
        print("White wins. White: " + b.get_white_score() + " Black: " + b.get_black_score())
        break
    elif result == -1:
        game = False
        print("Black wins. Black: " + b.get_black_score() + " White: " + b.get_white_score())
        break
    elif result == 0:
        print("Tie game")
        break

    # check if black can play
    if not black_available_points:
        print("black can no longer play. White wins")
        game = False
        break

    user_input = input("Enter move - Black: ")
    y = int(user_input[0])
    x = int(user_input[1])
    move = Board.Piece(x, y)

    isValid = False
    for i in black_available_points:
        if(move.x == i.x) and (move.y == i.y):
            isValid = True
            break

    while not isValid:
        user_input = input("Invalid. Please try again")
        move.y = user_input[0]
        move.x = user_input[1]
        for i in black_available_points:
            if (move.x == i.x) and (move.y == i.y):
                isValid = True
                break

    b.input_move(move, 'B', 'W')
    b.print_game_board()
    b.update_scores()
    print("Black: " + str(b.get_black_score()) + " White: " + str(b.get_white_score()))

    # ready up for white turn
    white_available_points = b.get_valid_points('W', 'B')
    black_available_points = b.get_valid_points('B', 'W')

    b.display_valid_spots(white_available_points, 'W', 'B')

    result = b.move_result(white_available_points,black_available_points)

    if result == 1:
        print("White wins. White: " + b.get_white_score() + " Black: " + b.get_black_score())
        break
    elif result == -1:
        print("Black wins. Black: " + b.get_black_score() + " White: " + b.get_white_score())
        break
    elif result == 0:
        game = False
        print("Tie game")
        break

    if not white_available_points:
        print("White can no longer play. Black wins");
        game = False
        break

    user_input = input("Enter move - White: ")
    y = int(user_input[0])
    x = int(user_input[1])
    move = Board.Piece(x, y)

    isValid = False
    for i in white_available_points:
        if(move.x == i.x) and (move.y == i.y):
            isValid = True
            break

    while not isValid:
        user_input = input("Invalid input. Try again")
        move.y = user_input[0]
        move.x = user_input[1]
        for i in white_available_points:
            if (move.x == i.x) and (move.y == i.y):
                isValid = True
                break

    b.input_move(move, 'W', 'B')
    b.update_scores()
    print("White: " + str(b.get_white_score()) + " Black: " + str(b.get_black_score()))

















while True:

    from board_template import board
    # variable declaration
    user=[" "," "," "," "," "," "," "," "," "]
    x_value={'123':0,'456':0,'789':0,'147':0,'369':0,'159':0,'258':0}
    y_value={'123':0,'456':0,'789':0,'147':0,'369':0,'159':0,'258':0}
    game_end='B'

    player1=input('Welcome to Tic tac game !!.Would you like to be player 1 Yes/No:')
    if player1=="Yes":
        player1_symbol=input('Player 1,Choose your symbol X or O:')
        player1_name=input('Player 1 Enter your name:')
        player2_name=input('Player 2 Enter your name:')
        if player1_symbol=='X':
            player2_symbol ='O'
        else:
            player2_symbol = 'X'
        board(user)
        k=0
        for k in range(1,10):
            # Player 1 turn to play
            if k in [1,3,5,7,9]:
                user_input = input("Player 1 Enter your position:")
                # To print on board
                for i in range(1,10):
                    if i==int(user_input):
                        user[i-1]=player1_symbol
                # To check if player 1 is won
                for key in x_value.keys():
                    if key.__contains__(user_input) is True:
                        x_value[key] = x_value[key] + 1
                for key in x_value.keys():
                    if x_value[key] == 3:
                        print(player1_name+' is winner.')
                        game_end=input('Would you like to play again Y/N:')
                        break


            # Player 2 turn to play
            else:
                user_input = input("Player 2 Enter your position:")
                for i in range(1,10):
                    if i == int(user_input):
                        user[i-1]=player2_symbol
                # To check if player 2 is won
                for key in y_value.keys():
                    if key.__contains__(user_input) is True:
                        y_value[key] = y_value[key] + 1
                for key in y_value.keys():
                    if y_value[key] == 3:
                        print(player2_name+' is winner.')
                        game_end = input('Would you like to play again Y/N:')
                        break
            if game_end == 'Y':
                break
            elif game_end == 'N':
                print("Thanks for playing!!")
                exit()
            board(user)  ## End of for loop for next user input
        if game_end == 'B':
            print('game is a draw')
            game_end = input('Would you like to play again Y/N:')
            if game_end == 'Y':
                continue
            elif game_end == 'N':
                print("Thanks for playing!!")
                exit()


    else:
        player2_symbol=input('Player 2,Choose your symbol X or O:')
        player2_name=input('Player 2 Enter your name:')
        player1_name=input('Player 1 Enter your name:')
        if player2_symbol=='X':
            player1_symbol ='O'
        else:
            player1_symbol = 'X'
        board(user)
        k = 0
        for k in range(1, 10):
            # Player 1 turn to play
            if k in [1, 3, 5, 7, 9]:
                user_input = input("Player 2 Enter your position:")
                # To print on board
                for i in range(1, 10):
                    if i == int(user_input):
                        user[i - 1] = player2_symbol
                # To check if player 2 is won
                for key in x_value.keys():
                    if key.__contains__(user_input) is True:
                        x_value[key] = x_value[key] + 1
                for key in x_value.keys():
                    if x_value[key] == 3:
                        print(player2_name+' is winner.')
                        game_end=input('Would you like to play again Y/N:')
                        break
            # Player 2 turn to play
            else:
                user_input = input("Player 1 Enter your position:")
                for i in range(1, 10):
                    if i == int(user_input):
                        user[i - 1] = player1_symbol
                # To check if player 2 is won
                for key in y_value.keys():
                    if key.__contains__(user_input) is True:
                        y_value[key] = y_value[key] + 1
                for key in y_value.keys():
                    if y_value[key] == 3:
                        print(player1_name+' is winner.')
                        game_end=input('Would you like to play again Y/N:')
                        break
            if game_end=='Y':
                break
            elif game_end=='N':
                print("Thanks for playing!!")
                exit()
            board(user)## End of for loop for nex user input
        if game_end=='B':
         print('game is a draw')
         game_end = input('Would you like to play again Y/N:')
         if game_end == 'Y':
             continue
         elif game_end == 'N':
             print("Thanks for playing!!")
             exit()



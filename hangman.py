import random

def hangman(words):
    random_word = random.choice(words)
    word = random_word
    wrong = 0
    stages = ["",
              "______      ",
              "|           ",
              "|     |     ",
              "|     O     ",
              "|    /|\    ",
              "|    / \    ",
              "|           "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))

list_of_words = ["cat","dog","mongoose","weasel","duck"]
hangman(list_of_words)

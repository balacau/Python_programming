# Challenge:  UNO Bank Card Game - www.101computing.net/uno-bank-card-game-using-python

# Still a work in prigress


"""
Challenge:

Create a text based game of Uno, that does the following:

Cards:
    Green Cards:
        Increase your bank balance by the amount on the card (+1$, +3$, +5$, +7$). Done
    Blue Cards:
        Decrease your bank balance by the amount on the card (-2$, -4$, -6$, -8$). Done
    Black Cards:
        x2: Double your current bank balance.
        /2: Halve your current bank balance.
        +2: Gain 2 extra draws.
        -2: Lose 2 draws.



How to Build the Game in Python
Step 1: Set Up the Deck
    Create a deck of cards with the following distribution:

        Green Cards: 4 cards (+1$, +3$, +5$, +7$)
        Blue Cards: 4 cards (-2$, -4$, -6$, -8$)
        Black Cards: 4 cards (x2, /2, +2, -2)

You can use a list to represent the deck and shuffle it at the start of the game.

Step 2: Initialise the Game

        Start with a bank balance of $10.
        Start with 10 draws.

Step 3: Game Loop

        Draw a Card: Randomly select a card from the deck.
        Apply the Effect:
        If it’s a green card, add the amount to the bank.
        If it’s a blue card, subtract the amount from the bank.
        If it’s a black card, apply the special effect (double, halve, or change the number of draws).
        Update Draws: Decrease the number of draws by 1 (unless a +2 or -2 card is drawn).
        Repeat until no draws are left.

Step 4: Display the Result
        Once all draws are used, display the final bank balance.

"""

import random, time

print(" +------------------+")
print(" |                  |")
print(" |     UNO BANK     |")
print(" |    CARD GAME!    |")
print(" |                  |")
print(" +------------------+")
print("")


# Let's setup Number of draws and bank balance for each player
player1B = 10
player1D = 10

player2B = 10
player2D = 10

# Let's setup the card values and shuffle the deck
cardValue = 0

greenCards = ['+1', '+3', '+5', '+7']
blueCards = ['-2', '-4', '-6', '-8']
blackCards = ['x2', '/2', '+2!', '-2!']

deck = greenCards + blueCards #+ blackCards
print("Shuffling deck...")
print("\n")
random.shuffle(deck)
time.sleep(1)

# Let's draw the first card from the deck...
def greenDraw(card):
    if card == '+1':
        return 1
    elif card == '+3':
        return 3
    elif card == '+5':
        return 5
    elif card == '+7':
        return 7
    return 0


def blueDraw(card):
    if card == '-2':
        return -2
    elif card == '-4':
        return -4
    elif card == '-6':
        return -6
    elif card == '-8':
        return -8
    return 0

def blackDraw(card):
    print("This is a BLACK card")

# Let's setup the card drawing process
def Draw():
    print("Drawing card...")
    time.sleep(1)

    card = random.choice(deck)
    print("Your card:", card)

    if card in greenCards:
        return greenDraw(card)
    elif card in blueCards:
        return blueDraw(card)
    return 0

# Let's setup the card draw for player 1
def player1Draw():
    global player1D, player1B

    if player1D >= 1:
        player1D -= 1
        print("\n" * 50)
        print("\nPlayer 1 drawing...\n")
        print(f"You have {player1D} draws left..")

        value = Draw()
        print("Card value:", value)

        player1B += value
        print(f"Your bank balance: {player1B}\n")
        time.sleep(2)

# Let's setup the card draw for player 2
def player2Draw():
    global player2D, player2B

    if player2D >= 1:
        player2D -= 1
        print("\nPlayer 2 drawing...\n")
        print(f"You have {player2D} draws left..")

        value = Draw()
        print("Card value:", value)

        player2B += value
        print(f"Your bank balance: {player2B}\n")
        time.sleep(2)

# Main program
def main():
    global player1D, player2D, player1B, player2B
    print()
    while player1D >= 1 and player2D >= 1:
        player1Draw()
        player2Draw()
    else:
        print("\n" * 50)
        print("Game over\n")
        print("Player 1 score: ", player1B)
        print("Player 2 score: ", player2B)
        print()
        if player1B > player2B:
            print("Player 1 wins!")
        elif player1B < player2B:
            print("Player 2 wins!")
        else:
            print("Draw!")


main()


"""
Extension Task: 2-Player Mode!
    Ready to take Uno Bank to the next level? In this two-player extension, 
    you and a friend will compete to maximise your bank balances by drawing cards from a shared deck. 
    The rules remain similar, but now, you will take turns drawing cards, 
    and a new set of yellow cards introduces exciting (and sometimes brutal) interactions between players!

New Rules for Two-Player Mode
    Objective
        Both players start with $10 and 10 draws. Players take turns drawing one card at a time. 
        The game ends when one of the players have used all their draws. The player with the highest bank balance wins!

New Cards
The game uses the same cards as before plus an extra 4 yellow cards:
        Swap Card: Both players swap their bank balances.
        Forward Card: Give all your money to the other player.
        Backward Card: Take all the money from the other player.
        Bomb Card: Your bank balance resets to $0.



"""

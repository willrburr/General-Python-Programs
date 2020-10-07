# ---------------------------------------
# Simulate a modified Liberty Bell Slot Machine.
# ---------------------------------------

import random

# Constants that represent the result of spinning a reel
DIAMOND = 1
HEART = 2
SPADE = 3
HORSESHOE = 4
LIBERTY_BELL = 5

# ---------------------------------------
# spin_payout
# ---------------------------------------
# reel_1: the symbol on the first reel, an integer constant
# reel_2: the symbol on the second reel, an integer constant
# reel_3: the symbol on the third reel, an integer constant
# ---------------------------------------
# Returns an integer, the payout of the spin
# ---------------------------------------

""" The missing spin_payout function goes here ... """


def spin_payout(reel_1, reel_2, reel_3):
    ValueWon = 0
    ReelArray = [reel_1, reel_2, reel_3]
    ReelArray.sort(reverse=True)

    if reel_1 == 5 and reel_2 == 5 and reel_3 == 5:
        ValueWon = 50
    elif reel_1 == 2 and reel_2 == 2 and reel_3 == 2:
        ValueWon = 40
    elif reel_1 == 1 and reel_2 == 1 and reel_3 == 1:
        ValueWon = 30
    elif reel_1 == 3 and reel_2 == 3 and reel_3 == 3:
        ValueWon = 20
    elif reel_1 == 4 and reel_2 == 4 and reel_3 == 4:
        ValueWon = 10
    elif ReelArray[0] == 4 and ReelArray[1] == 4 and ReelArray[2] == 1:
        ValueWon = 5
    elif ReelArray[0] == 4 and ReelArray[1] == 4 and ReelArray[2] == 2:
        ValueWon = 5
    elif ReelArray[0] == 4 and ReelArray[1] == 4 and ReelArray[2] == 3:
        ValueWon = 5
    elif ReelArray[0] == 4 and ReelArray[1] == 4 and ReelArray[2] == 5:
        ValueWon = 5
    else:
        ValueWon = 0

    return ValueWon


# ---------------------------------------
# convert
# ---------------------------------------
# reel: the symbol on a reel, an integer constant
# ---------------------------------------
# Returns a string, the printing value of integer
# ---------------------------------------

def convert(reel):
    if reel == DIAMOND:
        return "diamond"
    elif reel == HEART:
        return "heart"
    elif reel == SPADE:
        return "spade"
    elif reel == HORSESHOE:
        return "horseshoe"
    elif reel == LIBERTY_BELL:
        return "bell"
    else:
        return "error!"


# ---------------------------------------
# test_known_spin
# ---------------------------------------
# reel_1: the symbol on the first reel, an integer constant
# reel_2: the symbol on the second reel, an integer constant
# reel_3: the symbol on the third reel, an integer constant
# ---------------------------------------
# Display a message that shows the spin and its payout
# ---------------------------------------

def test_known_spin(reel_1, reel_2, reel_3):
    message = "{:10}".format(convert(reel_1))
    message += "{:10}".format(convert(reel_2))
    message += "{:10}".format(convert(reel_3))
    message += "{:-6d}".format(spin_payout(reel_1, reel_2, reel_3))
    print(message)


# ---------------------------------------
# test_known_spins
# ---------------------------------------
# For testing purposes, evaluate a variety of known spins
# ---------------------------------------

def test_known_spins():
    print("{:10}{:10}{:10}{}".format("REEL 1", "REEL 2", "REEL 3", "PAYOUT"))
    print("{:10}{:10}{:10}{}".format("------", "------", "------", "------"))
    test_known_spin(LIBERTY_BELL, LIBERTY_BELL, LIBERTY_BELL)
    test_known_spin(HEART, HEART, HEART)
    test_known_spin(DIAMOND, DIAMOND, DIAMOND)
    test_known_spin(SPADE, SPADE, SPADE)
    test_known_spin(HORSESHOE, HORSESHOE, HORSESHOE)
    test_known_spin(HORSESHOE, HORSESHOE, HEART)
    test_known_spin(HORSESHOE, DIAMOND, HORSESHOE)
    test_known_spin(SPADE, HORSESHOE, HORSESHOE)
    test_known_spin(HEART, HEART, HORSESHOE)
    test_known_spin(LIBERTY_BELL, DIAMOND, SPADE)


# ---------------------------------------
# simulate
# ---------------------------------------
# how_many: the number of spins to take, an integer
# ---------------------------------------
# Simulate the Liberty Bell Slot Machine being played
# how_many times.  Calculate and print the expected winnings.
# ---------------------------------------

""" The missing simulate function goes here ... """


def simulate(how_many):
    SymbolList = [LIBERTY_BELL, HEART, DIAMOND, SPADE, HORSESHOE]
    AmountWon = 0
    i = 0

    while i <= how_many:
        DisplayedSymbols = random.choices(SymbolList, k=3)
        # print(DisplayedSymbols)
        AmountWon += spin_payout(DisplayedSymbols[0], DisplayedSymbols[1], DisplayedSymbols[2])
        i += 1

    print(AmountWon)
    print(how_many)
    AmountWon = AmountWon / how_many
    print("For every $1 spent, you can expect to win {:.2f}.".format(AmountWon))


# ---------------------------------------
# main - controls the main flow of logic
# ---------------------------------------

def main():
    print("Program 1: Liberty Bell Slot Machine Simulation\n")
    print("--> Part 1: Testing Known Spins\n")
    test_known_spins()
    print("\n--> Part 2: Simulating 500,000 Spins\n")
    simulate(500000)


# ---------------------------------------

main()

#############################################
#####            VENTURE VOID           #####
#############################################
import os, time, random
def titlecard():
    print("\n.------. .------. .------. .------. .------. .------. .------.")
    print("|V.--. | |E.--. | |N.--. | |T.--. | |U.--. | |R.--. | |E.--. |")
    print("| (\\/) | | (\\/) | | (\\/) | | (\\/) | | (\\/) | | (\\/) | | (\\/) |")
    print("|  \\/  | |  \\/  | |  \\/  | |  \\/  | |  \\/  | |  \\/  | |  \\/  |")
    print("| '--'V| | '--'E| | '--'N| | '--'T| | '--'U| | '--'R| | '--'E|")
    print("`------' `------' `------' `------' `------' `------' `------'\n\n")

def title():
    time.sleep(1)
    print("                  V - E - N - T - U - R - E             \n\n")
    time.sleep(1)
    print("                  - - - - - - V - O - I - D             \n\n")
    time.sleep(1)

def goodbye():
    print("   That's enough venturin' for now ... adios!      \n")
    time.sleep(1)
    print("                  G - A - M - E - - - - - -             \n\n")
    time.sleep(1)
    print("                  - - - - - - O - V - E - R             \n\n")

    title()
    quit()

def q_continue():
    while True:
        choice = ""
        choice = input("  Would you like to continue? (Y/N) --> ")
        if choice.lower() == 'y':
            break
        elif choice.lower() == 'n':
            print("Uhhh .... OK?")
            continue
        else:
            print("I think there's been a problem, see!")
            quit()

def diceRoll(sides):
    return random.randint(1, sides)
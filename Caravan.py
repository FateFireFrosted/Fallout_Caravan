# Author: Dominic Fate
# Date: 4/18/2024
# Desc: A simple python script to play caravan from fallout new vegas within the terminal. Not as simple as I had hoped it to be

# Dictionary that enables both building and looking up point values of each card
Deck = {
    "AD": 1,
    "AC": 1,
    "AH": 1,
    "AS": 1,
    "2D": 2,
    "2C": 2,
    "2H": 2,
    "2S": 2,
    "3D": 3,
    "3C": 3,
    "3H": 3,
    "3S": 3,
    "4D": 4,
    "4C": 4,
    "4H": 4,
    "4S": 4,
    "5D": 5,
    "5C": 5,
    "5H": 5,
    "5S": 5,
    "6D": 6,
    "6C": 6,
    "6H": 6,
    "6S": 6,
    "7D": 7,
    "7C": 7,
    "7H": 7,
    "7S": 7,
    "8D": 8,
    "8C": 8,
    "8H": 8,
    "8S": 8,
    "9D": 9,
    "9C": 9,
    "9H": 9,
    "9S": 9,
    "10D": 10,
    "10C": 10,
    "10H": 10,
    "10S": 10,
    "JD": 10,
    "JC": 10,
    "JH": 10,
    "JS": 10,
    "QD": 10,
    "QC": 10,
    "QH": 10,
    "QS": 10,
    "KD": 10,
    "KC": 10,
    "KH": 10,
    "KS": 10,
    "JOKA": 0,
    "JOKB": 0
}

# Class to hold the game state
class GameState:
    # Board setup for a game. Each player has 3 caravans within which cards can be added to from players hand

    # Constructor Method
    def __init__(self, botD, playerD):
        # This is the six caravans
        self.PlayerSide1 = self.Caravan()
        self.PlayerSide2 = self.Caravan()
        self.PlayerSide3 = self.Caravan()
        self.BotSide1 = self.Caravan()
        self.BotSide2 = self.Caravan()
        self.BotSide3 = self.Caravan()

        # Player's and Bot's hands
        self.PlayerHand = []
        self.BotHand = []

        # Round Decks, This holds what cards are left in the deck to still draw from.
        self.PlayerRoundDeck = playerD
        self.BotRoundDeck = botD

    # Class to store acceding or descending caravans
    class Caravan:
        def __init__(self):
            self.Direction = ""
            self.Suit = ""
            self.Cards = []
            self.Value = 0

# Looks for key value in dictionary
def SearchDeck(DeckDict, Search):
    if Search in DeckDict:
        return 1
    else:
        return 0

# Looks for value in list
def SearchList(List, Search):
    rVal = List.count(Search)
    return rVal

# Constructor that creates the users Deck
def CreatePlayerDeck(PlayerDeck):
    Confirm = 0
    print("\n\nPlease enter a card you would like to add to your deck.\nWARNING once added you cannot remove it\n\nYou can have 5 copies of each card\nFORMAT: <card name><suite>\n")
    print("Example: AD, This is the ace of diamonds\nCards are:\nA - ace\n1-10 - Numbered cards 1-10\nJ - Jack\nQ - Queen\nK - King\nJok - Joker\nWARNING: FORMAT: JOKA and JOKB\n")
    print("Suits: D - Diamonds, C - Clubs, H - Hearts, S - Spades\n")
    while Confirm == 0:
        UserCard = input('Enter Card: ') #grabs the card entered if it is in the deck and not in hand 2 times add it to players deck.
        UserCard = UserCard.upper()
        if SearchDeck(Deck, UserCard):
            if SearchList(PlayerDeck, UserCard) < 5:
                PlayerDeck.append(UserCard)
                print("Success: Card Accepted")
                print(PlayerDeck)
            else:
                print("FAULT: Check rules please, Only 5 copies of each card")
        else:
            print("FAULT: Invalid card type: check rules again or look at the key values in the python code")

        #check if user is done and above 30
        if len(PlayerDeck) == 270:
            print("Deck at max size starting game now.")
            Confirm = 1
        elif len(PlayerDeck) >= 30:
            print("The player Deck is now bigger than 30 and can be played\n")
            con = input("Type Y to play, Or N to keep picking cards: ")
            con = con.lower()
            if con == "y" or con == "yes" or con == "y " or con == "yes  ":
                Confirm = 1

def DecideDeck(CDECK): #TODO make this return with success or failure to make sure a deck is selected
    ImportDECK = input("Do you want to Import a Caravan Deck? Y/N: ")
    if ImportDECK.lower() == "n":
        MakeDECK = input("Do you want to make a Caravan Deck? Y/N: ")
        if MakeDECK.lower() == "y":
            CreatePlayerDeck(CDECK)
            NameCreatedDeck = input("What do you want to name this deck: ") #This area creates a deck. Pretty complicated
            NameCreatedDeck = NameCreatedDeck + ".txt"
            WFP = open(NameCreatedDeck, "w")
            for line in CDECK:
                WFP.write("%s\n" % line)
            WFP.close()
            #Assumes that this works. But it will take the name and put a text file in the folder that the application resides in.
            #Sorry That I don't do error checking I cannot be bothered atm
        else:
            print("Selecting default deck")
            default = open('default.txt', 'r') # Opens the default deck and puts it into the current deck
            Lines = default.readlines()

            # Put the info in the deck
            for Entry in Lines:
                Entry = Entry.strip()
                CDECK.append(Entry)


    else:
        GrabDeck = input("Enter File Path for Caravan Deck: ") #grabs a deck from path
        NewDeck = open(GrabDeck, 'r')  # Opens the default deck and puts it into the current deck
        Lines = NewDeck.readlines()

        # Put the info in the deck
        for Entry in Lines:
            Entry = Entry.strip()
            CDECK.append(Entry)

#~~~~~~~~~~~~~~~~~~~ Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Player's and Bot's deck that must be filled out to at least 30 cards min.
PlayerDeck = []
BotDeck = []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# First we must ask if they want to use the default deck or import one
print("What do you want to do for your own Deck?")
DecideDeck(PlayerDeck)
# What should we do with the second players Deck
print("What do you want to do for the second Deck?")
DecideDeck(BotDeck)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Game Start ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#TODO Implement the actual game

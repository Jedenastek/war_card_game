import random

signs = ["♣", "♦", "♥", "♠"]
values = [i for i in range(2,15)]

#display ascii art cards
def ascii_cards_print(card):
    try:
        if card[1] < 2 or card[1] > 14:
            raise(ValueError)
        elif card[0] not in ["♣", "♦", "♥", "♠"]:
            raise(ValueError)
        drawn_card = list(card)
        if drawn_card[1] == 11:
            drawn_card[1] = "J"
        elif drawn_card[1] == 12:
            drawn_card[1] = "Q"
        elif drawn_card[1] == 13:
            drawn_card[1] = "K"
        elif drawn_card[1] == 14:
            drawn_card[1] = "A"
        string = ''
        strNonDealerHand = []
        if drawn_card[1] == 10:
                non_dealer_card = """
        ┌─────────┐
        │{}       │
        │         │
        │         │
        │    {}    │
        │         │
        │         │
        │       {}│
        └─────────┘""".format(drawn_card[1], drawn_card[0], drawn_card[1]).split('\n')
                strNonDealerHand.append(non_dealer_card)
        else:
            non_dealer_card = """
        ┌─────────┐
        │{}        │
        │         │
        │         │
        │    {}    │
        │         │
        │         │
        │        {}│
        └─────────┘""".format(drawn_card[1], drawn_card[0], drawn_card[1]).split('\n')
            strNonDealerHand.append(non_dealer_card)

        for i in zip(*strNonDealerHand):
            string = string + "\n" + " ".join(i)

        print(string)
        return 1
    except(ValueError):
        return 0

def war(c2_cards, p2_cards, war_rounds, p_points, c_points):
    try:
        war_cards_c = []
        war_cards_p = []
        war_rounds = war_rounds + 1

        print("War!!!")
        print("Computer cards:")
        for card in c2_cards:
            if card[1] < 2 or card[1] > 14:
                raise(ValueError)
            elif card[0] not in ["♣", "♦", "♥", "♠"]:
                raise(ValueError)
            else:
                ascii_cards_print(card)
                war_cards_c.append(card)

        print("Player cards:")
        for card in p2_cards:
            if card[1] < 2 or card[1] > 14:
                raise(ValueError)
            elif card[0] not in ["♣", "♦", "♥", "♠"]:
                raise(ValueError)
            else:
                ascii_cards_print(card)
                war_cards_p.append(card)

        if (war_cards_c[1])[1] < (war_cards_p[1])[1]:
            verdict = "Player won!"
            p_points = p_points + 1
        elif (war_cards_c[1])[1] == (war_cards_p[1])[1]:
            return war_rounds, 0
        else:
            verdict = "Computer won!"
            c_points = c_points + 1

        return war_rounds, verdict
    except ValueError:
        return 0

def initialize():
    try:
        d = Deck()
        d.shuffle()
        first_h, second_h=d.split_deck()

        computer = Player("Computer", Hand(first_h))
        human = Player(input("What's your name: "), Hand(second_h))

        return computer, human
    except:
        return 0

#make class deck
class Deck:
    def __init__(self):
        self.cards = [(i, j) for j in values for i in signs]

    #shuffle cards in a deck
    def shuffle(self):
        random.shuffle(self.cards)

    #split deck and give to each hand (bot and player)
    def split_deck(self):
        return (self.cards[26:], self.cards[:26])

#make class hand
class Hand:
    def __init__(self, cards_quantity):
        self.quantity = cards_quantity

    #return number of cards
    def __str__(self):
        return "Contains {} cards".format(len(self.quantity))

    #adding cards to hand
    def add(self, added_card):
        self.quantity.extend(added_card)

    #remove card from hand
    def remove(self):
        return self.quantity.pop()


#make class player
class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    #check if player still has cards
    def cards_in_hand(self):
        return len(self.hand.quantity) != 0

    #playing a card
    def play_card(self):
        drawn_card = list(self.hand.remove())
        return drawn_card

    #remove war cards
    def remove_war_cards(self):
        cards_war = []
        if len(self.hand.quantity) < 3:
            return self.hand.quantity
        else:
            for _ in range(2):
                cards_war.append(self.hand.quantity.pop())
            return cards_war

    def still_has_cards(self):
        return len(self.hand.quantity) != 0


def main():
    computer, human = initialize()

    rounds_count = 0
    war_rounds = 0
    p_points = 0
    c_points = 0

    while human.cards_in_hand() and computer.cards_in_hand():
        rounds_count += 1
        print("-------------------------------")
        print("\tNEW ROUND")
        print("-------------------------------")
        print("Here are the current standings")
        print(human.name + " has " + str(len(human.hand.quantity)) + " cards")
        print(f"{human.name} have {p_points} points")
        print(computer.name + " has " + str(len(computer.hand.quantity)) + " cards")
        print(f"{computer.name} have {c_points} points")
        print("Let's begin!")

        c_card = computer.play_card()
        print(f"\n{computer.name} played:")
        ascii_cards_print(c_card)

        p_card = human.play_card()
        print(f"\n{human.name} played:")
        ascii_cards_print(p_card)

        #check wich card is higher
        if c_card[1] > p_card[1]:
            print("Computer won!")
            c_points = c_points + 1
        elif c_card[1] == p_card[1]:
            c2_cards = computer.remove_war_cards()
            p2_cards = human.remove_war_cards()
            war_rounds, verdict = war(c2_cards, p2_cards, war_rounds, p_points, c_points)
            print(verdict)
        else:
            print("Player won!")
            p_points = p_points + 1

        game = input("Do you want to start the next round?(Y/N): ").lower()
        if game == 'y' or game == 'yes':
            continue
        else:
            break


    print("Game over!, number of rounds: "+str(rounds_count))
    print("A war happened " + str(war_rounds) +" times")
    print("Here are the final standings")
    print(human.name + " has " + str(len(human.hand.quantity)) + " cards")
    print(f"{human.name} have {p_points} points")
    print(computer.name + " has " + str(len(computer.hand.quantity)) + " cards")
    print(f"{computer.name} have {c_points} points")

if __name__ == "__main__":
    main()

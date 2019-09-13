# BlackJack game
from functools import reduce
import random

ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♠", "♡", "♣", "♢"]

# create a Card
class Card:
    def __init__(self, suit, rank, face_up=True):
        self.suit = suit
        self.rank = rank
        face_up = face_up

    def __repr__(self):
        return f"{self.suit}{self.rank}"


# create the Deck
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def take_card(self):
        return self.deck.pop(0)

    def __str__(self):
        return str(self.deck)


class Player_account:
    def __init__(self, balance=2000, bet=100):
        self.balance = balance
        # self.bet = bet

    def bet_withdraw(self, bet_amount):
        self.balance -= bet_amount

    def win_top_up(self, bet_amount):
        self.balance += 2 * bet_amount

    def lose_withdraw(self, bet_amount):
        self.balance -= bet_amount

    def __str__(self):
        return f"Your balance is ${self.balance}"


def take_bet():
    global bet_amount
    while not (bet_amount <= account.balance and bet_amount != 0):
        try:
            bet_amount = int(input("\nPlace your bet:"))

        except ValueError:
            print("Sorry, you don't have such a balance")


def deal():
    dealer_hand.add(playing_deck.take_card())
    player_hand.add(playing_deck.take_card())
    dealer_hand.add(playing_deck.take_card())
    player_hand.add(playing_deck.take_card())
    print(f"\nDealer has: \n'Hole card', {dealer_hand.cards[1]}")
    print(player_hand)


class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def count(self):
        global hand_value
        ranks_list = list(map(lambda current_card: current_card.rank, self.cards))
        value_list = [
            (
                10
                if (x == "Q" or x == "J" or x == "K")
                else (1 if (x == "A") else int(x))
            )
            for x in ranks_list
        ]
        # value_list = [0 if (x == "A") else int(x) for x in ranks_list]
        hand_value = reduce(lambda a, b: a + b, value_list)
        if hand_value < 10 or len(self.cards) == 2:
            value_list = [11 if (x == 1) else x for x in value_list]
            hand_value = reduce(lambda a, b: a + b, value_list)
        return hand_value

    def __str__(self):
        return f"\nHand is {self.cards}"


def check_if_win():
    if player_hand.count() < 21:
        pass
    elif player_hand.count() == 21:
        print("You win!")
    else:
        print(f"\nBust! You have lost ${bet_amount}")
        print(account)


def hit():
    while player_hand.count() < 21:
        check_if_win()
        hit = input("\nWould you like to hit? - [yes/no]: ").lower()
        if hit in ["yes", "y"]:
            player_hand.add(playing_deck.take_card())
            player_hand.count()
            print(player_hand)
            check_if_win()
        if hit in ["no", "n"]:
            print(f"Player stands. Your score is {hand_value}.")
            dealer_play()
            break


def dealer_play():
    print("Dealer turn!")
    print(dealer_hand)
    while True:
        dealer_hand.count()
        print(f"Dealer score is {hand_value}")
        if dealer_hand.count() <= 17:
            print("\nDealer takes one more card.")
            dealer_hand.add(playing_deck.take_card())
            dealer_hand.count()
            print(dealer_hand)
        elif dealer_hand.count() == player_hand.count():
            print("Push!")
            account.win_top_up(bet_amount / 2)
            print(account)
            break
        elif dealer_hand.count() > player_hand.count() and dealer_hand.count() > 21:
            print("You win!")
            account.win_top_up(bet_amount)
            print(account)
            break
        else:
            print("Dealer wins!")
            print(account)
            break


print("Hello! Welcome to BlackJack game! \nYour starting balance is $2000.")
account = Player_account()
while True:
    bet_amount = 0
    hand_value = 0
    playing_deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    if account.balance > 0:
        take_bet()
        account.bet_withdraw(bet_amount)
        playing_deck.shuffle()
        deal()
        check_if_win()
        hit()
        player_hand.count()
    else:
        print("You have lost all your money! The game is over!")
        break


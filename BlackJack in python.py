import os
import random

the_deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4
def deal(the_deck):
        hand = []
        for i in range(2):
                random.shuffle(the_deck)
                card= the_deck.pop()       
                if card==11:
                      card1 = 'Jack'
                if card==12:
                      card1 = 'Queen'
                if card==13:
                      card1 = 'King'
                if card==14:
                      card1 = 'Ace'
                hand.append(card)
        return hand
def play_again():
      again = input("Do you want to play? (Y/N): ").lower()
      if again == "y":
            dealer_hand = []
            player_hand = []
            the_deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4
            game()
      else:
            print("Thanks for playing!")
            exit()
      
def total(hand):
      total= 0
      for card in hand:
            if card == 11 or card ==12 or card == 13:
                    total = total+10
            elif card == 14:
                    if total >= 11:
                            total = total + 1
                    else:
                            total = total + 11
            else: total = total + card
      return total

def hit(hand):
      card = the_deck.pop()
      if card == 11:
              card1 = "J"
      if card == 12:
              card1 = "Q"
      if card == 13:
              card1 = "K"
      if card == 14:
              card1 = "Ace"
      hand.append(card)
      return hand

def print_results(dealer_hand, player_hand):
      print("The dealer has a ",str(dealer_hand),"for a total of ",str(total(dealer_hand)))
      print("You have a ",str(player_hand)," for a total of ",str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
      if total(player_hand) == 21:
              print_results(dealer_hand, player_hand)
              print("Congratulations! You got a Blackjack!\n")
              play_again()
      elif total(dealer_hand) == 21:
              print_results(dealer_hand, player_hand)
              print("Sorry, you lose. The dealer got a blackjack.\n")
              play_again()
def score(dealer_hand, player_hand):
      if total(player_hand) == 21:
              print_results(dealer_hand, player_hand)
              print("Congratulations! You got a Blackjack!\n")
      elif total(dealer_hand) == 21:
              print_results(dealer_hand, player_hand)
              print("Sorry, you lose. The dealer got a blackjack.\n")
      elif total(player_hand) > 21:
              print_results(dealer_hand, player_hand)
              print("Sorry. You busted. You lose.\n")
      elif total(dealer_hand) > 21:
              print_results(dealer_hand, player_hand)
              print("Dealer busts. You win!\n")
      elif total(player_hand) < total(dealer_hand):
              print_results(dealer_hand, player_hand)
              print("Sorry. Your score isn't higher than the dealer. You lose.\n")
      elif total(player_hand) > total(dealer_hand):
              print_results(dealer_hand, player_hand)
              print("Congratulations. Your score is higher than the dealer. You win\n")
def game():
      
      choice = 0
      print("WELCOME TO BLACKJACK!\n")
      dealer_hand = deal(the_deck)
      player_hand = deal(the_deck)
      p1=[]
      while choice != "q":
            
            print("The dealer is showing a " + str(dealer_hand[0]))
            for i in player_hand:
                  p1.append(i)
                  if i == 11:
                        p1.append("Jack")
                  if i == 12:
                        p1.append("Queen")
                  if i == 13:
                        p1.append("King")
                  if i == 14:
                        p1.append("Ace")
            print("You have a",p1," for a total of " + str(total(player_hand)))
            blackjack(dealer_hand, player_hand)
            choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
            if choice == "h":
                    hit(player_hand)
                    while total(dealer_hand) < 17:
                            hit(dealer_hand)
                    score(dealer_hand, player_hand)
                    play_again()
            elif choice == "s":
                    while total(dealer_hand) < 17:
                            hit(dealer_hand)
                    score(dealer_hand, player_hand)
                    play_again()
            elif choice == "q":
                    print("Bye!")
                    exit()
play_again()


                

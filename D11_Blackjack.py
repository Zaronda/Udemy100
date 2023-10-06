############### Blackjack Project #####################
import random
def play_game():
    
    is_game_over = False

    #Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
    #11 is the Ace.

    def deal_card():
        """ returns a random card from the deck """
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []

    #Create a function called calculate_score() that takes a List of cards as input 
    #and returns the score. 
    def calculate_score(cards):
    #Inside calculate_score() check for blackjack (a hand with only 2 cards: ace + 10) 
    # and return 0 instead of the actual score. 
    # 0 will represent a blackjack in our game.
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        
    # Inside calculate_score() check for an 11 (ace). 
    # If the score is already over 21, remove the 11 and replace it with a 1. 
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
 
        def compare(user_score, computer_score):
        ### compare user and computer scores ###
            result = ""
            #Bug fix. If you and the computer are both over, you lose.
            if user_score > 21 and computer_score > 21:
                return "You went over. You lose 😤"
            
            if user_score == computer_score:
                result = "draw"
                return result
            elif computer_score == 0:
                return "Lose, oponent has Blackjack."
            elif user_score == 0:
                return "Win with a Blackjack."
            elif user_score > 21:
                return "You went over. You lose."
            elif computer_score > 21:
                return "Oponent went over. You win."
            elif user_score > computer_score:
                return "You win."
            else:
                return "You lose."

        compare(user_score, computer_score)

        return sum(cards)

    for _ in range(2):
    #    new_card = deal_card()  - individual lines OR
    #    user_cards.append(new_card) - consolidated line below
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

    # Call calculate_score(). 
    # If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards) 
        computer_score = calculate_score(computer_cards) 
        # debugging print statements 
        print(f"Your cards {user_cards} Your score {user_score}")
        print(f"Computers first card {computer_cards[0]}")
        print (f"computer score {computer_score}")

        if computer_score == 0 or user_score== 0 or user_score > 21:
            is_game_over = True
        else:
                #If the game has not ended, ask the user if they want to draw another card.
        #  If yes, then use the deal_card() function to add another card to the user_cards List. 
        # If no, then the game has ended.
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

        #Hint 11: The score will need to be rechecked with every new card drawn 
        # and the checks in Hint 9 need to be repeated until the game ends.

        # Once the user is done, it's time to let the computer play.
        #  The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand {user_cards}, your score {user_score} ")
    print(f"Your oponents hand {computer_cards}, oponents score {computer_cards} ")
    print(compare(computer_score, user_score))        
        
    # Ask the user if they want to restart the game. 
    # If they answer yes, start a new game of blackjack.
while input("Do you want to play Blackjack? 'y' or 'n' ") == "y":
    play_game()


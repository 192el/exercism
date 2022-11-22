def value_of_card(card):
    facecards = ['J', 'Q', 'K']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
    if card in facecards:
        return 10
    elif card == 'A':
        return 1
    elif card in numbers:
        return int(card)



def higher_card(card_one, card_two):
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_one) < value_of_card(card_two):
        return card_two
    if value_of_card(card_one) == value_of_card(card_two):
        return card_one, card_two




def value_of_ace(card_one, card_two):
    total = value_of_card(card_two) + value_of_card(card_one)
    if total == 3:
        return 1
    elif total + 11 <= 21:
        return 11
    else:
        return 1




def is_blackjack(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    if card_one == 'A' and value_of_card(card_two) == 10:
        return True
    elif card_two == 'A' and value_of_card(card_one) == 10:
        return True
    if total == 21:
        return True
    else:
        return False




def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    else:
        return False




def can_double_down(card_one, card_two):
    total = (value_of_card(card_one) + value_of_card(card_two))
    if total == 9 or total == 10 or total == 11:
        return True
    else:
        return False

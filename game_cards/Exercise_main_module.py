from CardGame import CardGame


name1 = input("enter the first player's name: ")
name2 = input("enter the second player's name: ")
cards_to_deal = input("enter how many cards to deal: ")
if cards_to_deal.isnumeric():
    game = CardGame(name1, name2, int(cards_to_deal))
else:
    game = CardGame(name1, name2)
print(game)

for i in range(10):
    p1card = game.p1.get_card()
    p2card = game.p2.get_card()
    if p1card > p2card:
        print(f"{game.p1.name}'s card is: {p1card}\n"
              f"{game.p2.name}'s card is: {p2card}\n"
              f"and the winner of the round is:{p1card}  ")
        game.p2.add_card(p1card)
        game.p2.add_card(p2card)

    else:
        print(f"{game.p1.name}'s card is: {p1card}\n"
              f"{game.p2.name}'s card is: {p2card}\n"
              f"and the winner of the round is:{p2card}  ")
        game.p1.add_card(p1card)
        game.p1.add_card(p2card)

winner = game.get_winner()
if winner is None:
    print("It's a Tie!!")
else:
    print(f"the winner is {winner}")



import random
money = 100

# Flip Coin Function
def flip_coin(bet, guess):
    flip = random.randint(0,1)
    if flip == 0 and guess
        
        money += bet
        print("You guessed right! It is " +guess+ ". Your new balance is " +money+ ".")
    if flip == 1 and guess == tails:
        money += bet
        print("You guessed right! It is " +guess+ ". Your new balance is " +money+ ".")
    else: 
        money -= bet
        print("You guessed wrong! Your new balance is " +money+ ".")

print(flip_coin(10, heads))
print(flip_coin(10, tails)
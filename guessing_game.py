import random


class GuessingGame:
    def __init__(self, answer):
        self.answer = answer

    #create guess
    def guess(self, user_guess):
        if user_guess > self.answer:
            return 'high'
        elif user_guess < self.answer:
            return 'low'
        else:
            return 'correct'

    #created solved
    def solved(self):
        if last_result == 'correct':
            return True
        return False


# ----- DRIVER CODE -----
game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

print(game.answer)
while game.solved() == False:
    if last_guess != None: 
        print(f"Oops! Your last guess \"{last_guess}\" was {last_result}.")
        print("")
  
    last_guess  = int(input("Enter your guess: "))
    last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")


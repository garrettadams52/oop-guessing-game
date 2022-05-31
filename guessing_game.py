import random


class GuessingGame:
    def __init__(self, answer):
        self.answer = answer

    #create guess
    @classmethod
    def guess(cls, user_guess):
        if int(user_guess) > game.answer:
            return 'high'
        elif int(user_guess) < game.answer:
            return 'low'
        else:
            return 'correct'

    #created solved
    @classmethod
    def solved(cls):
        if last_result == 'correct':
            return True
        return False


# ----- DRIVER CODE -----
game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

#print(game.answer)
while game.solved() == False:
    if last_guess != None: 
        print(f"Oops! Your last guess \"{last_guess}\" was {last_result}.")
        print("")
  
    last_guess  = input("Enter your guess: ")
    last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")


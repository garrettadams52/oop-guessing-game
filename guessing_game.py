import random

class GuessingGame:
    def __init__(self, answer, last_guess, last_result):
        self.answer = answer
        self.last_guess = last_guess
        self.last_result = last_result

    def __str__(self):
        return (f"The answer is {self.answer}, the last guess was {self.last_guess}, and the last result was {self.last_result}")

    #create guess method
    def guess(self):
        if self.last_guess > self.answer:
            return 'high'
        elif self.last_guess < self.answer:
            return 'low'
        else:
            return 'correct'

    #created solved method
    def solved(self):
        return self.last_result == 'correct'


# -------------- DRIVER CODE -----------------
game = GuessingGame(random.randint(1,100), None, None)

while game.solved() == False:
    if game.last_guess != None: 
        print(f"Oops! Your last guess \"{game.last_guess}\" was {game.last_result}.")
        print("")
        #print(game.__str__())
  
    game.last_guess  = int(input("Enter your guess: "))
    game.last_result = game.guess()


print(f"{game.last_guess} was correct!")

"""
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


# ----- DRIVER CODE -----------------
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
"""
""" Exercise 18

Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
Say the number generated by the computer is 1038. An example interaction could look like this:
  Welcome to the Cows and Bulls Game!
  Enter a number:
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...
Until the user guesses the number.
"""

import random

class Generator(object):

    def __init__(self):
        pass

    def gen_number():
        """ Generates game number """
        number = [str(x) for x in random.sample(range(0, 9), 4)]
        return number

class ManageGuesses(object):

    def __init__(self, gamenum):
        self.number = gamenum
        self.numstring = "".join(self.number)

    def get_guesses(self):
        """ Gets guesses, tracks #, and prints results """
        guess_count = 0
        guess = None

        print("Cows are correct numbers in correct positions.\n"
            "Bulls are correct numbers in incorrect positions.\n\n"
            "I have randomly generated a four-digit number.\n"
            "Try and guess it.\n"
            )

        guess = input(">>> ")

        while len(guess) != 4:
            guess = input("Guess not long enough, try again.\n> ")

        while True:
            if guess != self.numstring:
                cows_and_bulls = self.check_guess(self.number, guess)
                guess_count += 1
                print(f"\nCows: {cows_and_bulls['cows']}, Bulls: {cows_and_bulls['bulls']}")
                guess = input("Guess again.\n>>> ")
                continue

            print(f"You guessed my number, {self.numstring}.")
            print(f"You took {guess_count} guesses.")
            break

    def check_guess(self, gamenum, guess):
        """ Logic to assess guess. First identifies cows and discards, then identifies bulls """
        numcows = 0
        numbulls = 0
        zipped = list(zip(guess, gamenum))

        for (x, y) in zipped[::-1]: # why is reverse necessary?
            if x == y:
                zipped.pop(zipped.index((x, y)))
                numcows += 1

        uzguess, uznum = zip(*zipped)

        for x in list(uzguess):
            if x in list(uznum):
                numbulls += 1

        return {'cows': numcows, 'bulls': numbulls}

class PlayGame(object):

    def __init__(self):
        pass

    number = Generator.gen_number()
    gameon = ManageGuesses(number)
    gameon.get_guesses()

play = PlayGame()

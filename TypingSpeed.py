#######################################################################################################################
#
#File Name:         TypingSpeed.py
# Author:           Maxwell Bruce
# Email:            Maxwellwallacebruce@gmail.com
# Description:      Program that checks typing speed of user
#
#######################################################################################################################

import time
import random
import os
import sys

os.system('clear')

class Word:
    def __init__(self):
        with open("Words.txt", "r") as file:
            WordsText = file.read()
            self.ChosenWord = random.choice(list(map(str, WordsText.split())))
    def CheckEqual(self, given_word):
        if given_word.strip() == self.ChosenWord:
            return 1
        else:
            return 0
    def ReturnWord(self):
        return self.ChosenWord
    def ChangeWord(self):
        with open("Words.txt", "r") as file:
            WordsText = file.read()
            self.ChosenWord = random.choice(list(map(str, WordsText.split())))

class Stats:
    def __init__(self, TotalCount):
        self.StartTime = time.perf_counter()
        self.running = 1
        self.WordCount = 0
        self.WordsAttempted = 0
        self.TotalCount = TotalCount
    def Stop(self):
        self.running = 0
        self.EndTime = time.perf_counter()
        self.TimeTaken = self.EndTime-self.StartTime
        print("You took " + str(self.TimeTaken) + " and you answered " + str(self.WordCount) + " correctly!!!")
        self.WordsPerMin = self.WordCount/self.TimeTaken*60
        print("Your words per minute was: " + str(self.WordsPerMin))
    def IncrementTotalWordCount(self):
        self.WordsAttempted += 1
    def IncrementCorrectWordCount(self):
        self.WordCount += 1
    def CheckWordsLeft(self):
        if self.WordsAttempted >= self.TotalCount:
            return 0
        else:
            return 1
    
PreInt = input("How many words would you like to try: ")
try:   
    WordsToTry = int(PreInt)
except ValueError:
    print("Integer value not entered, now exiting")
    sys.exit(0)
os.system('clear')
t = 3
print("Counting down from 3 now")
while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
os.system('clear')
W1 = Word()
S1 = Stats(WordsToTry)
while S1.CheckWordsLeft():
    given_word = input(W1.ReturnWord() + "\n").lower()
    S1.IncrementTotalWordCount()
    if given_word == W1.ReturnWord().lower():
        S1.IncrementCorrectWordCount()
    W1.ChangeWord()
S1.Stop()



    
  
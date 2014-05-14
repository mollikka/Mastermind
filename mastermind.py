#!/usr/bin/env python
#-*- coding:utf-8 -*-

import mastermind_core as core
from sys import stdout
from random import randint


'''
#standard
responses={ "intro":    "Input {0} integers between 1 and {1}",
            "invalid":  "                                ",
            "guess":    " | Next guess: ",
            "hint":     "CP:{0}, CS:{1} | {2} \t",
            "win":      "\n\nYou won in {0} turns!",
          }
'''
#minimal version
responses={ "intro":    "{0} values between 1 and {1}   ",
            "invalid":  "                           ",
            "guess":    " | ",
            "hint":     "{0}:\t{1} {2} | {3} ",
            "win":      "\n\nYou won in {0} turns!",
          }


turncount = 0
stdout.write(responses["intro"].format(core.sequencesize,core.setsize))

while True:
    stdout.write(responses["guess"])
    guess = raw_input()
    guess = guess.replace(" ","")
    if not len(guess) == core.sequencesize:
        stdout.write(responses["invalid"])
        continue
    try:
        guessvalues = [int(c) for c in guess]
    except ValueError:
        stdout.write(responses["invalid"])
        continue
    if not all([1<=i<=core.setsize for i in guessvalues]):
        stdout.write(responses["invalid"])
        continue


    cp_count, cs_count = core.ask_for_hint(guessvalues)

    turncount += 1
    stdout.write(responses["hint"].format(turncount,cp_count,cs_count,guessvalues))

    if cp_count == core.sequencesize:
        stdout.write(responses["win"].format(turncount))
        break

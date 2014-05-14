#!/usr/bin/env python
#-*- coding:utf-8 -*-

from sys import stdout
from random import randint

setsize = 7
sequencesize = 4

sequence = [randint(1,setsize) for i in range(sequencesize)]

turncount = 0

def ask_for_hint(guessvalues):
    cp = [guessvalues[i] == sequence[i] for i in range(sequencesize)]
    cp_count = cp.count(True)

    g = list(guessvalues)
    for i in sequence:
        if i in g: g.remove(i)
    cs_count = sequencesize - len(g)

    cs_count -= cp_count

    return cp_count, cs_count

#Mastermind

This is a simple CLI version of the traditional game: 
https://en.wikipedia.org/wiki/Mastermind_(board_game)

The CLI interface is in the file mastermind.py,
and the game logic is in mastermind_core.py

To run:
```
python mastermind.py
```

This thing only exists because I wanted to play some Mastermind.

Example game:
```
4 values between 1 and 7    | 1122
1:	0 1 | [1, 1, 2, 2]  | 1144
2:	0 1 | [1, 1, 4, 4]  | 3355
3:	0 0 | [3, 3, 5, 5]  | 6677
4:	2 1 | [6, 6, 7, 7]  | 7661
5:	2 1 | [7, 6, 6, 1]  | 7616
6:	3 0 | [7, 6, 1, 6]  | 7617
7:	4 0 | [7, 6, 1, 7] 

You won in 7 turns!
```

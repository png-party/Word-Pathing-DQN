
import random
from re import L
import numpy as np
from sortedcontainers import SortedDict
from sortedcontainers import SortedKeyList
from typeguard import typechecked
    #Generate a random frequency float between 0.0-100, map it to the corresponding letter
letterDictFreq = SortedDict({0.19:"Q", 0.44:"J", 0.71:"X", 1.15:"Z", 2.06:"W", 3.03:"K", 4.03:"V", 5.43:"F", 7.03:"Y", 9.03:"B", 11.3:"H", 14.03:"M",16.83:"P", 19.83:"G", 23.13:"U",26.93:"D", 30.93:"C", 36.24:"L", 42.33:"O", 49.03:"T", 56.23:"N", 63.53:"R", 71.33:"A", 79.93:"I", 89.0:"S", 100.0:"E"})
class Letterboard:
   
    @typechecked
    def __init__(self, cols:int=4, rows:int=4) -> None:
        self.height = cols
        self.width = rows
        self.board = np.full((self.width, self.height), ' ', dtype='<U1') #hold unicode chars of length 1 or less
        for r in range(rows):
            for c in range(cols):
                self.board[r,c] = self.generate_letter()
        print(self.board.shape)
      
    @typechecked
    def generate_letter(self) -> str:
        randomNum = random.randrange(0, 1000)/10.0
        letter = ""
        for key in letterDictFreq.keys():
            if key >= randomNum:
                letter = letterDictFreq[key]
                break
        return letter

    @typechecked
    def print_board(self) ->None:
        print(" ", self.width*"=="*2)
        print(self.board)
        print(" ", self.width*"=="*2)


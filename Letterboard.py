
import numpy as np
from sortedcontainers import SortedDict
from typeguard import typechecked
letterDictFreq = SortedDict({0.19:"Q", 0.44:"J", 0.71:"X", 1.15:"Z", 2.06:"W", 3.03:"K", 4.03:"V", 5.43:"F", 7.03:"Y", 9.03:"B", 11.3:"H", 14.03:"M",16.83:"P", 19.83:"G", 23.13:"U",26.93:"D", 30.93:"C", 36.24:"L", 42.33:"O", 49.03:"T", 56.23:"N", 63.53:"R", 71.33:"A", 79.93:"I", 89.0:"S", 100.0:"E"})
class Letterboard:
    #Generate a random float between 0.0-100 and map it based onth
   
    @typechecked
    def __init__(self, cols:int=4, rows:int=4) -> None:
        self.height = cols
        self.width = rows
    @typechecked
    def fillBoard(self) -> np.ndarray:
        return True
    def generateLetter(self) -> str:
        randomNum = 1
        randomLetter = abs(randomNum - letterDictFreq(letterDictFreq.bisect_left(randomNum)))
        letterDictFreq.bisect_right(randomNum)



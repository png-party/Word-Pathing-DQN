from typeguard import typechecked

from typing import List
from pypruningradixtrie.trie import PruningRadixTrie as radtrie
from pypruningradixtrie.input.abstract_input_provider import AbstractInputProvider
from pypruningradixtrie.input.input import Input

class TextInputProvider(AbstractInputProvider):
    #Input provider that uses .txt as a source (Implementing it from radtrie)
    @staticmethod
    @typechecked
    def read_input_data(file_path:str) ->List[Input]:
        dictionary:List[Input] = [] #using typehints
        try:
            infile = open(file_path, 'r')
            for line in infile:
                line = line.strip() #remove whitespace
                word = Input(query=line, score=1)
                dictionary.append(word)
            infile.close()
        except FileNotFoundError:
            print("File not found!")
            return []
        return dictionary

class Dictionary:
    def __init__(self, title:str="outputUpper190k.txt"):
        self.fileName = title
        #Create and fill radix trie
        self.dictionary = radtrie(self.fileName, TextInputProvider())

    @typechecked
    def valid(self, word:str) -> bool:
       wordNode= self.dictionary._get_node_by_term(word)
       #True if word is found & score is non-zero, meaning its a real word and not word fragment
       return wordNode is not None and wordNode[0].is_word_end
"""Word Finder: finds random words from a dictionary."""

def func_ftkjgizn():
    ...
    return 

import random

class WordFinder:
     def __init__(self, path):
    
    def __init__(self, path):

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

            def parse(self, dict_file):
            
              def random(self):
  


class SpecialWordFinder(WordFinder):
    def parse(self, dict_file):
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]

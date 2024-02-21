
class Progression: #a general iterator class for mathematical progressions

    def __init__(self, start=0):
        self._current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        '''returns next element in iteration'''
        element = self._current
        self._advance() #advances the self._current  private attribute
        return element
    
    def _advance(self):
        '''can be overriden for subclasses to customize progression'''
        self._current = self._current + 1



class ArithProgression(Progression): #subclass for arithmetic progressions

    def __init__(self, incr, start=0):
        super().__init__(start)
        self._incr = incr
    
    def _advance(self):
        '''overrides inherited method'''
        self._current = self._current + self._incr


class FibProgression(Progression): #subclass for Fibonacci progressions

    def __init__(self):
        super().__init__(1)
        self._prev = 0
        
    def _advance(self):
        '''overrides inherited method'''
        self._current, self._prev = (self._current + self._prev), self._current


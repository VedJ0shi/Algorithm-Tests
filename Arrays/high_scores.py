#storing high score entries for a game efficiently

class GameEntry:
    '''represents one entry in a bounded sequence of entries'''
    def __init__(self, name, score):
        self._name = name
        self._score = score
    
    @property
    def name(self):
        return self._name
    
    @property
    def score(self):
        return self._score
    
    def __str__(self):
        return f'{self.name}|{self.score}'

##################################################

class Scoreboard:
    '''sequence of high score entries in order--
    maximum capacity of sequence declared at object construction
    so that underlying array never has to resize'''

    def __init__(self, capacity=10):
        self._board = [None]*capacity
        self._n = 0 #actual number of entries between 0 and capacity
    
    def __getitem__(self, k):
        if k > self._n - 1 : #self._n-1 is the maximum index filled with an entry
            print('scoreboard not fully filled')
        return self._board[k]
    

    def __str__(self):
        return f'{[str(self._board[j]) for j in range(self._n)]}'
    
    def add(self, entry): #expects entry to be a GameEntry obj
        score = entry.score       
        #check if new entry qualifies as a high score
        #answer is True if board not filled OR score greater than min score among existing entries
        qualified = self._n < len(self._board) or score > self._board[-1].score
        
        if qualified: #either new entry needs to be inserted or needs to replace an existing one
            if self._n+1 <= len(self._board): #if no entry needs to be replaced
                self._n = self._n + 1 #number of entries increased by 1
        
            #procedure to insert new qualified entry
            j = self._n - 1 #max entry index
            while j > 0 and score > self._board[j-1].score:
                self._board[j] = self._board[j-1] #shift existing entry to right; replaces None if board not filled
                j = j - 1
            self._board[j] = entry



                
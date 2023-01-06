class ScoreCard():
    
    def __init__( self, card):
        self.card = card
        self.score = 0



    def getTotalScore(self): 
        self.calculateScore() 
        return self.score



    def calculateScore(self):  

        for turn in self.card:

            if turn in "123456789":
                self.score += int(turn)


            if turn == "/":
                self.score += 10




class ScoreCard():
    
    def __init__( self, card):
        self.card = card
        self.spare = False
        self.strike = False
        self.lastNumber = 0
        self.score = 0


    def getTotalScore(self): 
        self.calculateScore() 
        return self.score



    def calculateScore(self):  

        rolls = 0
        i = 0

        for roll in self.card:

            i += 1

            if i == 2:
                rolls += 1
                i = 0

            if roll in "123456789":
                
                if self.spare == False:
                    self.score += int(roll)
                    self.lastNumber = int(roll)
                else: 

                    if rolls == 10:
                        self.score += int(roll)
                    else:
                        self.score += int(roll) * 2
                        self.lastNumber = int(roll)



            if roll == "/":
                self.spare = True
                self.score += 10
                self.score -= self.lastNumber 


            if roll == "-":
                self.score += 0


                
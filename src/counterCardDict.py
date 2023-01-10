class ScoredCard():

    def __init__(self, card):
        self.card = card
        self.score = 0
        self.frames = {0:0, 1:0, 2:0, 3:0,
                       4:0, 5:0, 6:0, 7:0,
                       8:0, 9:0, 10:0}
        self.lastValue = 0

        

    def convertCardIntoDict(self):
      
        self.card = self.card.replace( '-' , "0")
        self.card = self.card.replace('X', 'X'+'0')
        self.card = list(self.card)
        
        if len(self.card) == 21:
            self.card.append('0')

        #Juntamos las tiradas por frames
        frames = []
        for i in range(0, len(self.card),2 ):
            frames.append([self.card[i], self.card[i+1]])

        
        
        #Creamos un diccionario que es el frame con el valor de las tiradas
        dictionary = {}  
        for i in range(0, len(frames)):
            dictionary[i] = frames[i]

        self.card = dictionary

        return self.card



    def calculateScore(self):

        self.card = self.convertCardIntoDict()

        for frame in self.card:
        
            if frame == 10:
                break
            else:
                for roll in self.card[frame]:
                    
                    if roll in "1234567890":
                        self.frames[frame] += int(roll)
                        self.lastValue = int(roll)

                    if roll == "-":
                        self.frames[frame] += 0
                        self.lastValue = 0

                    if roll == "/":
                        self.frames[frame] -= self.lastValue
                        if frame == 9:
                            self.frames[frame] += 10 + int(self.card[10][0])
                        else:
                            self.frames[frame] += 10 + int(self.card[frame+1][0])

                    
                    if roll == "X":
                        self.frames[frame] += 10

                        if self.card[frame+1][0] == "X":
                            self.frames[frame] += 10






                        else:
                            self.frames[frame] += int(self.card[frame+1][0])



                        if self.card[frame+1][1] == "X":
                            self.frames[frame] += 10
                        else:
                            self.frames[frame] += int(self.card[frame+1][1])
                        
                        """
                        Se tensa
                        """


                        



            

    def getTotalScore(self):
        self.calculateScore()
        return sum(self.frames.values())


                
            

    




card = ScoredCard("XX9-9-9-9-9-9-9-9-")
total = 100

print(card.getTotalScore())


class ScoredCard():

    def __init__(self, card):
        self.card = card
        self.score = 0
        self.frames = {0:0, 1:0, 2:0, 3:0,
                       4:0, 5:0, 6:0, 7:0,
                       8:0, 9:0}
        self.lastValue = 0

        

    def convertCardIntoDict(self):

        dictionary = {}        
        self.card = list(self.card)

        #Juntamos las tiradas por frames
        frames = []
        for i in range(0, len(self.card),2 ):
            frames.append([self.card[i], self.card[i+1]])


        #Creamos un diccionario que es el frame con el valor de las tiradas
        for i in range(0, len(frames)):
            dictionary[i] = frames[i]

        self.card = dictionary

        return self.card



    def calculateScore(self):

        self.card = self.convertCardIntoDict()

        for frame in self.card:
        
            for roll in self.card[frame]:
                
                if roll in "123456789":
                    self.frames[frame] += int(roll)
                    self.lastValue = int(roll)

                if roll == "-":
                    self.frames[frame] += 0
                    self.lastValue = 0

                if roll == "/":
                    if frame == 9:
                        self.frames[frame] += 10 + int(self.card[10][0])
                    else:
                        self.frames[frame] += 10 + int(self.card[frame][0])

            
    def getTotalScore(self):
        self.calculateScore()

        return sum(self.frames.values())


                
            

    




card = ScoredCard("12345123451234512345")


print(card.getTotalScore())


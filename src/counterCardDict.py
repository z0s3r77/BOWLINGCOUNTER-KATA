class ScoredCard():

    def __init__(self, card):

        self.card = card
        self.score = 0
        self.resultsPerFrame = {0:0, 1:0, 2:0, 3:0,
                       4:0, 5:0, 6:0, 7:0,
                       8:0, 9:0, 10:0}

        

    def convertCardIntoDict(self):

        #Formateamos el string entrante 
        self.card = self.card.replace( '-' , "0")
        self.card = self.card.replace('X', 'X'+'0')
        self.card = list(self.card)
        

        #Le sumamos un 0 en caso de que haya una tirada de bonus (así salen un array con arrays pares)
        if len(self.card) == 21:
            self.card.append('0')



        #Juntamos las tiradas por parejas
        # ['9', '0', '3', '/', '6', '1', '3', '/', '8', '1', '5', '/', '0', '/', '8', '0', '7', '/', '8', '/', '8', '0']
        # [['9', '0'], ['3', '/'], ['6', '1'], ['3', '/'], ['8', '1'], ['5', '/'], ['0', '/'], ['8', '0'], ['7', '/'], ['8', '/'], ['8', '0']]
        resultsPerFrame = []
        for i in range(0, len(self.card),2 ):
            resultsPerFrame.append([self.card[i], self.card[i+1]])


        
        #Creamos un diccionario que es el frame con el valor de las tiradas
        # [['9', '0'], ['3', '/'], ['6', '1'], ['3', '/'], ['8', '1'], ['5', '/'], ['0', '/'], ['8', '0'], ['7', '/'], ['8', '/'], ['8', '0']]
        # {0: ['9', '0'], 1: ['3', '/'], 2: ['6', '1'], 3: ['3', '/'], 4: ['8', '1'], 5: ['5', '/'], 6: ['0', '/'], 7: ['8', '0'], 8: ['7', '/'], 9: ['8', '/'], 10: ['8', '0']}
        dictionary = {}  
        for i in range(0, len(resultsPerFrame)):
            dictionary[i] = resultsPerFrame[i]


        #Asignamos el valor del diccionario con los frames y  en cada frame las dos tiradas
        self.card = dictionary

        return self.card



    # calculateScore es la suma del valor de los 10 frames
    def calculateScore(self):

        #Convierte el string en diccionario 
        # EJ: {0: ['9', '0'], 1: ['3', '/'], 2: ['6', '1'], 3: ['3', '/'], 4: ['8', '1'], 5: ['5', '/'], 6: ['0', '/'], 7: ['8', '0'], 8: ['7', '/'], 9: ['8', '/'], 10: ['8', '0']}
        self.card = self.convertCardIntoDict()


        # Vamos obteniendo los resultados por frame
        for frame in self.card:        
            if frame == 10:
                break
            else:
                for roll in self.card[frame]:
                    
                    #Si roll es un numero lo sumamos al frame actual
                    if roll in "1234567890":
                        self.resultsPerFrame[frame] += int(roll)


                    #Si roll es un spare, restamos el resultado anterior del numero
                    if roll == "/":
                        self.resultsPerFrame[frame] -= int(self.card[frame][0])
                        #En caso de que la siguiente tirada sea un strike, se suma 10 del strike y 10 del spare
                        #Si no es un strike, se suma el numero de la tirada
                        if self.card[frame+1][0] == "X":
                            self.resultsPerFrame[frame] += 10 + 10
                        else:
                            self.resultsPerFrame[frame] += 10 + int(self.card[frame+1][0])


                    #Si el roll es un strike , se debe de sumar 10, más las dos tiradas que le sigan
                    if roll == "X":
                        self.resultsPerFrame[frame] += 10


                    #Si la siguiente tirada es un strike, sumamos 10 y comprobamos si la siguiente tirada es otro strike
                        if self.card[frame+1][0] == "X":
                            self.resultsPerFrame[frame] += 10

                            if self.card[frame+2][0] == "X":
                                self.resultsPerFrame[frame] += 10   #Aquí tendríamos un total de 30 

                            else:
                                self.resultsPerFrame[frame] += int(self.card[frame+2][0])

                        else:
                            #Como la siguiente tirada no es un strike, sumamos el resultado
                            #Al ser la primera tirada del siguiente frame, no puede ser un spare, será del 0 a 9
                            self.resultsPerFrame[frame] += int(self.card[frame+1][0])


                            #La segunda tirada del frame si puede ser ser un spare, 
                            # en ese caso se suma 10 y se resta el numero anterior
                            if self.card[frame+1][1] == "/":
                                self.resultsPerFrame[frame] += 10 
                                self.resultsPerFrame[frame] -= int(self.card[frame+1][0])
                            else:
                            #En caso de que la segunda tirada no sea un spare, será otro numero
                                self.resultsPerFrame[frame] += int(self.card[frame+1][1])



    def getTotalScore(self):
        #Devuelve los valores de resultsPerFrame
        self.calculateScore()
        
        #Devuelve la suma de todos los frames
        return sum(self.resultsPerFrame.values())


                
            

if __name__ == '__main__':


    def getResult(scoreCard):

        card = ScoredCard(scoreCard)
        return card.getTotalScore()    


    # print(getResult("9-3/613/815/-/8-7/8/8")) debe devolver 131

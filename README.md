# Bownling-Game-Counter
**Indice**
 - [**Explicación del Kata**](##Explicación-del-Kata)
 - [**Metodología**](##Metodología)
 - [**Uso**](##Uso)
    
## Explicación del Kata
Este Kata consiste en contar la puntuación final de una partida de bolos. Al acabar la partida, todas las tiradas se guardan en una carta (en el codigo es la clase __ScoreCard__). 

Dicho *ScoreCard* se pasa al programa Python y obtiene la puntuación total.

## Metodología

Este codigo se ha desarrollado a partir de TDD (Test-Driven-Developmen). El ciclo es el siguiente:

    - Se construyen casos Test
    - Se desarrolla el codigo para cumplir dichos casos
    - Se refactoriza el codigo una vez acabado

Dicho kata y casos test fueron propuestos por @dfleta, el profesor.

## Uso

Una vez clonado el repositorio y ejecutado el archivo setup.py, debemos ejecutar:
```
pytest test/test_bowling_kata.py
```
Esto nos debe pasar todos los casos test, sino es así, asegurate de tener instalado pytest:
```
pip3 install pytest
```
Una vez pasados los tests, podemos ir a counterCardDict.py y añadir el caso que queramos:
```
    def getResult(scoreCard):

        card = ScoredCard(scoreCard)
        return card.getTotalScore()    


    print(getResult("9-3/613/815/-/8-7/8/8")) #Aquí iría el caso en particular 

```

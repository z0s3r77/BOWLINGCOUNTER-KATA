import pytest
from src.counterCard import ScoreCard


def test_TotalScoreHisttingPinsTest():

    #Hitting pins total = 60
    pins = "12345123451234512345"
    total = 60
    scoreCard = ScoreCard(pins)
    assert total == scoreCard.getTotalScore()



def test_TotalScoreHittingPinsFailTest():

    pins = "9-9-9-9-9-9-9-9-9-9-"
    total = 90
    scoreCard = ScoreCard(pins)
    assert total == scoreCard.getTotalScore()

    
    pins = "9-3561368153258-7181"
    total = 82
    scoreCard = ScoreCard(pins)
    assert total == scoreCard.getTotalScore()



# Último punto
def test_TotalScoreSpareTest():
    # pins = "5/5/5/5/5/5/5/5/5/5/5"
    # total = 150
    # scoreCard = ScoreCard(pins)
    # assert total == scoreCard.getTotalScore()

    pins = "9-3/613/815/-/8-7/8/8"
    total = 131
    scoreCard = ScoreCard(pins)
    assert total == scoreCard.getTotalScore()
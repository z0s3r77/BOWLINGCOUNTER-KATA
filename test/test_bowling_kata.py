import pytest
from src.counterCardDict import ScoredCard



def test_0Scores():

    pins = "--------------------"
    total = 0
    scoreCard = ScoredCard(pins)
    assert total == scoreCard.getTotalScore()


def test_TotalScoreHisttingPinsTest():

    pins = "12345123451234512345"
    total = 60
    scoreCard = ScoredCard(pins)
    assert total == scoreCard.getTotalScore()



def test_TotalScoreHittingPinsFailTest():

    pins = "9-9-9-9-9-9-9-9-9-9-"
    total = 90
    scoreCard = ScoredCard(pins)
    assert total == scoreCard.getTotalScore()

    
    pins = "9-3561368153258-7181"
    total = 82
    scoreCard = ScoredCard(pins)
    assert total == scoreCard.getTotalScore()



def test_TotalScoreSpareTest():

    pins = "5/5/5/5/5/5/5/5/5/5/5"
    total = 150
    scoreCard = ScoredCard(pins)
    assert total == scoreCard.getTotalScore()


    pins = "9-3/613/815/-/8-7/8/8"
    total = 131
    scoreCard = ScoredCard(pins)
    assert total == scoreCard.getTotalScore()



def test_TotalScoreStrikeTest():

    pins = "X9-9-9-9-9-9-9-9-9-"
    total = 100
    scoreCard = ScoredCard(pins)
    assert total == scoreCard.getTotalScore()

    pins = "9-9-9-9-9-9-9-9-9-X9-"
    total = 100
    scoreCard = ScoredCard(pins)
    assert total == scoreCard.getTotalScore()

    pins = "X9-X9-9-9-9-9-9-9-"
    total = 110
    scoreCard = ScoredCard(pins)
    assert total == scoreCard.getTotalScore()

    # pins = "XX9-9-9-9-9-9-9-9-"
    # total = 120
    # scoreCard = ScoredCard(pins)
    # assert total == scoreCard.getTotalScore()






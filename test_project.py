from project import ascii_cards_print
from project import initialize
from project import war

def test_ascii_cards_print():
    assert ascii_cards_print(["♣", 20]) == 0
    assert ascii_cards_print(["♣", 10]) == 1
    assert ascii_cards_print(["X", 10]) == 0
    assert ascii_cards_print(["♥", 2]) == 1

def test_war():
    assert war([("♥",10), ("♥",13)], [("♣",14), ("♥",9)], 1, 10, 20) == (2, "Computer won!")
    assert war([("♥",10), ("♥",13)], [("♣",20), ("♥",9)], 0, 10, 20) == 0
    assert war([("♥",10), ("♥",13)], [("♣",14), ("♥",20)], 1, 10, 20) == 0

def test_initialize():
    assert initialize() == 0

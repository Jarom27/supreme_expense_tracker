import database.InitDatabase
from logic.budget import *
import pytest


def verify_connection():
    assert create_database()

def test_difference_between():
    assert differenceBetweenExpectedBudget(2000,3000) == -1000
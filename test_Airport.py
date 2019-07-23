# pythone pytest
from Abstraction import *

import pytest

def test_first_name():
    assert passen_1.first_name == "Adam"

def test_last_name():
    assert passen_1.last_name == "johnson"

def test_age():
    assert passen_1.age == "25"

def test_passport():
    assert passen_1.passport == "british"

def test_first_name2():
    assert passen_2.first_name == "danny"

def test_last_name2():
    assert passen_2.last_name == "shearman"

def test_age2():
    assert passen_2.age == "20"

def test_passport2():
    assert passen_2.passport == "british"
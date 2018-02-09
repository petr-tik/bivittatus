import pytest

from ctrie import cTrie
from py_trie import PyTrie


constructors = [cTrie, PyTrie]


@pytest.mark.parametrize("constructor", constructors)
def test_find_added(constructor):
    tr = constructor()
    tr.add("bob")
    assert tr.find("bob") == 1


@pytest.mark.parametrize("constructor", constructors)
def test_find_incomplete(constructor):
    tr = constructor()
    tr.add("boban")
    assert tr.find("bob") == 0


@pytest.mark.parametrize("constructor", constructors)
def test_find_missing_missing_letter_before(constructor):
    tr = constructor()
    tr.add("bob")
    assert tr.find("alice") == 0


@pytest.mark.parametrize("constructor", constructors)
def test_find_missing_letters_exist_after(constructor):
    tr = constructor()
    tr.add("bob")
    assert tr.find("zlice") == 0


@pytest.mark.parametrize("constructor", constructors)
def test_find_missing_before_add(constructor):
    tr = constructor()
    assert tr.find("me") == 0

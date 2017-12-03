import pytest

from ctrie import cTrie
from py_trie import PyTrie


def test_find_added():
    tr = cTrie()
    tr.add("bob")
    assert tr.find("bob") == 1


def test_find_incomplete():
    tr = cTrie()
    tr.add("boban")
    assert tr.find("bob") == 0


def test_find_missing_missing_letter_before():
    tr = cTrie()
    tr.add("bob")
    assert tr.find("alice") == 0


def test_find_missing_letters_exist_after():
    tr = cTrie()
    tr.add("bob")
    assert tr.find("zlice") == 0


def test_find_missing_before_add():
    tr = cTrie()
    assert tr.find("me") == 0

import pytest

from trie import Trie


def test_find_added():
    tr = Trie()
    tr.add("bob")
    assert tr.find("bob") == 1


def test_find_incomplete():
    tr = Trie()
    tr.add("boban")
    assert tr.find("bob") == 0


def test_find_missing_missing_letter_before():
    tr = Trie()
    tr.add("bob")
    assert tr.find("alice") == 0


def test_find_missing_letters_exist_after():
    tr = Trie()
    tr.add("bob")
    assert tr.find("zlice") == 0


def test_find_missing_before_add():
    tr = Trie()
    assert tr.find("me") == 0

#! /usr/bin/env python3

import subprocess
import time

from py_trie import PyTrie
from ctrie import cTrie


def add_sorted_words(trie_constructor):
    print("\n\n{}".format(trie_constructor.__name__))
    startTime = time.time()
    tr = trie_constructor()
    creationTime = time.time() - startTime
    print("{} takes {}s to instantiate".format(
        trie_constructor.__name__, creationTime))
    with open("clean_words") as f:
        for line in f:
            tr.add(line.strip())
    elapsedTime = time.time() - startTime
    print("It takes {}s to add 18000 words to a {}".format(
        elapsedTime, trie_constructor.__name__))


def add_random_words(trie_constructor):
    print("\n\n{}".format(trie_constructor.__name__))
    startTime = time.time()
    tr = trie_constructor()
    creationTime = time.time() - startTime
    print("{} takes {}s to instantiate".format(
        trie_constructor.__name__, creationTime))
    with open("random_words") as f:
        for line in f:
            tr.add(line.strip())
    elapsedTime = time.time() - startTime
    print("It takes {}s to add 18000 random words to a {}".format(
        elapsedTime, trie_constructor.__name__))


def find_present_words(trie_constructor):
    print("\n\n{}".format(trie_constructor.__name__))
    tr = trie_constructor()
    with open("clean_words") as f:
        for line in f:
            tr.add(line.strip())

    startTime = time.time()
    with open("find_words") as f:
        for line in f:
            tr.find(line.strip())
    elapsedTime = time.time() - startTime
    print("It takes {}s to find 100 random words in a {}".format(
        elapsedTime, trie_constructor.__name__))


def find_missing_words(trie_constructor):
    print("\n\n{}".format(trie_constructor.__name__))
    tr = trie_constructor()

    with open("clean_words") as f:
        for line in f:
            tr.add(line.strip())
    missing_words_name = "missing_words"

    startTime = time.time()
    with open(missing_words_name) as f:
        for line in f:
            tr.find(line.strip())
    elapsedTime = time.time() - startTime
    print("It takes {}s to look for, but fail to find, 800 missing words in a {}".format(
        elapsedTime, trie_constructor.__name__))


if __name__ == "__main__":
    for trie in [cTrie, PyTrie]:
        add_sorted_words(trie)
        add_random_words(trie)
        find_present_words(trie)
        find_missing_words(trie)

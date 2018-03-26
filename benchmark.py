#!/usr/bin/env python3

import time

from py_trie import PyTrie
from ctrie import cTrie

time_fmt = ":5f"


def add_sorted_words(trie_constructor):
    startTime = time.time()
    tr = trie_constructor()
    creationTime = time.time() - startTime
    print("Takes {:5f}s to instantiate before adding sorted words".format(
        creationTime))
    with open("clean_words") as f:
        for line in f:
            tr.add(line.strip())
    elapsedTime = time.time() - startTime
    print("Takes {:5f}s to add 18000 words".format(elapsedTime))


def add_random_words(trie_constructor):

    startTime = time.time()
    tr = trie_constructor()
    creationTime = time.time() - startTime
    print("Takes {:5f}s to instantiate before adding random words".format(
        creationTime))
    with open("random_words") as f:
        for line in f:
            tr.add(line.strip())
    elapsedTime = time.time() - startTime
    print("Takes {:5f}s to add 18000 random words".format(
        elapsedTime))


def find_present_words(trie_constructor):

    tr = trie_constructor()
    with open("clean_words") as f:
        for line in f:
            tr.add(line.strip())

    startTime = time.time()
    with open("find_words") as f:
        for line in f:
            tr.find(line.strip())
    elapsedTime = time.time() - startTime
    print("Takes {:5f}s to find 100 random words".format(
        elapsedTime))


def find_missing_words(trie_constructor):
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
    print("Takes {:5f}s to look for, but fail to find, 800 missing words".format(
        elapsedTime))


if __name__ == "__main__":
    for trie in [PyTrie, cTrie]:
        print(trie.__name__)
        add_sorted_words(trie)
        add_random_words(trie)
        find_present_words(trie)
        find_missing_words(trie)

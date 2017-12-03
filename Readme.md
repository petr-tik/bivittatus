Extending Python with C and benchmarking against equivalent Python code.

## Objective

Find the difference between writing Python code vs compiling C into a shared library. 

## Method

A good comparison is storing and searching strings. A trie data structure is implemented with 2 methods - add and find. 2 implementations - Python and C compiled into a dynamic library loaded by the CPython interpreter are tested and benchmarked against each other to find out their memory footprint and speed. 

While C and the conventions of CPython extension hacking are tricky to get your head around. 

## Test

A pytest harness runs against Trie as imported from the python file or imported from the shared library compiled by distutils. 

## Benchmark

The same text file is fed into the trie implementation. 

### Textfile

#### Alphabetical order

Using a bit of bash magic, we can prepare a lowercase-only, clean of punctuation list of words to feed into our trie.

```bash
head -n 50000 /usr/share/dict/words | tail -n 20000 | tr -d "[A-Z|']" | iconv -f utf8 -t ascii//TRANSLIT | uniq | head -n 18000 > clean_words
```

Take the first 50000 words from unix dictionary fail, take the words from the middle, remove all uppercase letters and apostrophes, convert/transliterate all non-ascii chars to ascii and pipe the top 18000 unique words into the clean_words file


#### Random order

Take the clean_words file from above and shuffle the words around

```bash
shuf clean_words > random_words
```

#### Missing words

```bash
head -n 80000 /usr/share/dict/words | tail -n 1000 | tr -d "[A-Z|']" | iconv -f utf8 -t ascii//TRANSLIT | uniq | head -n 800 > missing_words
```


### Time to add 10000 words 

Absolute time

#### In alphabetic order

#### In random order

### Memory footprint

The size of trie object after all the words have been added.

### Time to find existing words 

Average duration of finding same 50 words that are in the trie

### Time to look for missing words

Average duration of looking for same 50 words that aren't in the trie


## Results

tbd

## Conclusion

Writing C feels hacky and teaches you about many footguns. Kudos to CPython developers for implementing and documenting a huge number of helper methods, class definition tutorials examples and providing a good debugging experience with gdb. 


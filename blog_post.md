Benchmarking the Python and C implementation of a trie-as-a-dictionary. 

## What does C give you over Python?

C is closer to the metal, saves memory for data structures and is compiled. The cTrie is implemented as a struct with 1 trie_node object and the PyObject\_Head that is compulsory for Python extensions. This is lighter on methods and thus memory used than the PyTrie class, which inherits unnecessary methods from the Base Object. 

As far as I know, Python converts variable names to memory addresses, so using pointers in the cTrie implementation doesn't give an advantage over PyTrie.

Characters are the same in C and Python - the CPython interpreter caches useful strings and individual characters are resolved as pointers to the immutable strings of characters. 


## How much infra is there for writing Python extensions in C? 

Loads. The CPython developers are great, there are helper methods to parse arguments passed to the function and cast them to given C types, debug print method, method to build return values and for the method definitions. The documentation is detailed and includes a tutorial, which helps. 


### Debugging

After installing debug symbols

```bash
sudo apt-get install python3.5-dbg
```

Compile the extension with `-g -O0` flags to make sure debug sybmols are avaiable and nothing is optimised out. 

Run the line below (inside emacs or terminal).

```bash
gdb -ex r --args python3 test.py
```

You can step through the programme, look at the backtrace and examine registers. 

## What's inside the shared library

Using readelf (better than objdump according to [this](https://stackoverflow.com/questions/8979664/readelf-vs-objdump-why-are-both-needed)), we can examine the functions of the shared library.


## What performs better - compiled C or Python?

```python
building 'ctrie' extension
creating build
creating build/temp.linux-x86_64-3.5
x86_64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -g -fstack-protector-strong -Wformat -Werror=format-security -D_FORTIFY_SOURCE=2 -fPIC -I/usr/include/python3.5m -c trie.c -o build/temp.linux-x86_64-3.5/trie.o -O3
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.5/trie.o -o /home/petr_tik/Coding/bivittatus/ctrie.cpython-35m-x86_64-linux-gnu.so
free && sync && sudo sh -c "echo 3 > /proc/sys/vm/drop_caches" && free

...

python3 benchmark.py
PyTrie
Takes 0.000009s to instantiate before adding sorted words
Takes 0.231256s to add 18000 words
Takes 0.000593s to instantiate before adding random words
Takes 0.239599s to add 18000 random words
Takes 0.005769s to find 100 random words
Takes 0.001648s to look for, but fail to find, 800 missing words
cTrie
Takes 0.000529s to instantiate before adding sorted words
Takes 0.012475s to add 18000 words
Takes 0.000002s to instantiate before adding random words
Takes 0.011485s to add 18000 random words
Takes 0.000142s to find 100 random words
Takes 0.000375s to look for, but fail to find, 800 missing words

```

The C trie is faster in all cases apart from instantiating a new trie. As far as I understand, this is related to the fact that the bytecode for PyTrie is preloaded by the CPython interpreter, while the C library needs to load when it's first called. After that the speed improvde is at least a factor of 2. Searching for words inside the trie is at least an order of magnitude faster. 


## Where is the source? 

[On my GitHub](https://github.com/petr-tik/bivittatus)


## tl; dr

Writing own toy Python extension in C is fun, gives you a big performance win for limited investment and is easy thanks to great documentation and tooling. 

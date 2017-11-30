

Running the test below throws a segfault right now

```
def test_find_missing_missing_letter_before():
    tr = Trie()
    tr.add("bob")
    assert tr.find("alice") == 0

```

while running another returns the correct value

```
def test_find_missing_letters_exist_after():
    tr = Trie()
    tr.add("bob")
    assert tr.find("zlice") == 0
```

the problem is somehow allocating a 0x1 pointer to the first element of the cur->children[] array. The pointer is dereferenced correctly when "alice" invokes tr.find(). Pointer 0x1 isn't NULL, so it doesn't throw us out of the while loop, but makes us look at bad memory 


## needed python3.5-dbg 

gdb couldn't find debug symbols, so I needed to download them

```
sudo apt-get install python3.5-dbg
```

failed to resolve URLs, because my distro is old and has been retired for security reasons. 

This man came up with a piece of hacky sed magic. Now it works, but I should definitely upgrade my ubuntu.

https://gist.github.com/dergachev/f5da514802fcbbb441a1


## debugging all set up now

Run an awesome emacs gdb with the command below, it will drop you into the segfault straightaway

```
gdb -i=mi -ex r --args python3 test.py
```

head -n 50000 /usr/share/dict/words | tail -n 20000 | tr -d "[A-Z|']" | iconv -f utf8 -t ascii//TRANSLIT | uniq | head -n 18000 > clean_words

shuf clean_words > random_words

head -n 80000 /usr/share/dict/words | tail -n 1000 | tr -d "[A-Z|']" | iconv -f utf8 -t ascii//TRANSLIT | uniq | head -n 800 > missing_words

# Assignment: Cuckoo Hashing
[Wikipedia article on Cuckoo Hashing](https://en.wikipedia.org/wiki/Cuckoo_hashing)

## Hash Function Selection
Some easy (but not necessarily "good") hash functions for strings are:
* length of the string % m
* ((number of vowels) * 13 + (number of consonants)/2 ** 12) % m

A "good" hash function has some properties like:
* small changes in input result in 'large' changes in output
  * e.g. hashes for 'Andy' and 'Andi' are nowhere close to each other

There's a whole category for special hash functions called "cryptographic hash functions".
One property we'd really like for a cryptographic hash is for it to be "one way":
easy to compute the hash, hard to compute the 'seed' value

* write your own for one
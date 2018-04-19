# Table of Contents
1. [Challenge Description](README.md#challenge-description)
2. [Solution Approach](README.md#solution-approach)
3. [Tests](README.md#tests)

# Challenge Description
https://gist.github.com/gdb/4ec57fa1574099339b356f0274787e93

# Solution Approach
Python3 solution to the openai scholarship coding challenge as described above. This is an iterative solution not a recursive one, in order to not blow the stackc and ensure scalabilty.

The entire solution is contained in `autocomplete.py`. 3 python packages used `faker` `pygtrie` and `string`.

The algorithm of the solution approach is decribed at the top of the extract function.

A `Character Trie` was used from this package: http://pygtrie.readthedocs.io/en/latest/. Even though a Trie was not directly required for this solution, I chose to use it as it handles these types of problems well. It creates a node for every character in the username, and keeps tracks of the "leaves" of every branch allowing for flexibility and scalability. 

Additional capabilities include:
1. Once the trie is fully completed it contains the entire data set. Now the trie can be "queried" to give us all, not just the top 5 with the suffix "ab" for example.
2. The Trie can also be traversed to give us an output of minimal ammount of queries required to extract the entire data base.
3. These capabilities are not displayed in the code.

I have left in `myfactory` of words that I had used for testing. `myfactory` was created using this python package: https://faker.readthedocs.io/en/latest/ . 
faker generates fake data for you and it is a really fun tool I use to stress test my code.
Here I show how to create a random sampling of 1 billion fake words containing just lowercase english alphabets plus some interspersed z words for good measure. You can decrase the number of words of myfactory if you want to do lighter tests.

The database must be lexographically sorted and must not contain duplicates and is only made of lowercase ASCII letters (a-z) as described in the challenge description. 

# Tests
Did multiple tests, containing different ammount of words as well as a much wider array of interspersed z words
The databse test still present in `autocomplete.py`. Specs:
* usernames: ~1 billion (accounting for additional z words and removing duplicates)
* The assertion in `main` was proven correct in 4316 seconds (72 min)

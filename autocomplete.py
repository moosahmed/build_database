#!/usr/bin/env python3

from faker import Faker
import pygtrie
from string import ascii_lowercase


def extract(query, char='a'):
    """
    extract takes in a `query` API function (which returns the first 5 usernames, lexicographically sorted,
    that start with a prefix) and returns the sorted list of all usernames in the database.
    
    extract starts with char = 'a' and fills the outputs of every query into a trie
    
    For every query:
    
    # 1) If the length of the query output is = 5:
    Queries the current character plus the next letter in the last username of the query output.
    
    # 2) If the length of the query output < 5 & the last letter of the current character is not 'z':
    Queries the next lexographical alphabet
    
    # 3) If the length of the query output < 5 & last letter of the current character is 'z':
    The function keeps moving back one location in the current character till it finds a non 'z' letter.
    Takes the next alphabet at that location and iterates that into the query.
    
    # 4) If it can't find a non z letter in the current character and it's query output was less than 5:
    We have reached the lexographical end point
    The function terminates the while loop and returns all the keys of the Trie i.e all the usernames
    """
    t = pygtrie.CharTrie()
    terminate = False
    while terminate is False:
        q_out = query(char)
        for username in q_out:
            t[username] = True
        if len(q_out) == 5:
            (query, char) = (query, q_out[-1][:len(char) + 1])  # 1
        elif len(q_out) < 5:
            if char[-1] != 'z':
                (query, char) = (query, char[:-1] + ascii_lowercase[ascii_lowercase.index(char[-1]) + 1])  # 2
            else:
                a = 1
                while char[-a] == 'z' and a < len(char):
                    a += 1
                if char[-a] != 'z':
                    (query, char) = (query, char[:-a] + ascii_lowercase[ascii_lowercase.index(char[-a]) + 1])  # 3
                else:
                    terminate = True  # 4
    return t.keys()


def main():
    """Runs your solution -- no need to update (except to maybe try out different databases)."""
    myfactory = Faker()
    # database should be sorted lexographically and should not have any duplicate values
    # database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve",
    #             "evening", "event", "eventually", "mallory",
    database = sorted(list(set(myfactory.words(1000000000) +
                ["za", "zazb", "zazc", "zazd", "zaze", "zazy", "zazz", "zb", "zba", "zbc", "zbd", "zbe", "zbz"])))
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database


main()

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 05:48:02 2022

@author: aarid
"""

import itertools
from html.parser import HTMLParser
from collections import Counter, defaultdict


class StringObject:
    """Various functions for stored strings"""
    def __init__(self, string):
        self.string = string
        self.sub_string = None
        self.load_file = None
        self.save_file = None


    def __repr__(self):
        """Return a string representation of string object"""
        return self.string

    def append(self, sub_string):
        """
        Appends a sub_string to string, and returns the appended string.

        >>> test = StringObject()
        >>> test.string = 'This is my string'
        >>> print(test.string)
        This is my string
        >>> test.sub_string = ', but only for now.'
        >>> print(test.append(test.sub_string))
        This is my string, but only for now.
        """
        self.string = str(self.string) + sub_string
        return self.string

    def remove(self, sub_string):
        """
        Removes a sub_string from string, and returns the truncated string.

        >>> test = StringObject()
        >>> test.string = 'This is my string, but only for now.'
        >>> print(test.string)
        This is my string, but only for now.
        >>> test.sub_string = ', but only for now.'
        >>> print(test.remove(test.sub_string))
        This is my string
        >>> test.sub_string = 'This is my string,'
        >>> print(test.remove(test.sub_string))
        but only for now.
        """
        self.string = self.string.replace(sub_string, '')
        return self.string

    def mirror_string(self):
        """
        Returns the mirrored string of string.

        >>> test = StringObject()
        >>> test.string = 'This is my string'
        >>> print(test.string)
        This is my string
        >>> print(test.mirror_string())
        gnirts ym si sihT
        """
        mirror = str(self.string[::-1])
        return mirror

    def load_string(self, load_file):
        """Loads a string from load_file and returns that string."""
        with open(load_file) as self.string:
            self.string = self.string.read()
        return self.string

    def save_string(self, save_file):
        """Saves the string to save_file."""
        with open(save_file, 'w') as saved:
            saved.write(self.string)


class Anagram(StringObject):
    """Inherits from StringObject class and can get anagrams of string."""
    def __init__(self):
        super().__init__(self)
        self.string = None
        self.words = []

    def find_anagrams(self, words):
        anagramsDict = defaultdict(list)
        self.words = words
        for word in words:
            if len(word) > 2:
                anagramsDict[frozenset(dict(Counter(word)).items())].append(word)
        return [anagrams for key, anagrams in anagramsDict.items() if len(anagrams) > 1]


    def create_all_anagrams(self, string):
        """Takes string and returns a list of string's anagrams (permutations)."""
        anagrams = [''.join(perm) for perm in itertools.permutations(self.string)]
        return anagrams


class Palyndrome(StringObject):
    """Inherits from StringObject and can identify palindromes."""
    def __init__(self, string):
        super().__init__(self)
        self.string = string

    def find_palindromes(self):
        """Checks if mirrored string is equal to string.
        If true, returns the mirrored string."""
        mirror = StringObject.mirror_string(self)
        if mirror == str(self.string) and len(mirror) > 2:
            palindrome = mirror
            return palindrome


class ParserHTML(HTMLParser):
    """Inherits from HTMLParser in python standard library.
    Parses text from inside <p> tags, adds text to a list, returns the list"""
    data_list = []
    def __init__(self):
        HTMLParser.__init__(self)
        self.is_data = False
    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.is_data = True
    def handle_endtag(self, tag):
        if tag == 'p':
            self.is_data = False
    def handle_data(self, data):
        if self.is_data:
            self.data_list.append(data)
        return self.data_list

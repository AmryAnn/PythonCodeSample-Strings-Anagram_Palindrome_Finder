# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 05:59:03 2022

@author: aarid
"""

import urllib.request
import argparse
import string

import anpatools

def access_webpage(url):
    """
    Opens and reads a webpage from URL and returns raw HTML from webpage.
    """
    webpage = urllib.request.urlopen(url)
    content = webpage.read().decode()
    return content

def parse_page(content):
    """
    Takes raw html as input and parses text from <p> tags.
    Returns a list of parsed text
    """
    pars = anpatools.ParserHTML()
    pars.feed(str(content))
    parsed_data = pars.data_list
    return parsed_data

def clean_data(data_list):
    """
    Takes a list of strings and iterates through the list to make all letters 
    lowercase and remove punctuation. Appends the cleaned strings to a new 
    list. Returns the new list.
    """
    string_list = []
    for item in data_list:
        item = item.lower()
        item = item.translate(str.maketrans('', '', string.punctuation))
        string_list.append(item)
    return string_list

def split_sentence(string_list):
    """
    Takes a list of sentences or multi-word strings and iterates through the 
    list to split each sentence into a list of words. Iterates through the 
    words, and appends each word once to a new list. Returns new list.
    """
    word_list = []
    for items in string_list:
        words = items.split(' ')
        for word in words:
            word = word.replace('\n', '')
            word = word.replace('\\', '')
            if word != '' and word not in word_list:
                word_list.append(word)
    return word_list


#Add command line argument
parser = argparse.ArgumentParser(description='Process web url.')
parser.add_argument('--url', type=str, required=True,\
                    help='Web address to the page to analyze.')


#Assign command line arguments
args = parser.parse_args()
URL = args.url

# # #TEST
# URL = "https://web.ics.purdue.edu/~gchopra/class/public/pages/webdesign/05_simple.html"

#Function calls
web_content = access_webpage(URL)
parsed_list = parse_page(web_content)
data_strings = clean_data(parsed_list)
data_words = split_sentence(data_strings)

print("\n\nAnagrams:")
anagrams = anpatools.Anagram()
anagram_groups = anagrams.find_anagrams(data_words)
print(anagram_groups)

print("\n\nPalindromes:")
palindromes = [anpatools.Palyndrome(n) for n in data_words]
for palyndrome in palindromes:
    pal = palyndrome.find_palindromes()
    if pal is not None:
        print(pal)

# #Test
# URL = "https://web.ics.purdue.edu/~gchopra/class/public/pages/webdesign/05_simple.html"
# web_content = access_webpage(URL)
# print(web_content)
# parsed_list = parse_page(web_content)
# print(parsed_list)
# data_strings = clean_data(parsed_list)
# print(data_strings)
# data_words = split_sentence(data_strings)
# print(data_words)

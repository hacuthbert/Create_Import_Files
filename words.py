"""Retrieve and print words from a URL.

Usage:
    python3 words.py <URL>

Example:
    python3 words.py http://sixty-north.com/c/t.txt
"""
import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.
    
    Args:
        url: the URL of a UTF-8 text document.
        
    Retuns:
        a list of strings containing the words from the document.
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_words(items):
    """Print items one per line.

        Args:
            An interable series of printable items.
    """
    for item in items:
        print(item)

def main(url='http://sixty-north.com/c/t.txt'):
    """Print each word from a text document from at a URL.
    
        Args:
            url: The URL of UTF-8 text document.
    """
    words = fetch_words(url)
    print_words(words)

if __name__ == '__main__':
    main(sys.argv[1])    # The 0th arg is the module filename.
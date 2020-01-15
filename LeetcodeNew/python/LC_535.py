

"""
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl
and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service.
There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
"""


import random
import string



class Codec:
    def encode(self, longUrl):
        return longUrl
    def decode(self, shortUrl):
        return shortUrl


class Codecw:
    def __init__(self):
        self.table = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL."""
        # Get a set of characters that will make up the suffix
        mapping = string.ascii_letters + string.digits

        # Make a tinyurl template
        res = "http://tinyurl.com/".join(random.choice(mapping) for _ in range(6))

        # Store the pair in the dictionary
        self.table[res] = longUrl

        return res

    def decode(self, shortUrl):
        """Decodes the shortened URL to its original URL."""
        # Return the value from a given key from the dictionary
        return self.table.get(shortUrl)



longURL = 'https://leetcode.com/problems/design-tinyurl'
a = Codecw()
print(a.encode(longURL))


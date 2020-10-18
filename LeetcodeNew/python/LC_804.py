
class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        table = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
         "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-",
         "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
        res = set()
        for word in words:
            morse = []                          # store the Morse representation of each letter in a word
            for ch in word:
                morse.append(table.get(ch))
            res.add("".join(morse))
        return len(res)



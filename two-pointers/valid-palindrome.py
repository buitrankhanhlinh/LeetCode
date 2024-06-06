class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for character in s:
            if character.isalpha() or character.isnumeric():
                new += character
        new = new.lower()
        return new == new[::-1]